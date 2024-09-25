import socket
import select
import sys
import threading

def send_message(server):
    while True:
        message = input()  # Use input() directly for Windows
        if message:
            server.send(message.encode())
            sys.stdout.write("<You> ")
            sys.stdout.write(message + "\n")
            sys.stdout.flush()

def receive_message(server):
    while True:
        try:
            message = server.recv(2048).decode()
            if message:
                print(message)
            else:
                # Server has closed the connection
                print("Disconnected from the server")
                server.close()
                break
        except:
            # Handle errors (like server disconnection)
            print("Error occurred. Disconnecting...")
            server.close()
            break

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Correct usage: script, IP address, port number")
        exit()

    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))

    # Create separate threads for sending and receiving messages
    send_thread = threading.Thread(target=send_message, args=(server,))
    receive_thread = threading.Thread(target=receive_message, args=(server,))

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

    server.close()
