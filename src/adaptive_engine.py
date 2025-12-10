# adaptive_engine.py
from typing import Literal

Difficulty = Literal['Easy', 'Medium', 'Hard']

class AdaptiveEngine:
    """
    Maintains a skill score in [0,1]. Updates after each attempt using:
      skill <- alpha * skill + (1-alpha) * reward
    Reward = correctness * time_factor
    time_factor = max(0.2, 1 - (response_time / target_time))
    target_time depends on difficulty.
    Mapping from skill -> difficulty via thresholds.
    """
    def __init__(self, initial_level: Difficulty = 'Easy'):
        self.skill = {'Easy': 0.2, 'Medium': 0.5, 'Hard': 0.8}[initial_level]
        self.alpha = 0.7  # memory of past skill
        self.target_times = {'Easy': 6.0, 'Medium': 8.0, 'Hard': 12.0}

    def update(self, difficulty: Difficulty, correct: bool, response_time: float):
        target = self.target_times[difficulty]
        time_factor = max(0.2, 1 - (response_time / target))  # faster -> higher factor
        reward = (1.0 if correct else 0.0) * time_factor
        self.skill = self.alpha * self.skill + (1 - self.alpha) * reward
        self.skill = min(max(self.skill, 0.0), 1.0)

    def next_difficulty(self) -> Difficulty:
        if self.skill < 0.4:
            return 'Easy'
        elif self.skill < 0.7:
            return 'Medium'
        else:
            return 'Hard'
