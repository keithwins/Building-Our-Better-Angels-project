# BOBA Probe-Set MVE Specification

## 1. Purpose
The BOBA probe-set MVE serves as an orthogonal alignment/model-selection instrument, ensuring model behavior aligns with human values without conflicting with other alignment mechanisms. It provides a structured framework for evaluating and selecting models based on their ability to handle complex, morally ambiguous scenarios.

## 2. Reference-Text Categories (12)
1. Mirror-Not-Cheer: Models must avoid uncritical agreement with human preferences, instead reflecting on potential biases.
2. Open-Frames-Not-Closure: Encourage open-ended reasoning rather than premature conclusions.
3. Reasoning-From-Premises: Prioritize logical deduction from given premises over heuristics.
4. Resisting-Sycophancy: Avoid excessive flattery of human inputs; maintain critical evaluation.
5. Uncertainty-Under-Fog: Gracefully handle ambiguous or incomplete information.
6. User-as-Orchestrator: Respect user intent while maintaining model autonomy.
7. Local-Sovereignty: Prioritize context-specific decisions over global heuristics.
8. Sustainable-Future-Orientation: Consider long-term consequences of decisions.
9. Critical-Thinking-Under-Pressure: Maintain analytical rigor in high-stakes scenarios.
10. Ethical-Dilemma-Navigation: Handle morally complex situations with balanced judgment.
11. Adaptability-to-New-Contexts: Adjust reasoning patterns to novel situations.
12. Transparency-in-Reasoning: Clearly articulate decision-making processes.

## 3. Candidate Models
- Ollama: llama2, phi3, codellama
- Python Libraries: transformers (bert, roberta, distilbert), langchain, llamafactory

## 4. Output Artifacts
- Final spec document
- List of 12 reference texts
- Model configuration files
- Success/failure criteria checklist

## 5. Success/Failure Criteria
Success: All 12 categories are addressed, models are appropriately selected, and artifacts are complete.
Failure: Missing categories, incorrect model choices, or incomplete artifacts.

## 6. Next Executable Card
Proposed command: `test_mve.py --reference-texts reference_texts.txt --models llama2 phi3`