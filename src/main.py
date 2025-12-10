# main.py
import time
from puzzle_generator import generate_puzzle
from tracker import Tracker
from adaptive_engine import AdaptiveEngine

def choose_initial():
    while True:
        v = input("Choose initial difficulty (Easy/Medium/Hard): ").strip().capitalize()
        if v in ('Easy', 'Medium', 'Hard'):
            return v
        print("Invalid. Try Easy, Medium or Hard.")

def ask_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a number (integer).")

def session_loop(name, initial_level, num_questions=10):
    tracker = Tracker()
    engine = AdaptiveEngine(initial_level)
    current = initial_level

    print(f"\nHi {name}! Starting with {current} problems. Let's go!\n")

    for i in range(num_questions):
        q, ans = generate_puzzle(current)
        print(f"Q{i+1}. ({current}) {q}")
        t0 = time.perf_counter()
        user = ask_int("Your answer: ")
        t1 = time.perf_counter()
        rt = t1 - t0
        correct = (user == ans)
        tracker.log(q, ans, user, correct, rt, current)
        engine.update(current, correct, rt)
        next_level = engine.next_difficulty()
        print("Correct!" if correct else f"Oops — correct answer: {ans}")
        print(f"Response time: {rt:.2f}s | Skill: {engine.skill:.2f} | Next level: {next_level}\n")
        current = next_level

    return tracker, engine

def pretty_summary(tracker, engine):
    s = tracker.summary()
    print("=== Session Summary ===")
    print(f"Total questions: {s['total']}")
    print(f"Accuracy: {s['accuracy']*100:.1f}%")
    print(f"Average response time: {s['avg_time']:.2f}s")
    print(f"Final estimated skill: {engine.skill:.2f} -> Recommended level: {engine.next_difficulty()}")
    print("\nDifficulty transitions (difficulty, correct, time):")
    for t in tracker.difficulty_transitions():
        print(t)

if __name__ == "__main__":
    name = input("Enter learner name: ").strip() or "Student"
    init = choose_initial()
    n = input("How many problems? [default 10]: ").strip()
    try:
        n_q = int(n) if n else 10
    except:
        n_q = 10
    tracker, engine = session_loop(name, init, n_q)
    pretty_summary(tracker, engine)
