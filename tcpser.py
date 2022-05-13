from array import array
from gettext import npgettext
import socket


import socket

codeCLient =''
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5057  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
      
        elif data == 'solde' :
            print(getSolde(int(codeCLient)))
        
        elif data =='r' :
            rep = conn.recv(1024).decode()
            retrait(int(codeCLient),int(rep))
        elif data =='ver' :
            rep = conn.recv(1024).decode()
            versement(int(codeCLient),int(rep))
        elif verif (data) == 'v' :
            conn.send(('Accepted').encode('utf-8'))
            codeCLient=data

        

    conn.close()
def getSolde(code):
    ListeC = getListeComptes()
    for item in ListeC :
        if code == item.refCompte :
            return item.valeur


def verif(ref):
    v ='f'
    Listec = getListeComptes()
    for item in Listec :
        if item.refCompte == int(ref) :
            v = 'v' 
    return v 


class Compte : 
    def __init__(self ,refCompte, valeur, etat ,Plafond):    
     self.refCompte = refCompte
     self.valeur = valeur
     self.etat = etat
     self.Plafond = Plafond




def getListeComptes() :
    file1 = open('compte.txt', 'r')
    Lines = file1.readlines()
    ListeComptes  =[]

    for line in Lines :
    
        
        ref = int (line.split('-')[0])
        val= int(line.split('-')[1])
        etat = line.split('-')[2]
        plafond = int (line.split('-')[3])
    
        ListeComptes.append(Compte(ref,val,etat,plafond))
   
    return ListeComptes
def viderFichier():
     open('compte.txt', 'w').close()



def writeInFile (Liste) :
    viderFichier()
    f = open('compte.txt', "a")

    for item in Liste :
        line = str(item.refCompte) +'-'+str(item.valeur) +'-' + item.etat +'-' + str(item.Plafond) +'-'+'\n'
        f.write(line)
        

    f.close()
    
   
   


def retrait(ref,montant):
    ListeC = getListeComptes()
    for item in ListeC :
        if item.refCompte == ref :
            item.valeur =item.valeur -montant
            file = open("histo.txt", "w")
            file.write(str(ref) + "-" + "retrait" + "-" + str(montant) + "-" + "succee" +"-" + "negatif")
            file.close
            
    writeInFile(ListeC)


def versement(ref,montant):
    ListeC = getListeComptes()
    for item in ListeC :
        if item.refCompte == ref :
            item.valeur =item.valeur + montant
            file = open("histo.txt", "w")
            file.write(str(ref) + "-" + "versement" + "-" + str(montant) + "-" + "succee" +"-" + "positif")
            file.close
            
    writeInFile(ListeC)


def ConsulterComptes () :
    print('[Ref ,   valeur , etat ,  Plafond ]')
    file1 = open('compte.txt', 'r')
    Lines = file1.readlines()
    for line in Lines :
    
        print(line.split('-'))


if __name__ == '__main__':
    server_program()
