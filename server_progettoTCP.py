import threading 
import socket
import mysql.connector
comunicazioni = ["",""]
PASSWORD = "CIAO"
lock=threading.Lock()
def gestisci_comunicazione(conn):
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    i=0
    while data != PASSWORD and i<2:
        i+=1
        conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {3-i} ".encode())
        data = conn.recv(1024).decode()      

    if(data != PASSWORD):
        conn.send("STOP".encode())
        

    while True:
        conn.send("Benvenuto, cosa vuoi fare: I=insert, U=update,R=read,D=delete oppure X per uscire".encode())
        data = conn.recv(1024).decode()
        print(data)
        scelta=data
        if(scelta=="X"):
            conn.send("S".encode())
            conn.close()
        elif(scelta=="R"):
            conn.send("su che tabella vuoi cercare? C=clienti, Z=zone di lavoro:".encode())
            data = conn.recv(1024).decode()            
            dati_query = db_R(data)
            #print(dati_query)
            #print(len(dati_query))
            #print(len(dati_query[0]))
            a="\n----------------------------------------\n"
            for j in range (0,len(dati_query)):
                for i in range (0, len(dati_query[j])):
                    a=a+str(dati_query[j][i])+"\n"
                a=a+"----------------------------------------\n"
        
            print(dati_query)
            conn.send(a.encode())
        elif(scelta=="D"):
                lock.acquire()
                conn.send("LOCK ACQUISITO!(premi invio per continuare)".encode())
                conn.send("su che tabella vuoi eliminare i dati? C=clienti Z=zone di lavoro:  ".encode())
                data = conn.recv(1024).decode()
                risposta=db_D(data,conn)
                print(risposta)
                conn.send(risposta.encode())
                lock.release()
        elif(scelta=="U"):
                lock.acquire()
                conn.send("LOCK ACQUISITO!(premi invio per continuare)".encode())
                conn.send("su che tabella vuoi aggiornare i dati? C=clienti Z=zone di lavoro:   ".encode())
                data = conn.recv(1024).decode()
                risposta=db_U(data,conn)
                print(risposta)
                conn.send(risposta.encode())
                lock.release()
        elif(scelta=="I"):
                lock.acquire()
                conn.send("LOCK ACQUISITO!(premi invio per continuare)".encode())
                conn.send("su che tabella vuoi inserire i dati? C=clienti Z=zone di lavoro:   ".encode())
                data = conn.recv(1024).decode()
                risposta=db_I(data,conn)
                print(risposta)
                conn.send(risposta.encode())
                lock.release()
        
            
            
        


def db_R(a):
    cono = mysql.connector.connect(
        host="localhost",
        user="sumi",
        password="hamil1234",
        database="5ATepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )

    cur = cono.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    if a=="C":
        query = "SELECT * FROM dipendenti_sami_hamil"
        cur.execute(query)
        dati = cur.fetchall()
    if a=="Z":
        query = "SELECT * FROM zone_di_lavoro_sami_hamil"
        cur.execute(query)
        dati = cur.fetchall()
    return dati
def db_D(a,conn):
    cono = mysql.connector.connect(
        host="localhost",
        user="sumi",
        password="hamil1234",
        database="5ATepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )
    cur = cono.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    if a=="C":
        conn.send("Inserisci l'id da rimuovere: ".encode())
        id=(conn.recv(1024)).decode()

        query = (f"DELETE FROM dipendenti_sami_hamil where id = '{id}'")
        print(id)
        print(query)
        cur.execute(query)
        cono.commit()
        dati = "Dati rimossi correttamente"
    if a=="Z":
        conn.send("Inserisci l'id della zona da rimuovere: ".encode())
        id=(conn.recv(1024)).decode()
        print(id)
        query = (f"DELETE FROM zone_di_lavoro_sami_hamil where id_zona = '{id}'")
        print(query)
        cur.execute(query)
        cono.commit()
        dati = "Dati rimossi correttamente"
    return dati

def db_U(a,conn):
    cono = mysql.connector.connect(
        host="localhost",
        user="sumi",
        password="hamil1234",
        database="5ATepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )
    cur = cono.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    if a=="C":
        conn.send("INSERISCI L'ID: ".encode())
        idUtent=conn.recv(1024).decode()
        idUtent="id = "+"'"+str(idUtent)+"'"
        conn.send("SELEZIONA IL PARAMETRO CHE VUOI CAMBIARE :\n1 - ID \n2 - NOME\n3 - COGNOME\n4 - INDIRIZZO\n5 - TELEFONO\n6 - POSIZIONE LAVORATIVA\n7 - DATA ASSUNZIONE\n8 - DATA NASCITA ".encode())
        risp=conn.recv(1024).decode()
        while int(risp) <= 0 or int(risp) >8 :
            conn.send("SELEZIONA IL PARAMETRO CHE VUOI CAMBIARE :\n1 - ID \n2 - NOME\n3 - COGNOME\n4 - INDIRIZZO\n5 - TELEFONO\n6 - POSIZIONE LAVORATIVA\n7 - DATA ASSUNZIONE\n8 - DATA NASCITA".encode())
            risp=conn.recv(1024).decode()
        cos=""
        a=""
        risp=int(risp)
        if risp==2:
            conn.send("Inserisci il nuovo nome: ".encode())
            cos=conn.recv(1024).decode()
            a="nome = "+"'"+cos+"'"
        elif risp==3:
            conn.send("Inserisci il nuovo cognome: ".encode())
            cos=conn.recv(1024).decode()
            a="cognome = "+"'"+cos+"'"
        elif risp==4:
            conn.send("Inserisci il nuovo indirizzo: Via ".encode())
            cos=conn.recv(1024).decode()
            a="indirizzo = "+"'"+cos+"'"
        elif risp==1:
            conn.send("Inserisci il nuovo ID: ".encode())
            cos=str(conn.recv(1024).decode())

            a="id = "+"'"+str(cos)+"'"
        elif risp==5:
            conn.send("Inserisci il nuovo numero di telefono: ".encode())
            cos=str(conn.recv(1024).decode())
            while len(cos)>10:
                conn.send("Inserisci il nuovo numero di telefono: ".encode())
                cos=str(conn.recv(1024).decode())
            a="telefono = "+"'"+str(cos)+"'"
        elif risp==6:
            conn.send("Inserisci la nuova posizione lavorativa: ".encode())
            cos=conn.recv(1024).decode()
            a="posizione lavorativa = "+"'"+cos+"'"
        elif risp==7:
            conn.send("Inserisci la data di assunzione(anno-mese-giorno): ".encode())
            cos=conn.recv(1024).decode()
            a="data di assunzione = "+"'"+cos+"'"
        elif risp==8:
            conn.send("Inserisci la data di nascita(anno-mese-giorno): ".encode())
            cos=conn.recv(1024).decode()
            a="data di nascita = "+"'"+cos+"'"
        

        print(a)
        query = (f"UPDATE dipendenti_sami_hamil SET {a} WHERE {idUtent}")
        print(query)
        cur.execute(query)
        cono.commit()
        dati = "Dati aggiornati correttamente(premi invio per continuare)"
    if a=="Z":
        conn.send("INSERISCI L'ID DIPENDENTE: ".encode())
        idUtent=conn.recv(1024).decode()
        idUtent="id_dipendenti= "+"'"+str(idUtent)+"'"
        conn.send("SELEZIONA IL PARAMETRO CHE VUOI CAMBIARE: \n1 - ID ZONA \n2 - NOME ZONA\n3 - NUMERO_CLIENTI\n4 - ID DIPENDENTE\n5 - CITTA' ".encode())
        risp=conn.recv(1024).decode()
        while int(risp) <= 0 or int(risp) >8 :
            conn.send("SELEZIONA IL PARAMETRO CHE VUOI CAMBIARE: \n1 - ID ZONA \n2 - NOME ZONA\n3 - NUMERO_CLIENTI\n4 - ID DIPENDENTE\n5 - CITTA' ".encode())
            risp=conn.recv(1024).decode()
        cos=""
        a=""
        risp=int(risp)
        if risp==2:
            conn.send("Inserisci il nome della nuova zona: ".encode())
            cos=conn.recv(1024).decode()
            a="nome_zona = "+"'"+cos+"'"
        elif risp==3:
            conn.send("Inserisci il nuovo numero clienti: ".encode())
            a="numero_clienti = "+"'"+str(cos)+"'"
        elif risp==4:
            conn.send("Inserisci il nuovo ID dipendente:  ".encode())
            cos=conn.recv(1024).decode()
            a="id_dipendenti = "+"'"+cos+"'"
        elif risp==1:
            conn.send("Inserisci il nuovo ID della zona: ".encode())
            cos=str(conn.recv(1024).decode())

            a="id_zona = "+"'"+str(cos)+"'"
        elif risp==5:
            conn.send("Inserisci la nuova citta' : ".encode())
            cos=str(conn.recv(1024).decode())
            a="città = "+"'"+str(cos)+"'"
        

        print(a)
        query = (f"UPDATE zone_di_lavoro_sami_hamil SET {a} WHERE {idUtent}")
        print(query)
        cur.execute(query)
        cono.commit()
        dati = "Dati aggiornati correttamente(premi invio per continuare)"
    return dati
def db_I(a,conn):
    cono = mysql.connector.connect(
        host="localhost",
        user="sumi",
        password="hamil1234",
        database="5ATepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )
    cur = cono.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    if a=="C":
        #conn.send("Inserisci il nuovo ID: ".encode())
        #cos=str(conn.recv(1024).decode())
        #id=str(cos)
        conn.send("Inserisci il nuovo nome: ".encode())
        cos=conn.recv(1024).decode()
        nome=str(cos)
        conn.send("Inserisci il nuovo cognome: ".encode())
        cos=conn.recv(1024).decode()
        cognome=str(cos)
        conn.send("Inserisci il nuovo indirizzo: \nVia ".encode())
        cos=conn.recv(1024).decode()
        indirizzo=str(cos)
        conn.send("Inserisci il nuovo numero di telefono: ".encode())
        cos=str(conn.recv(1024).decode())
        while len(cos)!=10:
            conn.send("Inserisci il nuovo numero di telefono: ".encode())
            cos=str(conn.recv(1024).decode())
        telefono=str(cos)
        conn.send("Inserisci la nuova posizione lavorativa: ".encode())
        cos=conn.recv(1024).decode()
        pos_lav=str(cos)
        conn.send("Inserisci la data di assunzione(anno-mese-giorno): ".encode())
        cos=conn.recv(1024).decode()
        d_assunzione=str(cos)
        conn.send("Inserisci la data di nascita(anno-mese-giorno): ".encode())
        cos=conn.recv(1024).decode()
        d_nascita=str(cos)
        

        print(a)
        query = (f"INSERT INTO `dipendenti_sami_hamil` (`id`, `nome`, `cognome`, `indirizzo`, `telefono`, `posizione lavorativa`, `data di assunzione`, `data_di_nascita`) VALUES ('', '{nome}', '{cognome}', '{indirizzo}', '{telefono}', '{pos_lav}', '{d_assunzione}', '{d_nascita}')")
        print(query)
        cur.execute(query)
        cono.commit()
        dati = "Dati inseriti correttamente(premi invio per continuare)"
    if a=="Z":
        #conn.send("Inserisci il nuovo ID della zona: ".encode())
        #cos=str(conn.recv(1024).decode())
        #id_zona=str(cos)
        conn.send("Inserisci il nome della nuova zona: ".encode())
        cos=conn.recv(1024).decode()
        nome_zona=str(cos)
        conn.send("Inserisci il nuovo numero clienti: ".encode())
        cos=conn.recv(1024).decode()
        numero_clienti=str(cos)
        conn.send("Inserisci il nuovo ID dipendente:  ".encode())
        cos=conn.recv(1024).decode()
        id_dipendente=str(cos)
        
        conn.send("Inserisci la nuova citta' : ".encode())
        cos=str(conn.recv(1024).decode())
        citta=str(cos)
        

        print(a)
        query = (f"INSERT INTO `zone_di_lavoro_sami_hamil` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendenti`, `città`) VALUES ('', '{nome_zona}', '{numero_clienti}', '{id_dipendente}', '{citta}')")
        print(query)
        cur.execute(query)
        cono.commit()
        dati = "Dati inseriti correttamente(premi invio per continuare)"
    return dati

print("server in ascolto: ")
lock = threading.Lock()
HOST = ''                 # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50010            # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i=0

while True:
    lista_connessioni.append( s.accept() ) #connessione = s.accept() 
    print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) )) 
    thread[i].start()
    i+=1
