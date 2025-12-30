import subprocess
targets = ["192.168.1.201", "192.168.1.200", "192.168.1.226"]
print ("....Starting Ping Sweep v2....")
for ip in targets:
    command = ["ping", "-n", "1", ip]
    result = subprocess.run(command, capture_output=True)
    if result.returncode == 0:
        print (f"🟢 {ip} IS REACHABLE!")
    else:
        print (f"🔴 {ip} IS NOT REACHABLE!")
print ("!!!SCAN COMPLETED!!!")