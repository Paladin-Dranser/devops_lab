import json
import datetime

import monitoring.settings.settings as settings
import monitoring.cpu_information
import monitoring.memory_information
import monitoring.io_information
import monitoring.network_information

from pathlib import Path


class Snapshot:
    """"Manage snapshots"""
    def __init__(self):
        self.cpu = monitoring.cpu_information.CpuInformation()
        self.memory = monitoring.memory_information.MemoryInformation()
        self.io_disk = monitoring.io_information.IoInformation()
        self.network = monitoring.network_information.NetworkInformation()

    def snapshot(self) -> None:
        """Do a snapshot"""
        self.cpu.snapshot()
        self.memory.snapshot()
        self.io_disk.snapshot()
        self.network.snapshot()

    def write_snapshot(self) -> None:
        """Write snapshot information to json file"""
        if settings.get_file_type() == 'json':
            self.__write_json_snapshot()
        else:
            self.__write_plain_snapshot()

    def __write_json_snapshot(self) -> None:
        """Write snapshot information to json file"""
        file = Path(settings.get_file_name() + '.' + settings.get_file_type())
        if file.exists():
            with open(file) as json_file:
                try:
                    data = json.load(json_file)
                except json.decoder.JSONDecodeError:
                    file.unlink()
                    data = {}
        else:
            data = {}

        snapshot_number = f'Snapshot {len(data.keys()) + 1}'

        data[snapshot_number] = {
            'timestamp': datetime.datetime.now().ctime(),
            'cpu': self.cpu.cpu,
            'physical memory': self.memory.physical_memory,
            'virtual_memory': self.memory.virtual_memory,
            'swap_memory': self.memory.swap_memory,
            'input-output_disk': self.io_disk.io_disk,
            'interfaces': self.network.interfaces
        }

        with open(file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def __write_plain_snapshot(self):
        """Write snapshot information to json file"""
        file = Path(settings.get_file_name() + '.' + settings.get_file_type())
        if file.exists():
            with open(file) as plain_file:
                data = plain_file.readlines()
        else:
            data = []

        data.append(
            f'Snapshot {len(data) // 8 + 1}:\n'
            f'timestamp {datetime.datetime.now().ctime()};\n'
            f'cpu: {str(self.cpu.cpu)};\n'
            f'physical_memory: {str(self.memory.physical_memory)};\n'
            f'virtual_memory: {str(self.memory.virtual_memory)};\n'
            f'swap_memory: {str(self.memory.swap_memory)};\n'
            f'input/output_disk: {str(self.io_disk.io_disk)};\n'
            f'interfaces: {str(self.network.interfaces)};\n'
        )

        with open(file, 'w') as plain_file:
            for line in data:
                plain_file.write('%s' % line)
