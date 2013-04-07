#!/usr/bin/python -tt

import whiskerboard
import subprocess


status = whiskerboard.WhiskerBoard(host='status.example.com', port='80')
hosts = ['www.google.com', 'domain-not-exist.com']

for host in hosts:
    command_line = 'ping -c 1 %s' % host
    args = command_line.split()
    try:
        subprocess.check_call(args,stdout=subprocess.PIPE)
        msg = "Website is up."
        print msg
        status.update_status('up', msg, 'app1')

    except subprocess.CalledProcessError:
        msg = "Website is down."
        status.update_status('down', msg, 'app1')
