from tests.logger.logger import CsvLogger
log = CsvLogger("logs/line_demo.csv", ["ts_ms","event","tape_detect","note"])
log.write(log.ts(), "approach", 0, "start")
log.write(log.ts(), "tape_hit", 1, "")
log.close()
print("Wrote logs/line_demo.csv")
