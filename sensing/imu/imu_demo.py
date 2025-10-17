import math, time
from tests.logger.logger import CsvLogger

log = CsvLogger("logs/imu_demo.csv", ["ts_ms","yaw_deg","pitch_deg","roll_deg"])

def read_imu():
    # TODO: replace with actual IMU read
    t = time.time()
    yaw = (t*20)%360; pitch = 0.5*math.sin(t); roll = 0.5*math.cos(t)
    return yaw, pitch, roll

for _ in range(100):
    yaw,p,r = read_imu()
    log.write(log.ts(), round(yaw,2), round(p,2), round(r,2))
    time.sleep(0.1)
log.close()
print("saved logs/imu_demo.csv")
