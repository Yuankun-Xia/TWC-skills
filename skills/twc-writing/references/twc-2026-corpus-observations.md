# TWC 2026 Corpus Observations

This report summarizes structural patterns from local user-provided TWC PDFs. It records reusable writing and presentation observations, not full paper text.

## Corpus Snapshot

- Papers analyzed: 50
- Average pages: 16.2
- Average abstract length when detected: 351.4 words
- Average figure mentions: 25.3
- Average table mentions: 4.9

## Dominant Technical Areas

- resource allocation: 50
- wireless federated learning: 46
- energy/privacy: 42
- uav/satellite/vehicular: 38
- over-the-air computation: 35
- cell-free/mimo: 33
- ris/irs: 22
- semantic/foundation models: 13

## Frequent Section Signals

- ABSTRACT: 50
- INTRODUCTION: 50
- CONCLUSION: 48
- SYSTEM MODEL: 46
- SIMULATION RESULTS: 32
- METHOD: 31
- CONVERGENCE ANALYSIS: 19
- NUMERICAL RESULTS: 12
- PROBLEM FORMULATION: 11
- PROPOSED ALGORITHM: 10
- PROPOSED METHOD: 9
- PERFORMANCE ANALYSIS: 6

## Reusable TWC Writing Moves

- Frame the wireless system constraint before the algorithm: bandwidth, channel fading, CSI, device heterogeneity, energy budget, latency, privacy, or topology.
- Turn the contribution into a coupled optimization or protocol design claim, not only a model-improvement claim.
- Separate problem formulation from algorithm design. TWC papers often need the variables, constraints, and wireless assumptions to be reviewable before the solution narrative starts.
- Pair convergence, communication cost, and energy/latency evidence. A performance gain alone is rarely enough for wireless FL or AirComp papers.
- Use simulation sections as claim-evidence ladders: setup, baselines, convergence/performance, resource sensitivity, ablation or robustness, then parameter studies.

## Abstract And Introduction Patterns

- Abstracts commonly follow: wireless bottleneck -> missing capability -> proposed protocol/optimization/framework -> theoretical or algorithmic guarantee -> simulation evidence -> bounded implication.
- Introductions work best when the unresolved gap is a coupled wireless-learning conflict, such as accuracy versus energy, latency versus staleness, privacy versus aggregation error, or CSI overhead versus beamforming quality.
- Contributions should be listed only after the reader understands the system model and the exact bottleneck. Otherwise, the paper reads like a collection of modules.

## Method And Problem Formulation Patterns

- Start with network entities and timeline: server/edge/UAV/RIS/users, local training, uplink/downlink aggregation, scheduling rounds, and channel model.
- Define objective, variables, constraints, and assumptions before the algorithm. Use consistent notation across system model, optimization, algorithm, and experiments.
- For nonconvex or mixed-integer formulations, state why decomposition, relaxation, alternating optimization, Lyapunov/MDP, or learning-based control is necessary.
- If the paper has theoretical analysis, connect each theorem or lemma to the practical design decision it justifies.

## Figure And Table Patterns

- Typical TWC figure sets include system model, algorithm workflow, convergence curves, accuracy/loss versus communication rounds, energy/latency tradeoffs, sensitivity to SNR/devices/bandwidth/data heterogeneity, and ablation bars.
- Result figures should preserve x-axis meaning carefully: communication rounds, global iterations, transmit power, number of devices, bandwidth, SNR, CSI error, or data heterogeneity each support a different claim.
- Tables are most useful for system parameters, complexity comparison, baseline summary, or final performance/energy/latency comparison.

## Paper Inventory

1. Adaptive Power Control and Data Sampling for Energy-Efficient Over-the-Air Federated Edge Learning
   - File: `Adaptive Power Control and Data Sampling for Energy-Efficient Over-the-Air Federated Edge Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 28; tables: 4
2. AirComp-Assisted Asynchronous Federated Learning for UAV Swarms A Self-Adaptive Aggregation Scheme to Tackle Model Staleness
   - File: `AirComp-Assisted Asynchronous Federated Learning for UAV Swarms A Self-Adaptive Aggregation Scheme to Tackle Model Staleness.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, uav/satellite/vehicular
   - Pages: 15; figures: 39; tables: 4
3. Biased Federated Learning Under Wireless Heterogeneity
   - File: `Biased Federated Learning Under Wireless Heterogeneity.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy
   - Pages: 14; figures: 6; tables: 0
4. Communication-and-Computation Efficient Split Federated Learning in Wireless Networks Gradient Aggregation and Resource Management
   - File: `Communication-and-Computation Efficient Split Federated Learning in Wireless Networks Gradient Aggregation and Resource Management.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 15; figures: 19; tables: 2
5. Decentralized Federated Learning With Energy Harvesting Devices
   - File: `Decentralized Federated Learning With Energy Harvesting Devices.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 10; tables: 2
6. Efficient Asynchronous Federated Edge Learning Oriented Tasks Scheduling and Resources Allocation in Dynamic Multitasks MEC Networks
   - File: `Efficient Asynchronous Federated Edge Learning Oriented Tasks Scheduling and Resources Allocation in Dynamic Multitasks MEC Networks.pdf`
   - Tags: wireless federated learning, resource allocation, energy/privacy, uav/satellite/vehicular
   - Pages: 15; figures: 32; tables: 2
7. Energy-Efficient Beamforming Design With Partial CSI Feedback for RIS-Assisted Systems
   - File: `Energy-Efficient Beamforming Design With Partial CSI Feedback for RIS-Assisted Systems.pdf`
   - Tags: resource allocation, ris/irs, cell-free/mimo, uav/satellite/vehicular
   - Pages: 15; figures: 14; tables: 5
8. Energy-Efficient Edge Scheduling and Resource Allocation for NOMA-Based Hierarchical Federated Learning
   - File: `Energy-Efficient Edge Scheduling and Resource Allocation for NOMA-Based Hierarchical Federated Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 17; figures: 17; tables: 10
9. Energy-Efficient Federated Edge Learning for Small-Scale Datasets in Large IoT Networks
   - File: `Energy-Efficient Federated Edge Learning for Small-Scale Datasets in Large IoT Networks.pdf`
   - Tags: wireless federated learning, resource allocation, ris/irs, cell-free/mimo, uav/satellite/vehicular
   - Pages: 17; figures: 32; tables: 5
10. Fast and Robust Channel Estimation for HMIMO A Graph-Based Wavenumber-Domain Approach
   - File: `Fast and Robust Channel Estimation for HMIMO A Graph-Based Wavenumber-Domain Approach.pdf`
   - Tags: resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 17; figures: 48; tables: 6
11. Federated Learning Over Device-Centric Cell-Free Networks A Long-Term Perspective
   - File: `Federated Learning Over Device-Centric Cell-Free Networks A Long-Term Perspective.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 32; tables: 4
12. Federated Learning Over Wireless Networks Optimizing Performance With NOMA and Power Allocation
   - File: `Federated Learning Over Wireless Networks Optimizing Performance With NOMA and Power Allocation.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, energy/privacy
   - Pages: 13; figures: 16; tables: 1
13. Federated Learning With Controlled Descent Under Fading Convergence and Energy Implications
   - File: `Federated Learning With Controlled Descent Under Fading Convergence and Energy Implications.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, energy/privacy
   - Pages: 16; figures: 18; tables: 4
14. Federated Learning With Energy Harvesting Devices An MDP Framework
   - File: `Federated Learning With Energy Harvesting Devices An MDP Framework.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 18; figures: 21; tables: 2
15. Federated Prompt-Based Decision Transformer for Resource Allocation of Customized VR Streaming in Mobile Edge Computing
   - File: `Federated Prompt-Based Decision Transformer for Resource Allocation of Customized VR Streaming in Mobile Edge Computing.pdf`
   - Tags: wireless federated learning, resource allocation, ris/irs, energy/privacy, semantic/foundation models
   - Pages: 15; figures: 32; tables: 17
16. Federated Reinforcement Learning for Uplink Centric Broadband Communication Optimization Over Unlicensed Spectrum
   - File: `Federated Reinforcement Learning for Uplink Centric Broadband Communication Optimization Over Unlicensed Spectrum.pdf`
   - Tags: wireless federated learning, resource allocation, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 14; figures: 36; tables: 4
17. Federated Split Learning via Low-Rank Approximation A Communication-Efficient Approach
   - File: `Federated Split Learning via Low-Rank Approximation A Communication-Efficient Approach.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, energy/privacy, semantic/foundation models
   - Pages: 17; figures: 21; tables: 3
18. Forwarding or Learning- A Flexible Low-Latency Low-Energy-Consumption Wireless Federated Learning Architecture With UE-to-Network Relay
   - File: `Forwarding or Learning- A Flexible Low-Latency Low-Energy-Consumption Wireless Federated Learning Architecture With UE-to-Network Relay.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 18; figures: 33; tables: 6
19. Idle-Mode Positioning in mmWave Cellular Networks Through Beam-Level Path Loss Measurements Without LOS Detection
   - File: `Idle-Mode Positioning in mmWave Cellular Networks Through Beam-Level Path Loss Measurements Without LOS Detection.pdf`
   - Tags: resource allocation, uav/satellite/vehicular
   - Pages: 17; figures: 30; tables: 36
20. Improving Wireless Federated Learning via Joint Downlink-Uplink Beamforming Over Analog Transmission
   - File: `Improving Wireless Federated Learning via Joint Downlink-Uplink Beamforming Over Analog Transmission.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo
   - Pages: 17; figures: 18; tables: 0
21. Integrated Sensing- Communication- and Computation for Over-the-Air Federated Edge Learning
   - File: `Integrated Sensing- Communication- and Computation for Over-the-Air Federated Edge Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 15; figures: 15; tables: 2
22. Integrated Sensing- Computation- and Communication Enabled Federated Edge Learning
   - File: `Integrated Sensing- Computation- and Communication Enabled Federated Edge Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy, uav/satellite/vehicular
   - Pages: 15; figures: 21; tables: 0
23. Joint Communication and Computation for Federated Learning Over Cell-Free MIMO Network
   - File: `Joint Communication and Computation for Federated Learning Over Cell-Free MIMO Network.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 15; figures: 30; tables: 2
24. Joint Communication Scheduling and Resource Allocation for Distributed Edge Learning Seamless Integration in Next-Generation Wireless Networks
   - File: `Joint Communication Scheduling and Resource Allocation for Distributed Edge Learning Seamless Integration in Next-Generation Wireless Networks.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 19; figures: 19; tables: 5
25. Joint Task Scheduling and Resource Allocation for Multi-Task Federated Learning Over Wireless Network
   - File: `Joint Task Scheduling and Resource Allocation for Multi-Task Federated Learning Over Wireless Network.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 16; figures: 22; tables: 1
26. Joint Topology and Beamforming Optimization for Decentralized Federated Learning
   - File: `Joint Topology and Beamforming Optimization for Decentralized Federated Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 17; figures: 39; tables: 1
27. Joint Client Scheduling and Quantization Optimization in Energy Harvesting-Enabled Federated Learning Networks
   - File: `Joint_Client_Scheduling_and_Quantization_Optimization_in_Energy_Harvesting-Enabled_Federated_Learning_Networks.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy
   - Pages: 17; figures: 16; tables: 15
28. LoLaFL Low-Latency Federated Learning via Forward-Only Propagation
   - File: `LoLaFL Low-Latency Federated Learning via Forward-Only Propagation.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy
   - Pages: 16; figures: 27; tables: 5
29. MAP-Optimal Hierarchical Quantization and Amplitude-Shift QAM for Reliable Digital Over-the-Air Computation
   - File: `MAP-Optimal Hierarchical Quantization and Amplitude-Shift QAM for Reliable Digital Over-the-Air Computation.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo
   - Pages: 16; figures: 27; tables: 9
30. Movable Antenna-Enhanced RIS-Assisted Over-the-Air Computation
   - File: `Movable Antenna-Enhanced RIS-Assisted Over-the-Air Computation.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 22; tables: 2
31. Multi-IRS Enhanced Wireless Coverage Deployment Optimization Based on Large-Scale Channel Knowledge
   - File: `Multi-IRS Enhanced Wireless Coverage Deployment Optimization Based on Large-Scale Channel Knowledge.pdf`
   - Tags: resource allocation, ris/irs, cell-free/mimo, uav/satellite/vehicular
   - Pages: 16; figures: 30; tables: 4
32. Optimization of Energy Efficiency for Federated Learning Over IRS-Assisted Cell-Free Massive MIMO Networks
   - File: `Optimization of Energy Efficiency for Federated Learning Over IRS-Assisted Cell-Free Massive MIMO Networks.pdf`
   - Tags: wireless federated learning, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 20; figures: 52; tables: 5
33. Over-the-Air Computation for Realizing Neural Link in In-Network AI Architectures
   - File: `Over-the-Air Computation for Realizing Neural Link in In-Network AI Architectures.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 31; tables: 0
34. Physical Layer Security for STAR-RIS-Assisted Federated Learning Systems With Differential Privacy
   - File: `Physical Layer Security for STAR-RIS-Assisted Federated Learning Systems With Differential Privacy.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 17; tables: 2
35. Power-Efficient Over-the-Air Aggregation With Receive Beamforming for Federated Learning
   - File: `Power-Efficient Over-the-Air Aggregation With Receive Beamforming for Federated Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 17; figures: 20; tables: 2
36. Prioritizing Gradient Sign Over Modulus An Importance-Aware Framework for Wireless Federated Learning
   - File: `Prioritizing Gradient Sign Over Modulus An Importance-Aware Framework for Wireless Federated Learning.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 17; figures: 22; tables: 0
37. PrivTuner With Homomorphic Encryption and LoRA A P3EFT Scheme for Privacy-Preserving Parameter-Efficient Fine-Tuning of AI Foundation Models
   - File: `PrivTuner With Homomorphic Encryption and LoRA A P3EFT Scheme for Privacy-Preserving Parameter-Efficient Fine-Tuning of AI Foundation Models.pdf`
   - Tags: wireless federated learning, resource allocation, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 17; figures: 24; tables: 19
38. Rethinking Federated Learning Over the Air The Blessing of Scaling Up
   - File: `Rethinking Federated Learning Over the Air The Blessing of Scaling Up.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy
   - Pages: 15; figures: 21; tables: 0
39. Rethinking Outage in Federated Learning An Adaptive Retransmission Design
   - File: `Rethinking Outage in Federated Learning An Adaptive Retransmission Design.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy
   - Pages: 16; figures: 14; tables: 2
40. RIS-Assisted AirComp FL Joint Data Allocation and Power Optimization for Reduced Distortion
   - File: `RIS-Assisted AirComp FL Joint Data Allocation and Power Optimization for Reduced Distortion.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 18; figures: 26; tables: 11
41. Robust Over-the-Air Federated Learning Under Imperfect CSI
   - File: `Robust Over-the-Air Federated Learning Under Imperfect CSI.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 16; figures: 32; tables: 6
42. Satellite Federated Fine-Tuning for Foundation Models in Space Computing Power Networks
   - File: `Satellite Federated Fine-Tuning for Foundation Models in Space Computing Power Networks.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 17; figures: 32; tables: 4
43. Semantic Communication-Enhanced U-Shaped Split Federated Learning With Adaptive Compression for Vehicular Networks
   - File: `Semantic Communication-Enhanced U-Shaped Split Federated Learning With Adaptive Compression for Vehicular Networks.pdf`
   - Tags: wireless federated learning, resource allocation, ris/irs, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 15; figures: 40; tables: 2
44. Semi-Distributed Reinforcement Learning for Internet of Robotic Things-Based Sustainable Data Collection
   - File: `Semi-Distributed Reinforcement Learning for Internet of Robotic Things-Based Sustainable Data Collection.pdf`
   - Tags: wireless federated learning, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 18; figures: 30; tables: 5
45. Task-Agnostic Semantic Communications Relying on Information Bottleneck and Federated Meta-Learning
   - File: `Task-Agnostic Semantic Communications Relying on Information Bottleneck and Federated Meta-Learning.pdf`
   - Tags: wireless federated learning, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 17; figures: 21; tables: 0
46. Toward Privacy-Preserving and Error-Tolerant Wireless Federated Learning Fixed-Point Model Aggregation With Differential Privacy Guarantees
   - File: `Toward Privacy-Preserving and Error-Tolerant Wireless Federated Learning Fixed-Point Model Aggregation With Differential Privacy Guarantees.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 17; figures: 33; tables: 8
47. UAV-Enabled Over-the-Air Federated Learning A Hierarchical Aggregation Approach
   - File: `UAV-Enabled Over-the-Air Federated Learning A Hierarchical Aggregation Approach.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular
   - Pages: 17; figures: 26; tables: 8
48. VecComp Vector Computing via MIMO Digital Over-the-Air Computation
   - File: `VecComp Vector Computing via MIMO Digital Over-the-Air Computation.pdf`
   - Tags: wireless federated learning, over-the-air computation, resource allocation, cell-free/mimo
   - Pages: 16; figures: 16; tables: 0
49. VEHFSL Hybrid Federated Split Learning for Resource-Constrained Vehicular Networks
   - File: `VEHFSL Hybrid Federated Split Learning for Resource-Constrained Vehicular Networks.pdf`
   - Tags: wireless federated learning, resource allocation, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 15; figures: 22; tables: 7
50. Zeroth-Order Federated Fine-Tuning for Large AI Models in Resource-Constrained Wireless Networks
   - File: `Zeroth-Order Federated Fine-Tuning for Large AI Models in Resource-Constrained Wireless Networks.pdf`
   - Tags: wireless federated learning, resource allocation, ris/irs, cell-free/mimo, energy/privacy, uav/satellite/vehicular, semantic/foundation models
   - Pages: 15; figures: 14; tables: 3
