# IMU Handler — UT-IMU-01
Goal: yaw ≤ ±3°, pitch/roll ≤ ±2° (static).

How to run
1) Level surface; mark 0°,90°,180°,270° on floor.
2) Record ~5 s at each; then tilt +10° and −10° once.
3) Logs → `logs/imu_demo.csv` with `ts_ms,yaw_deg,pitch_deg,roll_deg`.

Pass/Fail
- Mean yaw error ≤ 3° each cardinal; pitch/roll ≤ 2°.
