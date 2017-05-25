import socket
import threading
import json
HOST = "192.168.35.121"
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 테스트용 Python Dictionary
center = "128"

customer = {

    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': center},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

# JSON 인코딩
jsonString = json.dumps(customer, indent=4)

def sendingMsg():
    while True:
        data = jsonString
        data = bytes(data, "utf-8")
        s.send(data)
    s.close()

def gettingMsg():
    while True:
        data = s.recv(1024)
        data = data.decode("utf-8","ignore")
        print(data)
    s.close()

threading._start_new_thread(sendingMsg,())
threading._start_new_thread(gettingMsg,())

while True:
    pass

