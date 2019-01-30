import socket
import random

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

# Opens file and picks a random word
with open('file.txt', 'r') as f:
    lines = f.readlines()
    n = random.randrange(0,len(lines))
    word = (lines[n][:-1])

# Makes a list for dashes and where the correctly guessed letters in the word will be stored
count = 0
newWord = []
for i in range(len(word)):
    newWord.append("_ ")

while True:
    conn, addr = s.accept()     # Establish connection with client.

    while count < 5:

        str1 = ''.join(newWord)
        b = str1.encode('utf-8')
        conn.send(b)

        print(str1)
        print(newWord)

        data = conn.recv(1024)

        l = data.decode("utf-8")
        if l in word:
            for i in range(len(word)):
                if word[i] == l:
                    newWord[i] = l
                    str1 = ''.join(newWord)
                    b = str1.encode('utf-8')
                    conn.send(b)

        else:
            conn.send(b"Wrong letter")
            count += 1
        if "_ " not in newWord:
            conn.send(b"The word was " + b + b" You win")
            break
    conn.close()   # Closes connection
