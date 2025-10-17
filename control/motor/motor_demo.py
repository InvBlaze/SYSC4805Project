import time
from tests.logger.logger import CsvLogger

log = CsvLogger("logs/speed.csv", ["ts_ms","v_cmd","v_est"])

def set_speed(v_cmd):
    # TODO: send to motor controller
    pass

def estimate_speed():
    # TODO: read encoder/odometry; return m/s
    return v_cmd*0.95  # pretend 5% slip

for v_cmd in [0.10, 0.20, 0.30]:
    set_speed(v_cmd)
    t0 = time.time()
    while time.time() - t0 < 3.0:
        v_est = estimate_speed()
        log.write(log.ts(), v_cmd, round(v_est,3))
        time.sleep(0.1)
set_speed(0.0)
log.close()
print("saved logs/speed.csv")
