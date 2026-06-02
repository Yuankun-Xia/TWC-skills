# Published Article Patterns

Use this file when polishing should improve scientific argument, not just English.
The patterns below are distilled from curated IEEE and top communications journals
research articles, especially IEEE Transactions on Wireless Communications style
papers on wireless federated learning, AirComp, RIS/IRS, cell-free MIMO, edge
intelligence, semantic communications, and resource allocation. Do not copy their
wording. Use the patterns to diagnose and reshape the user's manuscript.

## Abstract pattern

Strong abstracts usually move in six steps:

1. name the field-scale problem or opportunity
2. show why existing approaches are incomplete
3. state the specific protocol, optimisation problem, algorithm, architecture, or
   analytical result
4. give the decisive result with wireless operating conditions, comparison, or
   constraint
5. explain why the result changes a communication-learning design tradeoff
6. close with scope, application, or boundary

Polishing rule: if an abstract starts with the method, add the problem and gap
first. If it ends with enthusiasm, replace it with a bounded implication.

## Introduction pattern

High-performing TWC introductions often use `system setting -> coupled bottleneck
-> prior technical families -> missing capability -> present study`.

- `System setting`: identify the wireless network, edge-learning, AirComp, RIS/IRS,
  MIMO, UAV, satellite, vehicular, or semantic-communication scenario.
- `Bottleneck`: name the coupled barrier, such as accuracy-energy, latency-staleness,
  CSI overhead-beamforming quality, privacy-aggregation error, or convergence-
  resource consumption.
- `Prior attempts`: acknowledge existing strategies fairly.
- `Missing capability`: explain what those strategies still cannot do under the
  relevant channel, resource, topology, heterogeneity, or privacy condition.
- `Present study`: state what the paper does, not what it hopes to do.

Polishing rule: keep the gap narrow enough that the study can actually fill it.
Avoid novelty claims that depend on weakening prior work.

## Results pattern

Results sections usually work best as an evidence ladder:

1. overview of the system, workflow or design space
2. simulation setup and fair baseline/protocol definition
3. convergence, accuracy, rate, distortion, or feasibility result
4. energy, latency, communication overhead, privacy, or resource tradeoff
5. ablation, sensitivity, robustness, or parameter study
6. operating-boundary or scalability analysis

Each Results paragraph should begin with the question or test, then report the
observation, then give the quantitative or comparative support. Interpretation
should be brief unless the paragraph is explicitly bridging into Discussion.

## Discussion pattern

Effective Discussion writing starts from the central advance and then widens:

- what the study demonstrates
- why the evidence is credible
- how it changes an existing wireless design rule, resource-control workflow, or
  communication-learning tradeoff
- what constraints remain
- what future work is enabled, without promising untested outcomes

Do not turn the Discussion into a second Results section. Use it to state what
the results mean and where that meaning stops.

## Conclusion pattern

IEEE-style conclusions are compact. They usually combine:

1. the contribution in one sentence
2. the mechanism, performance or feasibility evidence that supports it
3. the scale or application implied by the work
4. one boundary condition, if the claim could otherwise overreach

Polishing rule: remove new data from conclusions. Preserve confidence, but add
scope control.

## Title pattern

Strong titles are concrete and searchable. They often combine:

- object or system
- action or capability
- application, scale or consequence

Prefer titles that reveal the central scientific move. Avoid titles that sound
like grant aims, slogans or broad fields.

## Sentence-level pattern

Published prose often looks simple because each sentence does one job:

- background sentence: field stake or known fact
- gap sentence: unresolved limitation
- method sentence: what was done
- result sentence: observed effect plus condition
- comparison sentence: baseline or previous state
- implication sentence: meaning with scope
- limitation sentence: boundary or dependency

When polishing, label each sentence by job. If two jobs compete in one sentence,
split it or subordinate one job.

## Overclaim checks from article patterns

Flag and soften claims when:

- a simulation result under one channel or topology is written as an immediate
  field-wide solution
- a single protocol, model, dataset, or resource setting is described as
  universally applicable
- correlation is rewritten as mechanism
- a comparison lacks a fair baseline
- a future application is stated as an achieved outcome

Good IEEE-style prose can be ambitious, but the ambition must be attached to
evidence, scale and boundary.
