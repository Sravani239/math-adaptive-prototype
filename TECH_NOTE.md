Math Adventures — Technical Note

Architecture / Flow:
1. User starts session → selects initial difficulty.
2. Puzzle generator produces a problem for current difficulty.
3. User answers; tracker logs correctness and response time.
4. Adaptive engine updates an internal skill score (0–1).
5. Skill mapped to next difficulty via thresholds.
6. Repeat; end-of-session summary produced.

Adaptive logic:
- Skill update: skill <- alpha*skill + (1-alpha)*reward
- Reward = correctness * time_factor
- time_factor = max(0.2, 1 - (response_time / target_time))
- target_time varies by difficulty (tuned values).
- Thresholds: skill < 0.4 -> Easy; 0.4–0.7 -> Medium; >0.7 -> Hard.

Key metrics tracked:
- Correctness (binary)
- Response time (seconds)
- Per-question difficulty (for transition logs)
These determine reward and thus the skill update.

Why this approach:
- Explainable and stable for demo/viva.
- EMA smooths noisy answers and gives recent performance more weight.
- Time-aware reward captures both accuracy and fluency.

Extensions (discussion points):
- Collect real data by logging sessions (consent + anonymization).
- Use logged features to train a logistic regression / decision tree to predict success probability and map to difficulty (supervised).
- Handle noisy performance via robust stats (median, outlier filters) or confidence intervals on skill estimate.
- Scale to other topics by plugging other puzzle generators and re-tuning target times and thresholds.
