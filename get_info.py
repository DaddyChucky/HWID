import psutil
import hashlib
import numpy as np


def initiate_hash():
    return hashlib.md5()


def digest(hasher, barray: bytearray) -> str:
    hasher.update(bytearray(barray))
    return hasher.digest()


HASHER = initiate_hash()


# CPU
def get_physical_cpu_count() -> str:
    return str(psutil.cpu_count(False) if psutil.cpu_count(False) else "")

def get_physical_cpu_max_freq() -> str:
    return str(psutil.cpu_freq(False).max if psutil.cpu_freq(False).max else "")


# MEMORY
def get_memory_size() -> str:
    return str(psutil.virtual_memory().total if psutil.virtual_memory().total else "")


# DISKS
def get_disks() -> str:
    devices:        set[str] = set()
    mountpoints:    set[str] = set()
    fstypes:        set[str] = set()
    for disk in psutil.disk_partitions(False):
        devices.add(disk.device if disk.device else "")
        mountpoints.add(disk.mountpoint if disk.mountpoint else "")
        fstypes.add(disk.fstype if disk.fstype else "")
    return "".join(sorted(devices) + sorted(mountpoints) + sorted(fstypes))


# NET
def get_net_connections():
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


# USER
def get_users() -> str:
    names: set[str] = set()
    hosts: set[str] = set()
    for user in psutil.users():
        names.add(user.name if user.name else "")
        hosts.add(user.host if user.host else "")
    return "".join(sorted(names) + sorted(hosts))


# HWID
def get_hwid() -> str:
    hwid: str = ""
    try: hwid += get_physical_cpu_count()
    except Exception: pass
    try: hwid += get_physical_cpu_max_freq()
    except Exception: pass
    try: hwid += get_memory_size()
    except Exception: pass
    try: hwid += get_disks()
    except Exception: pass
    # try: hwid += get_net_connections() // too variable
    # except Exception: pass
    try: hwid += get_users()
    except Exception: pass
    return str(digest(HASHER, bytearray(hwid, encoding="utf8")))

print(get_hwid())
