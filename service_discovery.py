PORT = 50000
MAGIC = "fna349fn"

from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
s.bind(('', PORT))

while 1:
    data, addr = s.recvfrom(1024) #wait for a packet
    data = data.decode('utf-8')
    if data.startswith(MAGIC):
        print("got service announcement from", addr)