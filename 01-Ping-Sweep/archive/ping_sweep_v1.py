"""
This is version 2 of my first python script "Ping_sweep_v2.py"
Date: 2025-12-30
Author: JeNilSE
Description:
    This script sends a ping to my proxmox server, my media server and my wazuh server.
"""
import os
targets = ["192.168.1.201", "192.168.1.226", "192.168.1.201"]
print("....Starting Ping-Sweep Please Stand by....")
for ip in targets:
    print(f"Trying to reach: {ip}")
    response = os.system(f"ping -n 1 {ip}")
    if response == 0:
        print(f"🟢 {ip} IS REACHABLE!")
    else:
        print(f"🔴 {ip} IS NOT REACHABLE!")
print