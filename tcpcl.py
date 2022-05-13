
import socket
host = socket.gethostname() 
port = 5057

client_socket = socket.socket()  
client_socket.connect((host, port))  

connected = True

def client_program():
   

    while connected :

    
        print("W E L C O M E")
        nocompte = input("Enter your account  number : ")
        client_socket.send(( nocompte).encode("utf-8"))
        reponse = client_socket.recv(255).decode("utf-8")
        if reponse == 'Accepted' :
            menuClient()

    client_socket.close()  # close the connection








def menuClient() :
 

  ans=True
  while ans:
      print ("""
           =================================================
           =================================================
           ==               W E L C O M E                 ==
           =================================================
           =================================================
           ==         1.Check your balance                ==
           ==                                             ==
           ==         2.Consult your invoices             ==
           ==                                             ==
           ==         3. Make a transaction               ==
           ==                                             ==
           ==         4.Exit/Quit                         ==     
           ==                                             ==
           =================================================
           =================================================
      """)


      ans=input("What would you like to do? ") 
      if ans=="1": 
          client_socket.send(( 'solde').encode("utf-8"))
          print("\n \t   **** BIENVENUE DANS VOTRE COMPTE ****") 
      elif ans=="2":
         print("\n \t   **** VOS FACTURES ****") 
      elif ans=="3":
        print("\n \t   **** TRANSACTIONS ****") 
        print ("""

           =================================================
           =================================================
           ==               W E L C O M E                 ==
           =================================================
           =================================================
           ==         1.Withdraw                          ==
           ==                                             ==
           ==         2.Deposit                           ==
           ==                                             ==
           ==         4.Exit/Quit                         ==     
           ==                                             ==
           =================================================
           =================================================
      """)
        rep=input("What would you like to do? ") 
        if rep =="1" :
            client_socket.send(('r').encode("utf-8"))
            montant = input("Give amount :")
            client_socket.send((montant).encode("utf-8"))

        elif rep=="2":
            client_socket.send(('ver').encode("utf-8"))
            montant = input("Give amount :")
            client_socket.send((montant).encode("utf-8"))

        elif rep =="3":    
            print("\n Goodbye") 
        elif ans !="":
             print("\n Not Valid Choice Try again") 





#Menu principale
if __name__ == '__main__':
    client_program()
