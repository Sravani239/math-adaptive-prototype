Math Adventures — AI-Powered Adaptive Learning Prototype

Run:
$ python src/main.py

Structure:
src/
  puzzle_generator.py
  tracker.py
  adaptive_engine.py
  main.py

Design:
- Puzzle generator: difficulty-based ranges and operations.
- Tracker: logs correctness & response time.
- Adaptive engine: skill estimator (EMA) that maps to next difficulty by thresholds.

This prototype focuses on adaptive logic (explainable & tunable).
