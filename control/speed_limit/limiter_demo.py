import time
from tests.logger.logger import CsvLogger

MAX_V = 0.30  # m/s
log = CsvLogger("logs/speed.csv", ["ts_ms","v_cmd","v_est"])

def motor_full_throttle_to(v_cmd):
    # TODO: apply v_cmd to controller
    pass

def estimate_speed():
    # TODO: read encoder/odometry
    return min(v_cmd, MAX_V)  # pretend limiter OK

v_cmd = 1.0  # pretend full throttle command
v_cmd = min(v_cmd, MAX_V)  # limiting
t0 = time.time()
while time.time() - t0 < 5.0:
    motor_full_throttle_to(v_cmd)
    v_est = estimate_speed()
    log.write(log.ts(), v_cmd, round(v_est,3))
    time.sleep(0.1)
log.close()
print("saved logs/speed.csv (limiter)")
