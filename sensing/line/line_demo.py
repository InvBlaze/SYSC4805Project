import time
from tests.logger.logger import CsvLogger

log = CsvLogger("logs/line_demo.csv", ["ts_ms","event","tape_detect","note"])

def read_line_sensor():
    # TODO: replace with actual read; return 1 on tape, 0 otherwise
    return 1 if (int(time.time()*10) % 10 == 0) else 0

for i in range(50):  # ~5–10 s sample
    hit = read_line_sensor()
    log.write(log.ts(), "sample", hit, "")
    time.sleep(0.1)
log.close()
print("saved logs/line_demo.csv")
