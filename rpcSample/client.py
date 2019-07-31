#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  10/25/18 10:52 AM
# @Author: edison

from __future__ import absolute_import
import grpc
from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(data_pb2.Data(text='hello,world!'))
    print("received: " + response.text)


if __name__ == '__main__':
    run()