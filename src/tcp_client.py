import socket
import sys

def run_client():
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        print("connecting to server!")
        c.connect(('127.0.0.1',65421))
        while True:
            message = input()
            c.sendall(message.encode('utf-8'))
            print(f"sent {message} ")

            data = c.recv(1024)
            print(f"recieved from server {data.decode('utf-8')}")
    except ConnectionRefusedError:
        print("Error: Could not connect to the server")
    except KeyboardInterrupt:
        print("client is being closed initiate shutdown")
       

    finally:
        c.close()
        print("Client connection ended")

if __name__ == "__main__":
    run_client()
