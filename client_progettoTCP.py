import socket

HOST = 'localhost'    # Il nodo remoto, qui metti il tuo indirizzo IP per provare connessione server e client dalla tua macchina alla tua macchina
PORT = 50010             # La stessa porta usata dal server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    if(data.decode()=="STOP"):
        print("password ERRATA troppe volte, arrivederci")
        break
    subs=":"
    print('Received: ', data.decode())
    if  data.decode().find(subs):
        testo = input("").encode()
        s.send(testo)
    if(data.decode()=="S"):
        break


s.close()