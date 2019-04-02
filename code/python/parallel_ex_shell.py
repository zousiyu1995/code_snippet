# -*- coding: utf-8 -*-
from pssh.clients import ParallelSSHClient

hosts = [
    "cu01", "cu02", "cu03", "cu04", "cu05", "cu06", "cu07", "cu08", "cu09",
    "cu10", "cu11", "cu12", "cu13"
]
print(hosts)

client = ParallelSSHClient(hosts)
output = client.run_command("python /home/zousiyu1/bin/get_cpu_info.py")

for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, ":", line)
    for line in host_output.stderr:
        print(line)
