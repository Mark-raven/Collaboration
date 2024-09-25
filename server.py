import socket
import threading

# List to keep track of connected clients
clients_list = []

# Function to broadcast a message to all clients
def broadcast(message, connection=None):
    for client in clients_list:
        if client != connection:
            try:
                client.send(message)
            except:
                # If the client is disconnected, remove it from the list
                remove_client(client)

# Function to remove a client from the list
def remove_client(connection):
    if connection in clients_list:
        clients_list.remove(connection)

# Function to handle each client connection
def client_handler(connection, address):
    # Send a welcome message to the client
    connection.send("Welcome to this chatroom!".encode())
    while True:
        try:
            # Receive messages from the client
            message = connection.recv(2048)
            if message:
                # Print the message and address of the user on the server terminal
                print(f"<{address[0]}> {message.decode()}")

                # Broadcast the message to all other clients
                broadcast(f"<{address[0]}> {message.decode()}".encode(), connection)
            else:
                # Remove the connection if the message is empty
                remove_client(connection)
                break
        except:
            continue

# Function to allow the server to send messages to all clients
def server_message_handler():
    while True:
        message = input()  # Read server input
        if message:
            # Broadcast the server's message to all clients
            broadcast(f"<Server> {message}".encode())

def main():
    # Initialize the server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Define server address and port
    IP_address = "127.0.0.1"  # Change this to the desired IP address
    Port = 12345              # Change this to the desired port number

    # Bind the server to the specified IP address and port
    server.bind((IP_address, Port))

    # Start listening for incoming connections
    server.listen(100)
    print(f"Server started on {IP_address}:{Port}")

    # Start the server message handler thread
    threading.Thread(target=server_message_handler).start()

    while True:
        # Accept a new connection
        connection, address = server.accept()
        
        # Add the client to the list of clients
        clients_list.append(connection)

        # Print the address of the connected client
        print(f"{address[0]} connected")

        # Start a new thread for handling the client's messages
        threading.Thread(target=client_handler, args=(connection, address)).start()

    # Close the server socket (unreachable in this infinite loop)
    server.close()

if __name__ == "__main__":
    main()
           
