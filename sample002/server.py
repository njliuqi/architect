#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  7/31/19 10:00 AM
# @Author: edison

from __future__ import absolute_import

"""
    Server from multithreaded (asynchronous) chat application.
"""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = '0.0.0.0'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def accept_incoming_connections():
    """
        Sets up handing for incoming clients.
    :return:
    """
    while True:
        client, client_addr = SERVER.accept()
        print("%s has connected" % client_addr)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!"))
        addresses[client] = client_addr
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """
        Handles a single client connections
    :param client:
    :return:
    """
    name = client.recv(BUFSIZ).decode('UTF-8')
    welcome = 'Welcome %s ! if you ever want to quit. type {quite} to exit.' % name
    client.send(bytes(welcome, "UTF-8"))
    msg = "%s has joined the chat." % name
    broadcast(bytes(msg, "UTF-8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "UTF-8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quite}", "UTF-8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "UTF-8"))
            break



def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "UTF-8") + msg)


if __name__ == "__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print('Waitting for connection...')
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
