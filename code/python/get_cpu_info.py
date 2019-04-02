# -*- coding: utf-8 -*-
import psutil
import sys
import os

cpu_percents = []

for num in range(10):
    cpu_percents.append(psutil.cpu_percent(interval=0.5))

print(round(sum(cpu_percents) / len(cpu_percents)))
