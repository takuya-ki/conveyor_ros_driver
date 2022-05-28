#!/usr/bin/env python

import time
import socket


class DMHCommander(object):

    def __init__(self, hostip, sockport):
        # host name/IP address of the server (dmh controller)
        self.hostip = hostip
        self.port = sockport
        self.end_message = "complete"
        self.opening()

    def opening(self):
        while True:
            print("Waiting for server to start up...")
            try:
                self.dmhctr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.dmhctr.connect((self.hostip, self.port))
                break
            except socket.error as e:
                print("Failed to connect, try reconnect.")
                time.sleep(1.0)

    def closing(self):
        # finalizing the position
        try:
            self.dmhctr.sendall(self.end_message.encode('utf-8'))
            self.dmhctr.close()
        except socket.error as e:
            print("Closing error for the dmhctr instance.")

        print("Ended the demostoration successfully!")

    def sendcommand(self, keystr):
        if self.dmhctr is not None:
            try:
                self.dmhctr.sendall(keystr.encode('utf-8'))
                while True:
                    response = self.dmhctr.recv(4096)
                    if response.decode('utf-8') == self.end_message:
                        print(response.decode('utf-8'))
                        break
                    else:
                        print("Waiting for completion.")
                        time.sleep(1.)
            except socket.error as e:
                print("Error: command sending was failed.")
                pass
        else:
            print("Error: dmh controller instance is None...")
