import socket
import requests

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

public_ip = requests.get("https://api.ipify.org").text

print(f'Host Name:  {hostname}')
print(f'Local IP:  {local_ip}')
print(f'Public IP:  {public_ip}')