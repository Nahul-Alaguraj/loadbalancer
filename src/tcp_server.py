import socket
import sys
def run_server():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as err:
        print("failed to create socket")
        return


    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #free socket for other programs once server is terminated
    s.bind(("127.0.0.1",65421)) #socket ready to bind at this port
    s.listen(5)
    s.settimeout(1.0)
    print("server is listening")
    try:
        while True:
            try:
                c_conn,c_address = s.accept()
                c_conn.settimeout(5.0)
                print("Connected successfully")
                
                while True:
                    try:
                        data = c_conn.recv(1024)
                    except socket.timeout:
                        continue
                    if data:
                        print(f"Received from client {data}")
                        c_conn.sendall(data)
                    else:
                        print(f"client {c_address} disconnected")
                        break
                c_conn.close()
                print(f"connection with {c_address} closed.")
            except socket.timeout:
                pass
    except KeyboardInterrupt:
        print("\n shutting down the server")
    finally:
        s.close()

if __name__=="__main__":
    run_server()

