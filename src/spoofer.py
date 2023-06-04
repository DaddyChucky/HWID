###
#   --> IMPORTS <--
###

import taste_the_rainbow
import get_info
import hashlib


###
#   --> DOCS <--
###
__title__       = 'spoofer.py'
__doc__         = 'Spoofs hardware.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo (https://github.com/DaddyChucky/HWID).'


###
#   --> SPOOFER <--
###

class Spoofer:
    def __init__(self):
        _HASHER:            hashlib._Hash   = self.get_hasher()
        _CPU_COUNT:         str             = self.get_physical_cpu_count()
        _CPU_MAX_FREQ:      str             = self.get_physical_cpu_max_freq()
        _MEMORY_SIZE:       str             = self.get_memory_size()
        _DISKS:             str             = self.get_disks()
        _NET_CONNECTIONS:   str             = self.get_net_connections()
        _USERS:             str             = self.get_users()
        _HWID_STATIC:       str             = self.get_hwid(False)
        _HWID_DYNAMIC:      str             = self.get_hwid(True)

    def get_hasher(self) -> hashlib._Hash:
        return get_info.initiate_hash()
    
    def digest(self, barray: bytearray) -> str:
        return get_info.digest(self._HASHER, barray)
    
    def get_physical_cpu_count(self) -> str:
        return get_info.get_physical_cpu_count()

    def get_physical_cpu_max_freq(self) -> str:
        return get_info.get_physical_cpu_max_freq()

    def get_memory_size(self) -> str:
        return get_info.get_memory_size()

    def get_disks(self) -> str:
        return get_info.get_disks()

    def get_net_connections(self) -> str:
        return get_info.get_net_connections()

    def get_users(self) -> str:
        return get_info.get_users()

    def get_hwid(self, include_net_connections: bool = False) -> str:
        return get_info.get_hwid(include_net_connections)


if __name__ == '__main__':
    spoofer: Spoofer = Spoofer()
