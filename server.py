from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def accept_incoming_connections():
    while True:
        client, client_addres = SERVER.accept()
        print(f'{client_addres} has been connected')
        client.send(bytes("Welcome to chat", "utf-8"))

        addresses[client] = client_addres
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client: socket):
    clients[client] = client.getpeername()

    broadcast_msg = f"{client.getpeername()} is joined"
    broadcast_handler(bytes(broadcast_msg, "utf-8"))

    while True:
        try:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{quit}", "utf-8") and bool(msg):
                print("MSG", msg, bool(msg))
                broadcast_handler(msg, client.getpeername())
            else:
                client.send(bytes("{quit}", "utf-8"))
                client.close()
                del clients[client]
                broadcast_handler(bytes(f"{client.getpeername()} has left the chat", "utf-8"))
                break
        except:
            continue


def broadcast_handler(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix + ':', "utf-8") + msg)


if __name__ == "__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
