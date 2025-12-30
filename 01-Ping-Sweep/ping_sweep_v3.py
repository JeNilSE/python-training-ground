"""
This is version 3 of my first python script "Ping_sweep_v3.py"
Date: 2025-12-30
Author: JeNilSE
Despcription:
    This script sends a ping to my proxmox server, my media server and my wazuh server 
    and tells me if they're up or down and then logs it with time and date in a logfile.
"""



import subprocess
from datetime import datetime
targets = ["192.168.1.200", "192.168.1.201", "192.168.1.226"]
print ("....STARTING SCAN PLEASE STAND BY....")
with open ("ping_logg.txt", "a") as logfile:
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logfile.write(f"\n--- Scanning started: {timestamp} ---\n")
    for ip in targets:
        command = ["ping", "-n", "1", ip]
        result = subprocess.run(command, capture_output=True)
        if result.returncode == 0:
            status = "REACHABLE"
            Symbol = "✅"
        else:
            status = "UNREACHABLE"
            Symbol = "⛔"
        print(f"{Symbol} {ip} IS {status}")
        logfile.write(f"{timestamp} - {ip} IS {status}\n")
print ("....SCANNING COMPLETED & LOGGED")