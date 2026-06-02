# Article Architecture

Use this reference when writing or rebuilding manuscript sections. The patterns
come from curated IEEE Transactions on Wireless Communications and related
communications-journal papers. They are structural patterns, not wording
templates. For wireless FL, AirComp, RIS/IRS, cell-free MIMO, semantic
communications, or resource-allocation papers, also load
`references/twc-2026-corpus-observations.md`.

## Full-paper argument

A strong paper can usually be reduced to:

`wireless-system need -> coupled communication/learning bottleneck -> proposed
protocol, optimisation, or architecture -> theoretical or algorithmic support ->
simulation evidence -> implication with operating boundary`

Before drafting, force the user's material into this chain. If one link is
missing, mark it as missing rather than writing around it.

## Abstract

Recommended paragraph movement:

1. Wireless context or system bottleneck.
2. Why existing communication, learning, or optimisation routes do not fully
   resolve the bottleneck.
3. What this paper introduces: protocol, architecture, optimisation problem,
   algorithm, analysis, or resource-control mechanism.
4. The key analytical result, convergence property, complexity result, or
   algorithmic guarantee when available.
5. Simulation evidence with quantitative or comparative support.
6. Bounded implication tied to the operating regime.

Useful diagnostics:

- If the abstract begins with `Here, we`, it may be missing context.
- If it ends with a broad promise, it may need scope control.
- If it contains no number, comparison or concrete test, it may feel ungrounded.

## Introduction

Use a controlled funnel:

1. Establish the communication-system setting and why it matters.
2. Explain the coupled bottleneck, such as accuracy-energy, latency-staleness,
   CSI overhead-beamforming quality, privacy-aggregation distortion, or
   convergence-resource consumption.
3. Treat prior work fairly by technical family, not paper-by-paper chronology.
4. Identify the remaining capability gap and its technical reason.
5. State the present study as a direct response to that gap.

Avoid:

- a literature list without a narrowing logic
- claiming novelty by dismissing prior work
- announcing results before the reader understands the question

## Results

Arrange Results as an evidence ladder:

1. simulation setup, system parameters, datasets, channel model, and baselines
2. convergence or feasibility evidence
3. primary performance result
4. energy, latency, communication overhead, privacy, or resource tradeoff
5. ablation, sensitivity, or robustness analysis
6. operating-boundary discussion, such as SNR, bandwidth, device count, CSI
   error, mobility, or data heterogeneity

Subsection opening rule:

`To evaluate [claim] under [wireless condition], we compare [method] with
[baselines] using [metric].`

Then report the result and evidence. Keep interpretation short unless the
paragraph explicitly transitions toward Discussion.

## Discussion

Discussion should widen from finding to meaning:

1. central advance
2. why the theory and simulation evidence support it
3. how it changes a communication-learning design rule or resource-control
   workflow
4. how it relates to previous wireless FL, AirComp, RIS/IRS, MIMO, or edge
   intelligence studies
5. what limits or dependencies remain, such as CSI assumptions, synchronization,
   scalability, mobility, privacy budget, or non-IID severity
6. what future work is now plausible

Do not restate every figure. Select the evidence that changes interpretation.

## Conclusion

Use a compact four-part close:

1. This work demonstrates or establishes the main contribution.
2. The decisive evidence is named.
3. The broader implication is stated.
4. The boundary condition is clear.

Conclusions should not introduce new data, new citations or new mechanisms.

## Title

Good titles are concrete and searchable:

`system/object + capability/action + application/consequence`

Examples of title logic:

- protocol plus wireless-learning setting
- optimisation target plus system architecture
- resource-control mechanism plus operating constraint
- communication primitive plus AI/edge-intelligence task

Avoid vague prestige words such as `novel`, `advanced`, `powerful`, `green`,
`efficient` unless they are made concrete by the rest of the title.
