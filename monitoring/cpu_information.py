import psutil


class CpuInformation:
    """Keep CPU information"""
    def __init__(self):
        self.cpu = {}

    def snapshot(self) -> None:
        """Save information about CPU percent and load average"""
        load_average = psutil.getloadavg()
        self.cpu = {
            'percent': psutil.cpu_percent(),
            'load_average_for_1_minute': load_average[0],
            'load_average_for_5_minutes': load_average[1],
            'load_average_for_10_minutes': load_average[2]
        }
