from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
import sys

clients = {}
addresses = {}
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

msg_list = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def recieve():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf-8")
            msg_list.append(msg)
        except:
            pass


def send(event=None):
    msg = "hello"
    client_socket.send(bytes(msg, "utf8"))
    time.sleep(5)

    client_socket.send(bytes(msg, "utf8"))


while True:
    try:
        recv = client_socket.recv(BUFSIZ)
        print("FROM SERVER:", recv)
    except:
        continue

    msg = sys.stdin.readline()
    client_socket.send(bytes(msg, "utf-8"))

client_socket.close()
