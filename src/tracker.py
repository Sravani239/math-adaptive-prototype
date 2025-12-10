# tracker.py
from dataclasses import dataclass, asdict
from typing import List
import time

@dataclass
class Attempt:
    question: str
    correct_answer: int
    user_answer: int
    correct: bool
    response_time: float
    difficulty: str

class Tracker:
    def __init__(self):
        self.attempts: List[Attempt] = []

    def log(self, question, correct_answer, user_answer, correct, response_time, difficulty):
        a = Attempt(question, correct_answer, user_answer, correct, response_time, difficulty)
        self.attempts.append(a)

    def summary(self):
        total = len(self.attempts)
        if total == 0:
            return {"total": 0, "accuracy": 0.0, "avg_time": 0.0}
        correct = sum(1 for a in self.attempts if a.correct)
        avg_time = sum(a.response_time for a in self.attempts) / total
        return {
            "total": total,
            "accuracy": correct / total,
            "avg_time": avg_time
        }

    def difficulty_transitions(self):
        return [(a.difficulty, a.correct, round(a.response_time, 2)) for a in self.attempts]
