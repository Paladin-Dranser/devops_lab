import psutil


class NetworkInformation:
    """Keep information about interfaces and ip addresses"""
    def __init__(self):
        self.interfaces = {}

    def snapshot(self) -> None:
        """"Save information about interfaces and ip address and masks"""
        interfaces = list(psutil.net_if_addrs().keys())
        for interface in interfaces:
            interface_counter = list(
                psutil.net_io_counters(pernic=True)[interface]
            )
            self.interfaces[interface] = {
                'packets_sent': interface_counter[2],
                'packets_recv': interface_counter[3],
                'error_in': interface_counter[4],
                'error_out': interface_counter[5]
            }
