import os
import socket
import time
import  tkinter as tk
from tkinter import  filedialog

root = tk.Tk()
filepath = filedialog.askopenfilename()
fileNAme = os.path.basename(filepath)

root.withdraw()
password = "1234"


time.sleep(4)

HOST = 'localhost'    # The remote host
PORT = 54321           # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))

s.send(password.encode('utf-8'))
data = s.recv(1024).decode()
print("Server send " + data)
s.send(fileNAme.encode('utf-8'))
data = s.recv(1024).decode()
print("Server send " + data)

f = open(filepath)
value = f.read()
f.close()
s.sendall(value.encode("utf-8"))
data = s.recv(1024).decode()
print("Server send " + data)
s.close()
# while True:
#     haha = "Client 1\n"
#     s.send(haha.encode('utf-8'))
#     data = s.recv(1024).decode()
#     print("Server send")
#     time.sleep(2)
