import time, random
from tests.logger.logger import CsvLogger

log = CsvLogger("logs/ranging.csv", ["ts_ms","true_cm","meas_cm"])
distances = [5,10,20,30]  # set by your ruler placement

def read_range():
    # TODO: replace with actual range sensor read
    return current + random.uniform(-1.0, 1.0)

for current in distances:
    for _ in range(5):
        meas = read_range()
        log.write(log.ts(), current, round(meas,2))
        time.sleep(0.5)
log.close()
print("saved logs/ranging.csv")
