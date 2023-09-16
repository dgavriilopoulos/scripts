import os
import wmi
import sys

python_path = sys.executable

def running_processes():
    f = wmi.WMI()

    for process in f.Win32_Process():
        print(f"{process.ProcessId:10} {process.Name} {process.ExecutablePath}")

if __name__ == "__main__":

    print(f'Python Interpreter Path: {python_path}')

    print("\n","ProcessID", "ProcessName","ExecutablePath")

    list_running_processes = running_processes()
    print(list_running_processes)
