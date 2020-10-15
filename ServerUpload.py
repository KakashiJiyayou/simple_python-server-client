import socket
import  _thread
import os
import time
s = socket.socket()
host ="localhost"
port = 54321
password = "1234"
s.bind(('',port))
s.listen()


def mainFunc(c):
    try:
        data = c.recv(1024).decode()
        print("password sent : " +data + "\n")
        time.sleep(1)
        if data == password:
            c.send(("password verified" + "\n").encode('utf-8'))
        else:
            c.close

        data = c.recv(1024).decode()
        time.sleep(1)
        filename = data
        print("File name : "+ filename + "\n")
        c.send(("Got File Name " + "\n").encode('utf-8'))

    except IOError:
        print("Error")

    try:
        data = c.recv(1024).decode()
        print(data + "\n")
        f = open(filename, 'w')
        f.write(data)
        f.close()
        time.sleep(3)
        c.send((" bye bye" + "\n").encode('utf-8'))
    except IOError:
        print("Error", IOError.with_traceback())
    c.close()

while True:
    c, addr = s.accept()
    print("New Client")
    _thread.start_new_thread(mainFunc,(c,) )


