# SYSC 4805 — Team Ghost White (Autonomous Snowplow)

**Constraints:** size ≤ 226×262×150 mm · speed ≤ 0.30 m/s · run ≤ 5:00 · start from a corner  
**Arena:** black painter’s tape boundary · wooden cube “snow” · boxes as obstacles

## What lives here
- `sensing/` — line, IMU, and IR/ultrasonic handlers (stand-alone demos + logs)
- `control/` — motor bring-up and speed limiter (≤ 0.30 m/s)
- `plow/` — plow prototype + final build notes
- `tests/` — small demo apps and logging utility
- `report/` — images, evidence, and write-ups
- `logs/` — CSV logs (not versioned in GitHub if you prefer; see .gitignore)

## Quick start
- Run the 5 unit demos (UT-LINE-01, UT-IMU-01, UT-OBS-01, UT-MOT-01, UT-LIM-01).
- Save CSV logs in `/logs` and short videos in `/report/img`.
- Tag milestones: `L6_handlers_start`, `L7_handlers_done`, `L9_int1-2`, `L10_int3-4`, `L11_demo`.
