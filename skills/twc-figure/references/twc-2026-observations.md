# TWC Figure Observations

Use this file when the user asks for IEEE/TWC-style figures, figure audits, or
paper-style visual revisions. The observations combine IEEE engineering figure
conventions with structural patterns from 50 local user-provided TWC PDFs. Do not
copy paper content. Use the patterns to choose figure logic, layout, labels, and
review checks.

## Corpus-Level Signals

- Papers analyzed in the current local corpus: 50.
- Average paper length: about 16 pages.
- Average figure mentions: about 25 per paper.
- Average table mentions: about 5 per paper.
- Common section signals: Abstract, Introduction, System Model, Method, Problem
  Formulation, Proposed Algorithm, Convergence Analysis, Simulation Results,
  Numerical Results, Performance Analysis, and Conclusion.
- Dominant topics: resource allocation, wireless federated learning, energy and
  privacy, UAV/satellite/vehicular networking, over-the-air computation,
  cell-free/MIMO, RIS/IRS, and semantic/foundation-model communications.

## Expected Figure Set In A TWC Paper

For wireless FL, AirComp, RIS/IRS, cell-free MIMO, and resource-allocation papers,
a complete figure package usually includes:

1. system model or network architecture,
2. proposed workflow, protocol, or algorithm block diagram,
3. convergence curves over communication rounds or global iterations,
4. primary performance comparison, such as accuracy, loss, rate, distortion, or
   outage,
5. energy, latency, communication overhead, or power-consumption tradeoff,
6. sensitivity to wireless conditions such as SNR, bandwidth, channel error,
   number of devices, antennas, RIS elements, APs, or UAVs,
7. data/client heterogeneity or participation-ratio analysis when FL is central,
8. ablation or module comparison when the paper claims a technical design choice,
9. complexity/runtime table or parameter table when algorithmic cost matters.

## Quantitative Line Plots

The dominant figure type in TWC-style wireless-learning papers is the multi-series
line plot. Use it for convergence, loss, accuracy, energy, latency, queue length,
distortion, outage, or rate trends.

Actionable rules:

- Use 1x2 or 2x2 subplot grids as the default for related metrics or datasets.
- Keep a full boxed frame: top and right spines remain visible.
- Use light grey grid lines behind the data. IEEE engineering plots usually keep
  grids visible.
- Put the proposed method in blue and keep this mapping consistent across all
  figures.
- Use solid lines for the proposed method and dashed or marker-differentiated
  lines for baselines when helpful.
- Label the x-axis with the real independent variable: communication rounds,
  global iterations, transmit power, SNR, bandwidth, number of devices, number of
  antennas, CSI error, or data heterogeneity.
- Do not reuse a generic x-axis label when the claim depends on the wireless
  operating condition.

Recommended palette:

```python
IEEE_QUANT_PALETTE = {
    "proposed": "#0F4D92",
    "baseline_1": "#D9544D",
    "baseline_2": "#4DAF4A",
    "baseline_3": "#E78A2E",
    "baseline_4": "#984EA3",
    "baseline_5": "#A6CEE3",
    "neutral": "#999999",
}
```

## Bar Charts And Tables

Use grouped bars for final method comparisons across datasets, channel settings,
or resource budgets. Use tables for system parameters, complexity, baseline
summaries, or compact final comparisons.

Rules:

- Keep method colors consistent with the line plots.
- Use muted fills and thin dark outlines.
- Add error bars only when variance or repeated trials are actually available.
- Keep metric direction explicit in labels or captions, for example higher
  accuracy is better, lower latency is better, or lower energy is better.
- For tables, use booktabs style, consistent numeric precision, and units in
  headers.

## System And Algorithm Diagrams

Use diagrams to make the communication-learning pipeline reviewable before the
math or experiments.

Typical components:

- server, edge server, base station, access points, clients, UAVs, vehicles,
  satellites, RIS/IRS, antennas, or data owners,
- local training, gradient/model upload, over-the-air aggregation, beamforming,
  scheduling, quantization, encryption/privacy, and global update,
- time slots, communication rounds, local epochs, or asynchronous/staleness
  loops.

Rules:

- Use pastel fills with dark outlines.
- Use arrows for data flow, control flow, and wireless links.
- Keep one visual mapping between entities and colors across the paper.
- Avoid decorative network diagrams that do not reveal the optimization variables
  or protocol timeline.

## Tradeoff And Sensitivity Plots

TWC reviewers often look for whether a method survives changes in wireless
conditions.

Common x-axes:

- SNR, transmit power, bandwidth, noise variance, path-loss exponent,
- number of clients, scheduled devices, APs, antennas, RIS elements, or UAVs,
- non-IID degree, local epochs, participation ratio, or data size,
- CSI error, aggregation noise, privacy budget, or quantization bits.

Common y-axes:

- test accuracy, training loss, convergence rounds,
- energy consumption, latency, communication overhead,
- MSE, distortion, outage probability, achievable rate,
- queue length, reward, cost, or objective value.

The caption should state the operating condition and the claim. A parameter sweep
without a claim reads like filler.

## Anti-Patterns

- Do not hide top/right spines for TWC quantitative plots.
- Do not remove grid lines from engineering plots unless the target journal or
  user explicitly requests a minimalist style.
- Do not use saturated rainbow palettes for many methods.
- Do not change the proposed-method color between figures.
- Do not squeeze dense multi-panel plots into tiny single-column space. Split or
  simplify instead.
- Do not plot accuracy only when the paper claims energy, latency, privacy,
  convergence, or resource efficiency.
- Do not report a wireless result without showing the relevant wireless
  operating condition.
