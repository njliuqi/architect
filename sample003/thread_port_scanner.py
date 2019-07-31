#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  7/31/19 2:04 PM
# @Author: edison

from __future__ import absolute_import

import socket
from threading import Thread
from argparse import ArgumentParser


class PortScanner:
    def __init__(self, target_ip, show):
        self.show_ranges = show
        self.target_ip = target_ip
        self.port_ranges = {}
        r = 0
        for i in range(256):
            n = r + 256
            self.port_ranges[str(i)] = (r, n)
            r = n

    def scan(self, begin, end):
        if self.show_ranges:
            message = "scaning range: %d - %d" % (begin, end)
            print(message)
        for port in range(begin, end):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                status = s.connect_ex((self.target_ip, port))
            except Exception:
                continue
            finally:
                s.close()

            if status != 0:
                continue
            try:
                service = socket.getservbyport(port)
            except Exception:
                service = "unknown"

            print("SERVICE: %-15s\tPORT: %-8d" % (service, port))


    def run(self):
        threads = []
        for th, ranges in self.port_ranges.items():
            t = Thread(target=self.scan, args=(ranges[0], ranges[1]))
            t.start()
            threads.append(t)

        [thread.join() for thread in threads]


if __name__ == '__main__':
    description = 'Usage: python threaded_port_scanner.py -i <IP address> '
    description += '-s (optional flag - show Port Ranges)'
    parser = ArgumentParser(description=description)
    parser.add_argument('-i', '--ip', required=True, help='IP address')
    parser.add_argument('-s', '--show', help='see ranges', action='store_true')
    args_in = parser.parse_args()
    ps = PortScanner(args_in.ip, args_in.show)
    ps.run()
