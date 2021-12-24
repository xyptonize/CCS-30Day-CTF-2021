import socket
import threading
from random import randint


a = """ 


|  \/  | __ _| |_| |__   __| | __ _  __ _   ___  __ _(_)_ __  
| |\/| |/ _` | __| '_ \ / _` |/ _` |/ _` | / __|/ _` | | '_ \ 
| |  | | (_| | |_| | | | (_| | (_| | (_| | \__ \ (_| | | | | |
|_|  |_|\__,_|\__|_| |_|\__,_|\__,_|\__,_| |___/\__,_|_|_| |_|
                                                              
 _                 _   _               _       _ 
| |__  _   _ _ __ | | | |__   ___   __| | ___ (_)
| '_ \| | | | '_ \| | | '_ \ / _ \ / _` |/ _ \| |
| | | | |_| | | | | | | |_) | (_) | (_| | (_) | |
|_| |_|\__,_|_| |_|_| |_.__/ \___/ \__,_|\___// |
                                            |__/ 
      _               _             
  ___| |__   __ _  __| |_ __   __ _ 
 / __| '_ \ / _` |/ _` | '_ \ / _` |
| (__| | | | (_| | (_| | | | | (_| |v
 \___|_| |_|\__,_|\__,_|_| |_|\__,_|
                                     \n"""

incorrect = """
|___ \  | |_ ___   ___    _ __   ___ _ __ ___  (_)
  __) | | __/ _ \ / _ \  | '_ \ / _ \ '_ ` _ \ | |
 / __/  | || (_) | (_) | | | | |  __/ | | | | || |
|_____|  \__\___/ \___/  |_| |_|\___|_| |_| |_|/ |
                                             |__/ 
      _               _       _                 _                              
  ___| |__   __ _  __| | __ _| |__   __ _ _   _(_)  _   _ _ __ ___   __ _ _ __ 
 / __| '_ \ / _` |/ _` |/ _` | '_ \ / _` | | | | | | | | | '_ ` _ \ / _` | '__|
| (__| | | | (_| | (_| | (_| | | | | (_| | |_| | | | |_| | | | | | | (_| | |   
 \___|_| |_|\__,_|\__,_|\__,_|_| |_|\__, |\__,_|_|  \__, |_| |_| |_|\__,_|_|   
                                    |___/           |___/                      
                                           _               __
 ___ _   _  __ _  __ _   _   _ _ __ ___   | |__   ___   _ / /
/ __| | | |/ _` |/ _` | | | | | '_ ` _ \  | '_ \ / _ \ (_) | 
\__ \ |_| | (_| | (_| | | |_| | | | | | | | |_) |  __/  _| | 
|___/\__,_|\__, |\__,_|  \__, |_| |_| |_| |_.__/ \___| (_) | 
           |___/         |___/                            \_\

"""


num1 = randint(10000, 20000)
num2 = randint(10000, 20000)
randsum = num1 + num2

result = str(num1) + "+" + str(num2) + "="
size = 1024
HEADER = 64
ADDR = ('0.0.0.0', 10000)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


flag = "M@tH_iS_k0n1_0F_sC13nCe"


def handle_client(conn, addr):
    conn.settimeout(3)
    try:
        data = conn.recv(size).decode()
        if int(data) == randsum:
            conn.send(flag.encode())
        else:
            conn.send(incorrect.encode())
    except:
        conn.send(incorrect.encode())
    conn.close()


def start():
    server.listen()
    print("Server is listening on")

    conn, addr = server.accept()
    conn.send(a.encode())
    conn.send(result.encode())
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

    pr


print("STARTING")
start()
