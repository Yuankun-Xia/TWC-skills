from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

import fitz


SECTION_RE = re.compile(
    r"^(?:[IVX]+\.\s+|[0-9]+\.\s+)?(ABSTRACT|INTRODUCTION|RELATED WORK|SYSTEM MODEL|SYSTEM MODEL AND PROBLEM FORMULATION|PROBLEM FORMULATION|METHODOLOGY|METHOD|PROPOSED METHOD|PROPOSED ALGORITHM|ALGORITHM DESIGN|CONVERGENCE ANALYSIS|PERFORMANCE ANALYSIS|SIMULATION RESULTS|NUMERICAL RESULTS|EXPERIMENTAL RESULTS|CONCLUSION|CONCLUSIONS)\b",
    re.IGNORECASE,
)

FIGURE_RE = re.compile(r"\b(?:Fig\.|Figure)\s*\d+", re.IGNORECASE)
TABLE_RE = re.compile(r"\bTable\s+[IVX0-9]+", re.IGNORECASE)

CLAIM_PATTERNS = [
    "we propose",
    "we develop",
    "we design",
    "we formulate",
    "we derive",
    "we analyze",
    "we prove",
    "we establish",
    "we investigate",
    "we optimize",
    "we present",
]

DOMAIN_PATTERNS = {
    "wireless federated learning": [r"\bfederated learning\b", r"\bfederated edge learning\b", r"\bwireless federated\b"],
    "over-the-air computation": [r"\bover[- ]the[- ]air\b", r"\baircomp\b", r"\bota aggregation\b"],
    "resource allocation": [r"\bresource allocation\b", r"\bscheduling\b", r"\bpower allocation\b", r"\bbeamforming\b"],
    "ris/irs": [r"\b(?:star[- ]?)?ris\b", r"\birs\b", r"\breconfigurable intelligent\b", r"\bintelligent reflecting\b"],
    "cell-free/mimo": [r"\bcell[- ]free\b", r"\bmimo\b", r"\bmassive mimo\b", r"\bhmimo\b"],
    "energy/privacy": [r"\benergy efficiency\b", r"\benergy harvesting\b", r"\bprivacy\b", r"\bdifferential privacy\b"],
    "uav/satellite/vehicular": [r"\buav\b", r"\bsatellite\b", r"\bvehicular\b", r"\bspace computing\b"],
    "semantic/foundation models": [r"\bsemantic communication\b", r"\bfoundation model\b", r"\bfine[- ]tuning\b", r"\bprompt\b"],
}


@dataclass
class PaperSummary:
    file: str
    title_guess: str
    page_count: int
    word_count_first_pages: int
    abstract_words: int
    section_headings: list[str]
    figure_mentions: int
    table_mentions: int
    domain_tags: list[str]
    claim_move_count: int


def normalize_space(text: str) -> str:
    text = text.replace("铿乧", "ffici").replace("鈥?", "-").replace("鈫?", "->")
    return re.sub(r"\s+", " ", text).strip()


def extract_text(pdf_path: Path, max_pages: int | None = None) -> tuple[str, int]:
    with fitz.open(pdf_path) as doc:
        pages = len(doc)
        upto = pages if max_pages is None else min(max_pages, pages)
        chunks = [doc[i].get_text("text") for i in range(upto)]
    return "\n".join(chunks), pages


def title_from_first_page(text: str, fallback: str) -> str:
    filename_title = fallback.removesuffix(".pdf").replace("_", " ")
    if len(filename_title.split()) >= 4:
        return filename_title
    lines = [normalize_space(x) for x in text.splitlines()]
    lines = [x for x in lines if len(x) > 8 and not x.lower().startswith(("ieee", "vol.", "accepted"))]
    for line in lines[:12]:
        if len(line.split()) >= 4 and not SECTION_RE.match(line):
            return line[:180]
    return filename_title


def abstract_word_count(text: str) -> int:
    match = re.search(r"\bAbstract\b\s*[-:.\s]*(.*?)(?=\bI\.\s+Introduction\b|\bIntroduction\b)", text, re.I | re.S)
    if not match:
        return 0
    abstract = normalize_space(match.group(1))
    return len(re.findall(r"[A-Za-z0-9]+", abstract))


def section_headings(text: str) -> list[str]:
    found: list[str] = []
    for raw in text.splitlines():
        line = normalize_space(raw)
        if len(line) > 90:
            continue
        match = SECTION_RE.match(line)
        if match:
            heading = match.group(1).upper()
            if heading not in found:
                found.append(heading)
    return found[:18]


def domain_tags(text: str) -> list[str]:
    low = text.lower()
    tags = []
    for tag, patterns in DOMAIN_PATTERNS.items():
        if any(re.search(pattern, low) for pattern in patterns):
            tags.append(tag)
    return tags


def claim_move_count(text: str) -> int:
    low = normalize_space(text.lower())
    count = 0
    for pat in CLAIM_PATTERNS:
        if pat in low:
            count += 1
    return count


def summarize_paper(pdf_path: Path) -> PaperSummary:
    first_text, pages = extract_text(pdf_path, max_pages=5)
    full_text, _ = extract_text(pdf_path, max_pages=None)
    return PaperSummary(
        file=pdf_path.name,
        title_guess=title_from_first_page(first_text, pdf_path.name),
        page_count=pages,
        word_count_first_pages=len(re.findall(r"[A-Za-z0-9]+", first_text)),
        abstract_words=abstract_word_count(first_text),
        section_headings=section_headings(full_text),
        figure_mentions=len(FIGURE_RE.findall(full_text)),
        table_mentions=len(TABLE_RE.findall(full_text)),
        domain_tags=domain_tags(full_text),
        claim_move_count=claim_move_count(first_text),
    )


def build_markdown(summaries: list[PaperSummary]) -> str:
    domain_counts = Counter(tag for s in summaries for tag in s.domain_tags)
    section_counts = Counter(h for s in summaries for h in s.section_headings)
    page_counts = [s.page_count for s in summaries]
    abstract_counts = [s.abstract_words for s in summaries if s.abstract_words]
    fig_counts = [s.figure_mentions for s in summaries]
    table_counts = [s.table_mentions for s in summaries]

    def avg(values: list[int]) -> float:
        return round(sum(values) / len(values), 1) if values else 0

    lines = [
        "# TWC 2026 Corpus Observations",
        "",
        "This report summarizes structural patterns from local user-provided TWC PDFs. It records reusable writing and presentation observations, not full paper text.",
        "",
        "## Corpus Snapshot",
        "",
        f"- Papers analyzed: {len(summaries)}",
        f"- Average pages: {avg(page_counts)}",
        f"- Average abstract length when detected: {avg(abstract_counts)} words",
        f"- Average figure mentions: {avg(fig_counts)}",
        f"- Average table mentions: {avg(table_counts)}",
        "",
        "## Dominant Technical Areas",
        "",
    ]
    for tag, count in domain_counts.most_common():
        lines.append(f"- {tag}: {count}")

    lines += [
        "",
        "## Frequent Section Signals",
        "",
    ]
    for heading, count in section_counts.most_common(12):
        lines.append(f"- {heading}: {count}")

    lines += [
        "",
        "## Reusable TWC Writing Moves",
        "",
        "- Frame the wireless system constraint before the algorithm: bandwidth, channel fading, CSI, device heterogeneity, energy budget, latency, privacy, or topology.",
        "- Turn the contribution into a coupled optimization or protocol design claim, not only a model-improvement claim.",
        "- Separate problem formulation from algorithm design. TWC papers often need the variables, constraints, and wireless assumptions to be reviewable before the solution narrative starts.",
        "- Pair convergence, communication cost, and energy/latency evidence. A performance gain alone is rarely enough for wireless FL or AirComp papers.",
        "- Use simulation sections as claim-evidence ladders: setup, baselines, convergence/performance, resource sensitivity, ablation or robustness, then parameter studies.",
        "",
        "## Abstract And Introduction Patterns",
        "",
        "- Abstracts commonly follow: wireless bottleneck -> missing capability -> proposed protocol/optimization/framework -> theoretical or algorithmic guarantee -> simulation evidence -> bounded implication.",
        "- Introductions work best when the unresolved gap is a coupled wireless-learning conflict, such as accuracy versus energy, latency versus staleness, privacy versus aggregation error, or CSI overhead versus beamforming quality.",
        "- Contributions should be listed only after the reader understands the system model and the exact bottleneck. Otherwise, the paper reads like a collection of modules.",
        "",
        "## Method And Problem Formulation Patterns",
        "",
        "- Start with network entities and timeline: server/edge/UAV/RIS/users, local training, uplink/downlink aggregation, scheduling rounds, and channel model.",
        "- Define objective, variables, constraints, and assumptions before the algorithm. Use consistent notation across system model, optimization, algorithm, and experiments.",
        "- For nonconvex or mixed-integer formulations, state why decomposition, relaxation, alternating optimization, Lyapunov/MDP, or learning-based control is necessary.",
        "- If the paper has theoretical analysis, connect each theorem or lemma to the practical design decision it justifies.",
        "",
        "## Figure And Table Patterns",
        "",
        "- Typical TWC figure sets include system model, algorithm workflow, convergence curves, accuracy/loss versus communication rounds, energy/latency tradeoffs, sensitivity to SNR/devices/bandwidth/data heterogeneity, and ablation bars.",
        "- Result figures should preserve x-axis meaning carefully: communication rounds, global iterations, transmit power, number of devices, bandwidth, SNR, CSI error, or data heterogeneity each support a different claim.",
        "- Tables are most useful for system parameters, complexity comparison, baseline summary, or final performance/energy/latency comparison.",
        "",
        "## Paper Inventory",
        "",
    ]
    for idx, summary in enumerate(summaries, start=1):
        tags = ", ".join(summary.domain_tags) if summary.domain_tags else "uncategorized"
        lines.append(f"{idx}. {summary.title_guess}")
        lines.append(f"   - File: `{summary.file}`")
        lines.append(f"   - Tags: {tags}")
        lines.append(f"   - Pages: {summary.page_count}; figures: {summary.figure_mentions}; tables: {summary.table_mentions}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_dir", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    pdfs = sorted(args.pdf_dir.glob("*.pdf"))
    summaries = [summarize_paper(path) for path in pdfs]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build_markdown(summaries), encoding="utf-8")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps([asdict(s) for s in summaries], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
