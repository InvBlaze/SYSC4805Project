# Line Sensor Handler — UT-LINE-01
Goal: detect black painter’s tape reliably (no boundary crossing).

How to run (demo)
1) Place robot 20–30 cm from tape at 0°,15°,30°,45°.
2) Run `line_demo` and drive slowly toward the tape; cross and back away (5× each angle).
3) Logs → `logs/line_demo.csv` with `ts_ms,event,tape_detect,note`.

Pass/Fail
- 20/20 detections, 0 misses; prompt detection (<~200 ms).
