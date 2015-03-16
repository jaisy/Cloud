import socket
import os
import select
import sys


HOST = '127.0.0.1'
PORT = 8081
p = input('p = ')
q1 = input('q1 = ')
r1 = input('r1 = ')
b1 = input('b1 = ')
q2 = input('q2 = ')
r2 = input('r2 = ')
b2 = input('b2 = ')
b = b1^b2
print "b1 XOR b2, b = ", b
bb = b1&b2
print "b1 AND b2, b = ", bb
c1 = (int(p) * int(q1)) + (2 * int (r1)) + int(b1)
print "c1 = ", c1
c2 = (int(p) * int(q2)) + (2 * int(r2)) + int(b2)
print "c2 =", c2
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

print 'Connected to remote host. Start sending messages'

s.send(str(c1)+":"+str(c2))

while True:

    M = s.recv(4098)
    C=M.split(":")[0]
    Cmul=M.split(":")[1]
    print "Cipher text received from server after addition operation= ", C
    print " "
    print "Cipher text received from server after multiplication operation = ", Cmul
    print""
    N1 = int(C) % p
    N2 = int(Cmul) % p
    print "Result after mod operation C % p : ", N1
    print "Result after mod operation Cmul % p : ", N2
    print ""
    print "ADDITION"
    if N1 % 2 == 0:
        print "Expecting b = 0, Expected number is even. Noise = ", N1
    else:
        print "Expecting b = 1, Expected number is odd. Noise = ", N1
    print ""
    print "MULTIPLICATION"
    if N2 % 2 == 0:
        print "Expecting b = 0, Expected number is even. Noise = ", N2
    else:
        print "Expecting b = 1, Expected number is odd. Noise = ", N2

s.close()


