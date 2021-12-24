import socket
host = '18.141.145.22'
port = 10000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
answer = s.recv(1024)
print(answer.decode())
exp = s.recv(1024)
arr = str(exp).split('+')
print(arr)
a = arr[0]
b = arr[1]
result = int(a[2:]) + int(b[:len(b)-2])
s.send(str(result).encode())
print(s.recv(1024).decode())
s.close()
