import psutil


class IoInformation:
    """Keep input/output information"""
    def __init__(self):
        self.io_disk = {}

    def snapshot(self) -> None:
        """Save input/output information"""
        io = psutil.disk_io_counters()
        self.io_disk = {
            'read_time': io[4],
            'write_time': io[5],
            'busy_time': io[8]
        }
