# Speed Limiter — UT-LIM-01
Goal: peak speed ≤ 0.30 m/s at full throttle.

How to run
1) Use 1 m strip; logger on.
2) Run `limiter_demo` (full throttle ~5 s).
3) Logs → `logs/speed.csv` (same columns).

Pass/Fail
- Peak `v_est` ≤ 0.30 m/s across 3 trials.
