__title__       = 'taste_the_rainbow.py'
__doc__         = 'Makes text decoration.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo (https://github.com/DaddyChucky/HWID).'


###
#   --> GET INFO <--
###


### !== IMPORTS ###
from taste_the_rainbow import *
import psutil
import hashlib
import numpy as np
### IMPORTS ==! ###


### !== COMMON ###
def initiate_hash() -> hashlib._Hash:
    '''
    Initiates hashing algorithm (MD5 chosen).
        Returns:
            hasher (hashlib._Hash): The Hasher used for further digestion
    '''
    return hashlib.md5()

def digest(hasher, barray: bytearray) -> str:
    '''
    Digests a bytearray to a MD5 hash.
        Parameters:
            hasher (hashlib._Hash): The Hasher used to digest
            barray (bytearray):     The bytearray to digest
        Returns:
                digested_bytearray (str): The digested bytearray
    '''
    hasher.update(bytearray(barray))
    return hasher.digest()

HASHER = initiate_hash()
### COMMON ==! ###


### !== CPU ###
def get_physical_cpu_count() -> str:
    '''
    Gets physical CPU count.
    Returns:
        physical_cpu_count (str): Number of physical CPUs
    '''
    return str(psutil.cpu_count(False) if psutil.cpu_count(False) else "")

def get_physical_cpu_max_freq() -> str:
    '''
    Gets physical CPU max frequency.
    Returns:
        physical_cpu_max_freq (str): Physical CPU max frequency
    '''
    return str(psutil.cpu_freq(False).max if psutil.cpu_freq(False).max else "")
### CPU ==! ###


### !== MEMORY ###
def get_memory_size() -> str:
    '''
    Gets physical memory size (in total, used & unused).
    Returns:
        memory_size (str): Physical memory size
    '''
    return str(psutil.virtual_memory().total if psutil.virtual_memory().total else "")
### MEMORY ==! ###


### !== DISKS ###
def get_disks() -> str:
    '''
    Gets physical memory disks (devices, mountpoints & types).
    Returns:
        disks_info (str): Concatenation of devices, mountpoints & fstypes related to memory disks
    '''
    devices:        set[str] = set()
    mountpoints:    set[str] = set()
    fstypes:        set[str] = set()
    for disk in psutil.disk_partitions(False):
        devices.add(disk.device if disk.device else "")
        mountpoints.add(disk.mountpoint if disk.mountpoint else "")
        fstypes.add(disk.fstype if disk.fstype else "")
    return "".join(sorted(devices) + sorted(mountpoints) + sorted(fstypes))
### DISKS ==! ###


### !== NET ###
def get_net_connections() -> str:
    '''
    Gets various informations about net connections (fds, families, types, ips & ports).
    WARNING: For HWID purposes, net connections are variable, and thus should not be used for a static verification.
    Returns:
        net_info (str): Concatenation of fds, families, types, ips & ports related to net connections
    '''
    fds:        dict = dict()
    families:   dict = dict()
    types:      dict = dict()
    ips:        dict = dict()
    ports:      dict = dict()
    retries:    int  = 10
    for _ in range(retries):
        for net in psutil.net_connections():
            if net.fd: 
                try:                fds[str(net.fd)] += 1
                except KeyError:    fds[str(net.fd)] =  0
            if net.family:
                try:                families[str(net.family)] += 1
                except KeyError:    families[str(net.family)] =  0
            if net.type:
                try:                types[str(net.type)] += 1
                except KeyError:    types[str(net.type)] =  0
            if net.laddr.port:
                try:                ports[str(net.laddr.port)] += 1
                except KeyError:    ports[str(net.laddr.port)] =  0
            if net.laddr.ip:
                try:                ips[str(net.laddr.ip)] += 1
                except KeyError:    ips[str(net.laddr.ip)] =  0
    m_fds:      float = np.median(np.array(list(fds.values())))
    m_families: float = np.median(np.array(list(families.values())))
    m_types:    float = np.median(np.array(list(types.values())))
    m_ips:      float = np.median(np.array(list(ips.values()))) 
    m_ports:    float = np.median(np.array(list(ports.values()))) 
    return "".join(
        sorted([fd[0]        for fd     in fds.items()      if float(fd[1])     >= float(m_fds)])        +   \
        sorted([family[0]    for family in families.items() if float(family[1]) >= float(m_families)])   +   \
        sorted([_type[0]     for _type  in types.items()    if float(_type[1])  >= float(m_types)])      +   \
        sorted([ip[0]        for ip     in ips.items()      if float(ip[1])     >= float(m_ips)])        +   \
        sorted([port[0]      for port   in ports.items()    if float(port[1])   >= float(m_ports)])
    )
### NET ==! ###


### !== USERS ###
def get_users() -> str:
    '''
    Gets OS' users info (names & hosts).
    Returns:
        user_info (str): Concatenation of names & hosts related to OS' users
    '''
    names: set[str] = set()
    hosts: set[str] = set()
    for user in psutil.users():
        names.add(user.name if user.name else "")
        hosts.add(user.host if user.host else "")
    return "".join(sorted(names) + sorted(hosts))
### USERS ==! ###


### !== HWID ###
def get_hwid(include_net_connections: bool = False) -> str:
    '''
    Gets OS' users info (names & hosts).
    Parameter:
        include_net_connections (bool, False by default): Since net connections are variable, net connections could be instanced for dynamic HWID
    Returns:
        hwid (str): Digested HWID (static or dynamic depending on include_net_connections)
    '''
    hwid: str = ""
    try: hwid += get_physical_cpu_count()
    except Exception: pass
    try: hwid += get_physical_cpu_max_freq()
    except Exception: pass
    try: hwid += get_memory_size()
    except Exception: pass
    try: hwid += get_disks()
    except Exception: pass
    if include_net_connections:
        try: hwid += get_net_connections()
        except Exception: pass
    try: hwid += get_users()
    except Exception: pass
    return str(digest(HASHER, bytearray(hwid, encoding="utf8")))
### HWID ==! ###


### !== MAIN ###
if __name__ == "__main__":
    print_success("STATIC HWID", get_hwid())
    print_warning("DYNAMIC HWID", get_hwid(True))
### MAIN ==! ###
