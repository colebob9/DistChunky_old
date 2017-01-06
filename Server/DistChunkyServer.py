"""
DistChunky Server v0.0.1
colebob9
Written in Python 3
"""

import shlex
import subprocess
import yaml
import os.path
import os                   
import time
import socket                   # Import socket module
import sys
from _thread import *


# Defining YAML
def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)
def yaml_load(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

# Introduction
print("DistChunky v0.0.1")
print("Written by colebob9")
print("Source Code on GitHub.com/colebob9/DistChunky")
print('')
# Read config files and assign variables
# Configuration:
# !!!: Needs actual configuration
filepath = "config/testdump.yaml"
filepathExists = os.path.exists(filepath)
if filepathExists == True:
    conf_File = yaml_load(filepath)
    print("Loaded YAML:")
    print(conf_File['port'])
elif filepathExists == False: # Fill in config
    conf_File = {'port': '5000', 'age': 39, 'height': 6 * 12 + 2}
    yaml_dump(filepath, conf_File)
    print("New YAML config file created.")
else:
    print("YAML error!")
""" # exit to configure file
    exit_Conf = input('Exit to configure file? (Y/N) ')
    if exit_Conf == 'Y':
        print("Exiting.")
        exit()
    elif exit_Conf == 'N':
        print('Continuing.')
    else:
        print("Please use Y/N.")
"""

# Read Scene files in the scenes directory, list .zip files, and assign to queue
# !!!: Needs check for folder and create if it doesn't exist
currentQueue = []
for file in os.listdir("scenes/input"):
    if file.endswith(".zip") == False:
        print("\"%s\" is not a valid scene file format. Exiting." % file)
        exit()
    elif file.endswith(".zip"):
        print("Found scene: %s" % file)
        currentQueue.append(file)   # !!!: Add code to allow user to do the queue in any order.
    else:
        print("No scenes found, exiting.")
        exit()

if currentQueue == []:
    print("No scenes found. Exiting.")
    exit()    
print("\nAll queued scenes:")
print(currentQueue)
# Connect to clients and have them wait for instruction
# Wait for input from user to stop looking for clients and start only with the clients given.

'''
Simple socket server using threads
'''
 
host = socket.gethostname() 
port = 60000                    # Reserve a port for your service.
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((host, port))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('send_config') # send only takes string
     
    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))

        filename='oldcode.py'
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
           conn.send(l)
           print('Sent ',repr(l))
           l = f.read(1024)
        f.close()

        print('Done sending')
        conn.send('Thank you for connecting')
        conn.close()
    #infinite loop so that function do not terminate and thread do not end.
    """
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        if data == "":
            print(data)
        elif data == "":
            print
        else:
            print("Recieved an invalid command from client %s" % conn)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
    """
 
# now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
    

# Send command to start to benchmark, then wait for results back from each.
"""[Code]"""
# Save to a "clients" YAML file 

#exit()