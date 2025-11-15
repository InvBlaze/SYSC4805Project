# Unit Tests 
This stage-based unit-test summary includes all the components test for current project process
## UT-MOT-01 — Motor Control
Verifies wheel directions and checks run speed on a 1 m lane. **Pass** if directions match and measured speed is within **±3%** of target.

## UT-LIM-01 — Speed Limiter
Confirms the governor caps top speed at **≤ 0.30 m/s (30 cm/s)** during an ~8 s run (with tach or calibrated estimate). **Pass** if the limit isn’t exceeded.

## UT-IMU-01 — IMU Accuracy
Checks IMU presence, tilt at rest (**≤ 2°**), and yaw at **0°/90°/180°/270°** within **±2.5°**. **Pass** if all criteria are met.

## UT-LINE-01 — Line Sensor Detection
Validates white/black reflectance separation (**> 120 ADC counts** per channel) and counts **20** tape crossings reliably. **Pass** if separation and crossings are achieved.

## UT-OBS-01 — Obstacle Detection
Measures ultrasonic medians at **5/10/20/30 cm** and reports class (**CLEAR / CUBE / TALL**). **Pass** if average absolute error is **≤ ±1.5 cm** with no misses.

## UT-LOG-01 — Logging System
Ensures key events are recorded with timestamps in the correct order. **Pass** if all expected events appear and ordering is correct.

