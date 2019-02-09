#!/usr/bin/env python
import psutil
import platform
import cpuinfo


def convertBytestoReadable(n):
    symbols = (' Kb',' Mb',' Gb',' Tb',' Pb',' Eb',' Zb',' Yb')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def Start():
    cpufamily = platform.processor()
    cpugeneral = cpuinfo.get_cpu_info()
    cpuname = cpugeneral['brand']
    cpuarch = cpugeneral['arch']
    cpubits = cpugeneral['bits']
    cpuraw_arch_string = cpugeneral['raw_arch_string']
    cpuhz_advertised = cpugeneral['hz_advertised']
    cpuhz_actual = cpugeneral['hz_actual']
    cpul2_cache_size = cpugeneral['l2_cache_size']
    print("\n")
    print("--CPU--")
    print("Cpu Family =", cpufamily)
    print("Cpu Name =", cpuname)
    print("Core Count =", psutil.cpu_count())
    print("Arch =", cpuarch)
    print("Bits =", cpubits)
    print("Arch String =", cpuraw_arch_string)
    print("Known Hz =", cpuhz_advertised)
    print("Actual Hz =", cpuhz_actual)
    print("Cache Size =", cpul2_cache_size)
    cpu = psutil.cpu_percent(interval=1)
    print("Percentage =",str(cpu) + "%")
    psutil.virtual_memory()
    ram = psutil.virtual_memory()
    print("--RAM--")
    print("Total =",ram.total >> 20,"mb")
    print("Available =",ram.available >> 20,"mb")
    print("Percentage =", str(ram.percent) + "%")
    print("Used =",ram.used >> 20,"mb")
    print("Free =",ram.free >> 20,"mb")
    print("--DISK--")
    print("MOUNTED")
    disk = psutil.disk_partitions(all=False)
    for item in disk:
        if item.fstype == "" or item.fstype is None:
            continue
        else:
            print("----")
            print("Device =", item.device)
            print("Mount Point =", item.mountpoint)
            print("fstype =", item.fstype)
            print("opts =", item.opts)
            print("Usage;",)
            usagelist = psutil.disk_usage(item.device)
            print("Total =", convertBytestoReadable(usagelist.total))
            print("Used =", convertBytestoReadable(usagelist.used))
            print("Free =", convertBytestoReadable(usagelist.free))
            print("Percent =", str(usagelist.percent) + "%")
    print("----")
    print("UNMOUNTED")
    for item in disk:
        if item.fstype == "" or item.fstype is None:
            print(item.device)


if __name__ == '__main__':
    Start()

    
