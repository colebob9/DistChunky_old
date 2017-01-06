"""
DistChunky Client v0.0.1
colebob9
Written in Python 3

Psuedocode:
* Read YAML config file and assign variables
* Connect to server
* If first time started, tell server that it is benchmarking, then send results once done.
* ->
* Wait for instructions.
* Once server sends an instruction to start rendering, request the specific scene file for this client.
* Start rendering.
* Once done, zip up the finished scene files, to all merge at the server. 
* Repeat from -> until recieving a disconnection from the server.
"""
import shlex
import subprocess

import socket                   # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

    
def render():
    queueNumber = 0
    chunkyPath = "ChunkyLauncher.jar"
    while True:
        try:
            currentScene = queueList[queueNumber]
            print('')
            print("Now rendering: " + currentScene)
            print('')
            subprocess.call(shlex.split("java -jar %s -render %s" % (chunkyPath, currentScene)))
            queueNumber = queueNumber + 1
        except IndexError:
            print('')
            print("All renders done!")
            break