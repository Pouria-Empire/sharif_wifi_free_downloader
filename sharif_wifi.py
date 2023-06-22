import requests
import re
import time

def sharif_login(username, password):
    payload = {"username": username, "password": password}
    requests.post("https://net2.sharif.edu/login", data=payload)
    response = requests.get("https://net2.sharif.edu/status")
    print(re.findall(r'<td>.*</td>', response.text))
    time.sleep(1)

def sharif_ip(username, password):
    payload = {"username": username, "password": password}
    requests.post("https://172.17.1.214/login", data=payload, verify=False)
    response = requests.get("https://172.17.1.214/status", verify=False)
    print(re.findall(r'<td>.*</td>', response.text))
    time.sleep(1)

def sharif_logout():
    payload = {"username": "test", "password": "test"}
    requests.post("https://net2.sharif.edu/logout", data=payload)
    time.sleep(1)

# Replace "YourUsername" and "YourPassword" with your actual credentials
your_username = "Pouria_ArefiJamal"
your_password = ":))"

sharif_login1 = lambda: sharif_login(your_username, your_password)
sharif_ip1 = lambda: sharif_ip(your_username, your_password)

# Usage:
sharif_logout()
for i in range(100):
    sharif_login1()
    time.sleep(9)
    sharif_logout()

# login with ip
# sharif_ip1()
