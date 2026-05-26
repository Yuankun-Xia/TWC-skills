# 2026 IEEE TWC Paper Figure Observations

This note captures page-level figure patterns observed from 4 real IEEE Transactions papers
in wireless communications / federated learning (2025–2026). These papers represent the same
genre as IEEE TWC — two-column IEEEtran format, quantitative results, system diagrams.

## Sampled papers

1. `Adaptive_Rank_Allocation_for_Federated_PEFT` — IEEE Trans. Computers, Vol. 75, No. 4, April 2026
   - LoRA rank allocation, federated learning, 15 figures
2. `Energy-Efficient_Federated_Edge_Learning_With_Streaming_Data` — IEEE Trans. Communications, Vol. 73, No. 2, Feb 2025
   - Lyapunov optimization, streaming data, 8 figures
3. `Fed-HeLLo_Efficient_Federated_Foundation_Model_Fine-Tuning` — IEEE TNNLS, Vol. 36, No. 10, Oct 2025
   - Heterogeneous LoRA allocation, 6 figures
4. `JCSRC_Joint_Client_Selection_and_Resource_Configuration` — IEEE Trans. Computers, Vol. 74, No. 12, Dec 2025
   - Multi-task FL, MARL, resource config, 12 figures

---

## Archetype 1: Quantitative performance line plots

The dominant figure type in all sampled papers (70%+ of all figures). Shows convergence,
accuracy, loss, or resource metrics over training rounds/epochs.

Actionable rules:

- Use **1x2 side-by-side subplot grid** as the default. 2x2, 2x3, 2x4 also common.
- **Grid lines: ON**. Light gray (`#b0b0b0` or `#7f7f7f`), thin (0.4pt), both horizontal
  and vertical. Grid is visible but subordinate — never more salient than data lines.
- **Full boxed frame**. Top and right spines are visible. This is standard IEEE plot
  convention, NOT the Nature/minimalist style.
- **White background** (`#ffffff`), no shading in the plot area.
- **Line weight**: 1pt for primary data series, distinct from grid lines.
- **Markers**: Small circles (~3pt) at data points on lines.
- **Line styles**: Solid for proposed method, dashed for baselines. This is a common
  pattern but not universal — some papers use all-solid lines with color differentiation.
- **Legend**: Inside the plot area, typically upper-right corner. Boxed with thin border
  or frameless. Colored rectangle patches matching line colors.
- Axis labels: ~7–8pt Times-Roman. Tick labels: ~7pt.
- X-axis: "Training Rounds" or "Communication Rounds". Y-axis: metric name.
- **Error/variance**: If shown, uses light pastel shading behind lines (confidence bands)
  rather than individual error bars. This is seen in 2 of 4 papers.

Recommended palette for line plots:

```python
LINE_PALETTE = {
    "proposed":   "#0071bc",  # blue — hero method (always blue across all papers)
    "baseline_1": "#d95218",  # orange
    "baseline_2": "#77ac2f",  # green
    "baseline_3": "#7d2e8e",  # purple
    "baseline_4": "#ecb01f",  # gold
    "baseline_5": "#4dbded",  # cyan
}
```

---

## Archetype 2: Grouped bar charts for method comparison

Second most common type. Used for "method A vs B vs C across datasets/conditions."

Actionable rules:

- **Vertical grouped bars**, solid fill, no patterns or hatching.
- **Colors match the line-plot palette** — same method = same color across all figures
  in the paper. This cross-figure consistency is non-negotiable.
- **Error bars: T-cap style** on top of bars, thin black/dark lines. (Note: 3 of 4
  papers use error bars on bar charts.)
- X-axis group labels: horizontal text, ~7pt Times-Roman.
- Legend: outside plot area (to the right or above) when many methods; inside when few.
- Bar charts often span wider than line plots to accommodate grouped bars.
- Value labels sometimes placed above bars for key comparisons.

Bar-edge treatment:
- Thin dark outline on bars (0.3–0.5pt, `#333333` or black) — adds definition when
  fills are light.

---

## Archetype 3: System architecture / block diagrams

Every paper has 1–2 of these. Explains the proposed framework visually.

Actionable rules:

- **Pastel fills** for boxes: light blue (`#c4d7e0`, `#d9dff1`), light yellow (`#fff2cb`),
  light green (`#b6daa0`), light peach (`#f9dbcc`).
- **Black outlines** on boxes, ~0.5–1pt.
- **Black solid arrows** for data/control flow, standard arrowhead tips.
- **Font**: Times-Roman, ~7–8pt, centered in boxes.
- **Nesting**: Dashed-border containers (`#ff0000` or black, dashed) grouping related
  components.
- Diagram width: single-column (~3.5 inches). Height: can be substantial (up to 60%
  of column).
- **Semantic color coding**: blue tones = server/cloud/pre-trained modules; green tones =
  client/local training; orange = trainable/fine-tuned modules; red = emphasis/critical
  path.
- Keep a 1:1 mapping between diagram colors and method colors where possible — e.g.,
  if the proposed method is blue in plots, use blue family for "our method" boxes in
  diagrams.

---

## Archetype 4: Heatmaps

Less common but present (1 of 4 papers). Used to show rank distribution or energy
distribution across clients/rounds.

Actionable rules:

- **Sequential color scale**: light yellow → dark blue or light cream → dark orange.
  NOT diverging (no red-white-blue).
- Grid cells have thin borders or no borders — white gutters between cells.
- Embedded colorbar: small (~36×680px JPEG), placed to the right of the heatmap.
- Axis: "Layer" (y) vs "Rank" (x) or "Round" vs "Client".
- Cell text labels only for small heatmaps (<20 cells per dimension).

Recommended sequential scale:
```python
HEATMAP_COLORS = ["#fff9c9", "#fff1ac", "#ffb733", "#ff6400", "#ea4a00"]
```

---

## Archetype 5: Pareto / tradeoff scatter

Present in 2 of 4 papers (Lyapunov paper, resource allocation paper). Plots one metric
against another to show the tradeoff frontier.

Actionable rules:

- **Scatter markers**: larger than line-plot markers (6–8pt), with thin black edge.
- **Log scale on y-axis**: common when queue/energy spans orders of magnitude.
- **Arrow annotations**: used to highlight the advantage direction (e.g., "better" corner).
- Method label placed directly beside each marker (no detached legend needed when
  methods are spatially separated).
- **Hero method**: larger marker, thicker edge, visually distinct but same blue as
  in other figures.

---

## Cross-cutting IEEE rules from the sample

### Typography (CRITICAL)

- **Times-Roman** (NimbusRomNo9L) for ALL figure text: captions, axis labels, tick
  labels, legends, annotations. NO sans-serif in figures (except rare Helvetica for
  copyright stamps in page footers).
- **Figure captions: 8pt** Times-Roman, below the figure, left-aligned.
- **Math in figures: Computer Modern** (CMMI, CMR, CMSY, CMEX) — standard LaTeX math
  fonts.
- Body text: 10pt; Section headings: 10pt Bold.
- Subfigure labels: (a), (b), (c) in ~7pt Times-Roman, near top-left of each panel.

### Color discipline

- **Proposed method = blue, always**. This is the single most consistent rule across
  all 4 papers.
- **One method = one color**, maintained across all figures in the paper.
- Colors are **desaturated** — no pure red `#ff0000`, no pure green `#00ff00`, no
  pure blue `#0000ff` (except in one paper's vector plots). Prefer perceptual midtones.
- **Red** is reserved for emphasis/callouts/arrows, not used as a method color unless
  it's the "bad" baseline.
- **3–5 method colors** is standard. More than 6 methods in one plot requires
  rethinking the comparison.
- Diagrams use **pastel versions** of the method colors — same hue, lower saturation.

### Grid lines

- **Grid lines are PRESENT and EXPECTED** in IEEE engineering papers. This is the
  biggest difference from Nature/biology conventions.
- Light gray (`#b0b0b0` or `#7f7f7f`), thin (0.35–0.5pt).
- Both major and minor grid lines in some papers (dual-level gray).
- Grid is always behind data (zorder below data artists).

### Spines / axes frame

- **Full boxed frame** — all four spines visible. Top and right spines are NOT hidden.
  This differs from the minimalist Nature convention.
- Axis line width: 0.6–0.8pt, black or dark gray (`#262626`).
- Tick direction: inward (standard matplotlib default).

### Legend

- **Inside plot area** preferred for line plots (saves space in single-column layout).
- Outside (right side or top) for bar charts with many methods.
- Frameless or thin-bordered.
- Colored rectangle patches (not lines) in legend entries.

### Figure caption format

- "Fig. N. Description text." — "Fig." in same font weight as description (not bold).
- Multi-sentence for complex figures.
- Subfigure labels in caption: "(a) ... (b) ..."

### Layout dimensions

- Single-column figure: ~3.5 inches (251pt) wide.
- Wide figure (spanning most of text width): ~5.0–5.5 inches.
- Figure height varies by content but rarely exceeds 40% of page height.
- DPI: vector preferred (PDF/EPS export). Raster only for complex multi-panel figures
  (rendered at 150–200 DPI effective).

---

## What NOT to copy from Nature/biology conventions

- **Do not use Arial/sans-serif** for figure text. IEEE papers use Times-Roman.
- **Do not hide top/right spines**. Full boxed frame is standard in IEEE engineering.
- **Do not remove grid lines**. Grid lines are expected and present in all sampled papers.
- **Do not use pure/saturated colors**. IEEE papers use desaturated, colorblind-aware palettes.
- **Do not force legends out of every panel**. Inside-plot legends are common and
  space-efficient.
- **Do not use black** as a hero method color. Black = axes, text, grid infrastructure.
  Blue = proposed method.
- **Do not use asymmetric layouts** (hero panel + small support panels). IEEE multi-panel
  figures prefer equal-sized subplot grids (1x2, 2x2, 2x3).
- **Do not put panel labels as large bold badges**. Small ~7pt Times-Roman "(a)" in the
  plot corner is sufficient.
- **Do not use dark backgrounds** for any plot. White background is universal.

---

## Palette quick-reference

### For quantitative plots (line, bar, scatter)

```python
IEEE_QUANT_PALETTE = {
    "proposed":    "#0F4D92",  # deep blue — hero / proposed method
    "baseline_1":  "#D9544D",  # muted red
    "baseline_2":  "#4DAF4A",  # muted green
    "baseline_3":  "#E78A2E",  # muted orange
    "baseline_4":  "#984EA3",  # muted purple
    "baseline_5":  "#A6CEE3",  # light blue
    "neutral":     "#999999",  # grey for reference/hard-energy
}
```

### For architecture diagrams

```python
IEEE_DIAGRAM_FILLS = {
    "server_cloud":  "#C4D7E0",  # light blue
    "client_local":  "#B6DAA0",  # light green
    "trainable":     "#FFCA8B",  # light peach/orange
    "communication": "#FFF2CB",  # light yellow
    "emphasis":      "#FF0000",  # red — sparse, for callouts only
    "group_bg":      "#F2F2F2",  # light grey — container backgrounds
}
```

### For heatmaps

```python
IEEE_HEATMAP_SEQUENTIAL = ["#FFF9C9", "#FFF1AC", "#FFB733", "#FF6400", "#EA4A00"]
```

---

## Anti-patterns observed (and to avoid)

1. **Multi-hue rainbow palette for method comparison** — one paper's radar chart used
   6 fully distinct hues (red, teal, blue, purple, gold, navy). This is hard to read
   and print. Prefer a tighter palette.
2. **CMYK JPEG for vector-suitable content** — one paper rendered an 8-panel line plot
   grid as 400×300px JPEGs. Vector PDF/SVG is always preferred for line plots and bar
   charts.
3. **Inconsistent method-to-color mapping** — one paper changed the hero color from
   green (in vector figures) to blue-green (in raster figures). This breaks reader trust.
