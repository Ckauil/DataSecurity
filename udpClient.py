import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind((target_host,target_port))

dt = "AAABBBCCC"

client.sendto(dt.encode('ascii'),(target_host,target_port))

data, addr = client.recvfrom(4096)

print(data.decode('ascii'))
client.close()
