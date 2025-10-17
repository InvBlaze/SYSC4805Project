# IR/Ultrasonic Handler — UT-OBS-01
Goal: mean error ≤ ±2 cm at 5/10/20/30 cm (5 reps each).

How to run
1) Tape ruler on floor; place a box at the marks.
2) Run `range_demo`; 5 readings per distance (0.5 s apart).
3) Logs → `logs/ranging.csv` with `ts_ms,true_cm,meas_cm`.

Pass/Fail
- All means within ±2 cm; 0 missed detections.
