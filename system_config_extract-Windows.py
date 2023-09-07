import platform
import os
import psutil
import socket
import subprocess


# converts bytes to gigabytes
def bytes_to_gb(bytes):
    return round(bytes / 1024 ** 3, 2)


def get_system_info():
    # Get basic system, network and user information
    SSID_devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    SSID_devices = SSID_devices.decode('ascii')
    SSID_devices = SSID_devices.replace("\r", "")
    system_info = {
        "OS": platform.system(),
        "OS version": platform.version(),
        "OS Release": platform.release(),
        "Machine Processor": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "ip-address": socket.gethostbyname(socket.gethostname()),
        "username": os.getlogin(),
        "user profile": os.environ.get("USERPROFILE"),
        "Open network connections": psutil.net_connections(),
        "Network interface card names": psutil.net_if_addrs(),
        "Previously Connected to WiFi SSIDs": SSID_devices
    }

    # get basic memory information
    memory_info = {
        "Total Memory (GB)": bytes_to_gb(psutil.virtual_memory().total),
        "Available Memory (GB)": bytes_to_gb(psutil.virtual_memory().available),
        "Used Memory (GB)": bytes_to_gb(psutil.virtual_memory().used),
    }

    # get basic disk information
    disk_info = []
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Device": partition.device,
            "Mount Point": partition.mountpoint,
            "File System": partition.fstype,
            "Total Space (GB)": bytes_to_gb(usage.total),
            "Used Space (GB)": bytes_to_gb(usage.used),
            "Free Space (GB)": bytes_to_gb(usage.free),
            "Disk Usage (%)": usage.percent
        })

    # print system information
    print("System & Network Configuration Information:")
    for key, value in system_info.items():
        print(f"{key}:{value}")

    print("\n")

    # print memory information
    print("Memory Information:")
    for key, value in memory_info.items():
        print(f"{key}:{value}")

    # print disk information
    for disk in disk_info:
        print("\n")
        print("Disk Information:")
        for key, value in disk.items():
            print(f"{key}:{value}")

    print("\n")
    print('Script has Completed!')

if __name__ != "__main__":
    pass
else:
    get_system_info()
