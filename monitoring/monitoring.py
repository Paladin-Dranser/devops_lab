import time

import monitoring.settings.settings as settings
from monitoring.snapshot import Snapshot


def run() -> None:
    """Create a snapshot every n minutes"""
    snapshot = Snapshot()
    sleep_time = int(settings.get_interval() * 60)

    while True:
        snapshot.snapshot()
        snapshot.write_snapshot()

        try:
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            print('Stop doing snapshots.\nExit program.')
            exit(0)


def set_interval(interval: int) -> None:
    """Set interval to create a snapshot"""
    settings.set_interval(interval)


def set_file_name(file_name: str) -> None:
    """Set file name"""
    settings.set_file_name(file_name)


def set_file_type(file_type: str) -> None:
    """Set file type"""
    settings.set_file_type(file_type)
