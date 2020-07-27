# Login:
USERNUMBER = "12345678"
PASSWORD = 'password123'

# Since date:
datestr = "Jul 15 21:00:00 2020"

# Symbol:
SYMBOL = "US100"

import socket
import ssl
import json
import time
import csv

class xserver(object):
    """docstring for xserver"""
    def __init__(self):
        super(xserver, self).__init__()
        host = 'xapi.xtb.com'
        port = 5124 # For demo account

        host = socket.getaddrinfo(host, port)[0][4][0]
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.sock = ssl.wrap_socket(self.sock)

        json_to_send = {
            "command" : "login",
            "arguments" : {
                "userId": USERNUMBER,
                "password": PASSWORD
            }
        }
        packet = json.dumps(json_to_send)
        self.sock.send(packet.encode("utf-8"))
        
        ans = self.sock.recv(4096)
        print("Print login:", json.dumps(ans[:-2].decode("utf-8"),indent=2))

    def logout(self):
        json_to_send = {
            "command" : "logout"
        }
        packet = json.dumps(json_to_send)
        self.sock.send(packet.encode("utf-8"))

        ans = self.sock.recv(4096)
        print("Print logout:", json.dumps(ans[:-2].decode("utf-8"),indent=2))

    def send_cmd(self,CMD):
        packet = json.dumps(CMD)
        self.sock.send(packet.encode("utf-8"))
        ans = self.sock.recv(4096)
        while b'\n\n' not in ans:            
            ans += self.sock.recv(4096)
            
        # print("Print", CMD['command'],":", json.dumps(ans[:-2].decode("utf-8"),indent=2))
        return str(ans)

    def get_symbols(self):
        self.send_cmd({"command": "getAllSymbols"})


# Whit this the time will be done
times = time.mktime(time.strptime(datestr, "%b %d %H:%M:%S %Y")) * 1000
times = round(times)
# print(times)


XTB = xserver()
aux = XTB.send_cmd({"command": "getAllSymbols"})[2:-5].replace("\\", "\\\\")
aux = json.loads(aux)["returnData"]


f = open("symbols.txt","w")
for s in aux:
    f.write(s["symbol"]+" - "+ s["description"] + "\n")
f.close()


a = XTB.send_cmd({
    "command": "getChartLastRequest",
    "arguments": {
        "info": {
            "period": 1440,
            "start": times,
            "symbol": SYMBOL
        }
    }
})[2:-5]
a = json.loads(a)
# print(json.dumps(a))
XTB.logout()

# data to csv
dataout={}
dataout = a["returnData"]["rateInfos"]

csv_file = open('out.csv', 'w')
csv_writer = csv.writer(csv_file) 
csv_writer.writerow(dataout[0].keys()) 

for row in dataout:
    csv_writer.writerow(row.values())
csv_file.close()







