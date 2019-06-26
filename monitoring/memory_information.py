import psutil


class MemoryInformation:
    """Keep memory information (physical and virtual)"""
    def __init__(self):
        self.physical_memory = {}
        self.virtual_memory = {}
        self.swap_memory = {}

    def snapshot(self) -> None:
        """Save memory information"""
        self.__snapshot_physical_memory()
        self.__snapshot_virtual_memory()
        self.__snapshot_swap_memory()

    def __snapshot_physical_memory(self) -> None:
        """Save physical memory information"""
        disk_partitions = []
        for partition in list(psutil.disk_partitions()):
            disk_partitions.append(partition[1])

        for partition in disk_partitions:
            memory = psutil.disk_usage(partition)
            self.physical_memory[partition] = {
                'total': f'{memory[0] / (1024.0 ** 2):.2f} Mb',
                'used': f'{memory[1] / (1024.0 ** 2):.2f} Mb',
                'free': f'{memory[2] / (1024.0 ** 2):.2f} Mb'
            }

    def __snapshot_virtual_memory(self) -> None:
        """Save virtual memory information"""
        memory = psutil.virtual_memory()

        self.virtual_memory = {
            'total': f'{memory[0] / (1024 ** 2):.2f} Mb',
            'used': f'{memory[3] / (1024 ** 2):.2f} Mb',
            'free': f'{memory[4] / (1024 ** 2):.2f} Mb'
        }

    def __snapshot_swap_memory(self) -> None:
        """Save swap memory information"""
        memory = psutil.swap_memory()

        self.swap_memory = {
            'total': f'{memory[0] / (1024.0 ** 2):.2f} Mb',
            'used': f'{memory[1] / (1024.0 ** 2):.2f} Mb',
            'free': f'{memory[2] / (1024.0 ** 2):.2f} Mb'
        }
