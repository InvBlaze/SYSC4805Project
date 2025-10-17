# Motor Control — UT-MOT-01
Goal: 0.10/0.20/0.30 m/s within ±5%.

How to run
1) 1 m timing strip (two tape marks).
2) Run `motor_demo` for ~3–5 s per speed.
3) Logs → `logs/speed.csv` with `ts_ms,v_cmd,v_est`.

Pass/Fail
- Each commanded speed within ±5% of measured.
