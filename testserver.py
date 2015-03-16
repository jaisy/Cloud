import socket
import os
import select
import sys


try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

PORT = 8081
HOST = '127.0.0.1'
RECV_BUFFER = 4098

server_socket.bind((HOST, PORT))
server_socket.listen(10)
print "Ready to receive the data"
while True:
    # print server_socket.recv(RECV_BUFFER)
    c, addr = server_socket.accept()
    print addr
    M = c.recv(4098)
    c1=M.split(":")[0]
    c2=M.split(":")[1]
    print "c1 = ", c1
    print "c2 = ", c2
    C = int(c1) + int(c2)
    Cmul = int(c1) * int(c2)
    print "Result after performing addition operation on c1 and c1 : ", C
    print "result after multiplication operation : ", Cmul
    print " "
    print "Results after the operations are SENT to the client"
    c.send(str(C)+":"+str(Cmul))
    
server_socket.close()


