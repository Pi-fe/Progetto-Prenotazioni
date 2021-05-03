

class Utente():
    
    def __init__(self,nome,cognome,indirizzo,cf,password,privacy,email,numero):
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo
        self.cf = cf
        self.password = password
        self.privacy = privacy
        self.email = email
        self.numero = numero

    def stampa(self):
        print("Nome: \t%s \nCognome: %s \nIndirizzo: %s \nCodice Fiscale: %s \nEmail: %s \nNumero: %s \nPassword: ******" % (self.nome,self.cognome,self.indirizzo,self.cf,self.email,self.numero))

    def modificaPw(self,oldPassword, newPassword):
        if(self.password == oldPassword):
            self.password = newPassword
            print("Password modificata con successo! password: %s"% self.password)
        else:
            print("Passowrd Errata!")
    def registrazione(self,lista):
        lista.append(self)
        print("Registrazione Effettuata!")


class Messaggio():

    def __init__(self,contenuto,utente):
        self.contenuto = contenuto
        self.utente = utente
    
class Sms(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.numero = self.utente.numero

    def invia(self):
        print("Messaggio: %s\nNumero: %s" % (self.contenuto,self.numero))


class Email(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.email = self.utente.email   


class Tavolo():

    def __init__(self,id_tavolo,nmax):
        self.id_tavolo = id_tavolo
        self.nmax =  nmax
        self.calendario = {}


    def prenota(self,utente,npersone,data_ora):
        self.numero

class Tavolo():

    def __init__(self,id_tavolo,n_max):
        self.id_tavolo = id_tavolo
        self.n_max = 4
        self.prenotazioni = {}

    def prenota(self,utente,n_persone,data,ora):
        if (0 < n_persone <= self.n_max):
            self.prenotazioni[data]=ora           
            print("\nPrenotazione effettuata a nome di %s , per %d persone.\nData e ora: %s ." %(utente.nome.title()+" "+utente.cognome.title(),n_persone,data+" "+ora))
            for key, value in self.prenotazioni.items():
                print("Data: " + key)
                print("Ora: " + value)
        else:
            print("TAVOLO GIA PRENOTATO O N. PERSONE SUPERIORE A 4 !")
              

    def prenotato(data,ora):
        if 

class Tavolo():

    def __init__(self,id_tavolo,nmax=4):
        self.id_tavolo = id_tavolo
        self.nmax = nmax
        self.prenotato = False


#Funzione di prenotazione semplice (singola prenotazione per tavolo)
    def prenota(self,utente,npersone,data_ora):
        if (0 < npersone <= self.nmax and self.prenotato == False):
            self.prenotato = True
            self.npersone = npersone
            self.utente = utente
            self.data_ora = data_ora
            print("Prenotazione effettuta a nome di : %s \n per numero di persone: %d \n data e ora: %s"% (self.utente.nome+" "+self.utente.cognome,self.npersone,self.data_ora))
        else:
            print("Il tavolo è già prenotato o il numero di persone è superiore a 4 !")
    






#FILE Prenotazione db
'''
    def stampa(self):
        print("Nome: \t%s \nCognome: %s \nIndirizzo: %s \nCodice Fiscale: %s \nEmail: %s \nNumero: %s \nPassword: ******" % (self.nome,self.cognome,self.indirizzo,self.cf,self.email,self.numero))

    def modificaPw(self,oldPassword, newPassword):
        if(self.password == oldPassword):
            self.password = newPassword
            print("Password modificata con successo! password: %s"% self.password)
        else:
            print("Passowrd Errata!")
    def registrazione(self,lista):
        lista.append(self)
        print("Registrazione Effettuata!")
'''




'''
class Messaggio():

    def __init__(self,contenuto,utente):
        self.contenuto = contenuto
        self.utente = utente
    
class Sms(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.numero = self.utente.numero

    def invia(self):
        print("Messaggio: %s\nNumero: %s" % (self.contenuto,self.numero))


class Email(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.email = self.utente.email   
'''



'''
ListaUtenti = []
myUtente = Utente("Pietro","Ferrulli","Via Roma 123","FRRPTR123123123123","pippo123",True,"pppp@outlook.it","346123456")
myTavolo = Tavolo(1,4)
myTavolo.prenota(myUtente,3,"27/04/2021 12:00")
'''

'''
myUtente2 = Utente("Mario","Rossi","Via Lazo 321","RSSMR123123123123","pippo123",True,"mrmr@outlook.it","3463213213216")
myUtente.stampa()
myUtente.registrazione(ListaUtenti)
myUtente2.registrazione(ListaUtenti)
myUtente.modificaPw("pippo123","Password123")
mess_num = Sms("Contenuto",myUtente)

print("--------------------------------------------")

for utente in ListaUtenti:
    utente.stampa()
'''












ListaUtenti = []
myUtente = Utente("Pietro","Ferrulli","Via Roma 123","FRRPTR123123123123","pippo123",True,"pppp@outlook.it","346123456")
myTavolo = Tavolo(1,4)
myTavolo.prenota(myUtente,3,"27/04/2021 12:00")

'''
myUtente2 = Utente("Mario","Rossi","Via Lazo 321","RSSMR123123123123","pippo123",True,"mrmr@outlook.it","3463213213216")
myUtente.stampa()
myUtente.registrazione(ListaUtenti)
myUtente2.registrazione(ListaUtenti)
myUtente.modificaPw("pippo123","Password123")
mess_num = Sms("Contenuto",myUtente)

print("--------------------------------------------")

for utente in ListaUtenti:
    utente.stampa()
'''