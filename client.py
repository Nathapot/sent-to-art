import socket

# serverip = "localhost"
serverip = "104.248.39.146"
port = 27617
# arr = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']

while True:
    data = "{}-{}-{}".format('bilimbi', 'calamansi', 'clementines') #น่าจะอันเดียวกันของกูใช้ 3 ตัวนี้อะ กูเอาลูปออกไปละมันช้า ถ้ารันได้ก็ได้ลิ้งละ
    print(data)
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server: ', data_server)
    server.close()