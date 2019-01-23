import socket

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))         # Connect to sever

count = 0
while count < 5:
    letter = input("Guess a letter ")
    b = letter.encode('utf-8')     # Encodes to bytes
    data = s.send(b)    # Recieves data from server

    print(s.recv(1024))
    if s.recv(1024) == b"Wrong letter":
        print("wrong")
        count += 1


s.close() # Closes connection to server
print('Connection closed')

