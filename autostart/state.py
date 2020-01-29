#!/usr/bin/python3
# -*- coding! utf-8 -*-


import os
import time
from subprocess import Popen, PIPE
from datetime import datetime
import psutil


def sys_state():

    state = ''
    # net speed
    s1 = psutil.net_io_counters()
    time.sleep(1)
    s2 = psutil.net_io_counters()
    down_speed = (s2.bytes_recv - s1.bytes_recv) / 1024
    if down_speed < 1024:
        down_speed = '{:.2f}kb/s'.format(down_speed)
    elif down_speed >= 1024:
        down_speed /= 1024
        down_speed = '{:.2f}mb/s'.format(down_speed)

    up_speed = (s2.bytes_sent - s1.bytes_sent) / 1024
    if up_speed < 1024:
        up_speed = '{:.2f}kb/s'.format(up_speed)
    elif up_speed >= 1024:
        up_speed /= 1024
        up_speed = '{:.2f}mb/s'.format(up_speed)

    state += '↓ {} ↑ {} '.format(down_speed, up_speed)

    # sys usage
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    state += '▣ {}% Ⅱ {}% ∞ {}% '.format(cpu, mem, swap)

    # battery
    cmd = "acpi -b | grep 'Battery 1' | awk '{ print $3, $4 }' | tr -d ','"
    with Popen(cmd, shell=True, stdout=PIPE) as s:
        out, _ = s.communicate()
    out = out.decode().replace('\n', '')

    if out.startswith('F'):
        out = '▪▪▪ 100%'
    elif out.startswith('C'):
        global bat_sign
        if len(bat_sign) == 3:
            bat_sign.clear()
        bat_sign.append('▪')
        out = out.replace('Charging', ''.join(bat_sign).ljust(3, ' '))
    elif out.startswith('D'):
        if int(out[12:-1]) <= 33:
            out = out.replace('Discharging', '▫')
        elif 33 < int(out[12:-1]) <= 66:
            out = out.replace('Discharging', '▫▫')
        elif 66 < int(out[12:-1]) <= 100:
            out = out.replace('Discharging', '▫▫▫')

    else:
        out = '▪▪▪ ▫▫▫'

    state += '{} '.format(out)

    # date time
    state += datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    state = state.rjust(80, ' ')
    return state


if __name__ == '__main__':

    bat_sign = []
    while True:
        os.system('xsetroot -name "{}"'.format(sys_state()))
