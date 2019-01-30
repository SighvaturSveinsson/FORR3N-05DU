import socket

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))         # Connect to sever

count = 0
while count < 5:

    print("Tries left: ", 5-count)
    wordData = s.recv(1024)

    print(wordData)

    letter = input("Guess a letter ")
    b = letter.encode('utf-8')     # Encodes to bytes
    data = s.send(b)    # Recieves data from server

    wordData2 = s.recv(1024)

    if wordData2 == b"Wrong letter":
        print("Wrong letter")
        count += 1


s.close() # Closes connection to server
print('Connection closed')

