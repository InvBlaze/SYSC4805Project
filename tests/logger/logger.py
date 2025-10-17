import csv, time, os

class CsvLogger:
    def __init__(self, path, header):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.f = open(path, "a", newline="")
        self.w = csv.writer(self.f)
        if self.f.tell() == 0:
            self.w.writerow(header)
        self.t0 = int(time.time() * 1000)

    def ts(self):
        return int(time.time() * 1000) - self.t0

    def write(self, *row):
        self.w.writerow(row); self.f.flush()

    def close(self):
        self.f.close()
