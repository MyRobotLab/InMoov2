## this need to be modified for multi language
## currently only works with the fr-FR bot
import imaplib
import re
import email
import smtplib
from email import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import *
from email import encoders
from email.mime.base import *

expediteur =  "xxxxxxxxxxx@xxxxxxx"
serveursmtp = 'smtp-msa.orange.fr'
port = 587
password = "xxxxxxxxxxxxxxxxxx"
serveurimap = 'imap.orange.fr'

def mailsend(amis,message):
	try:
		# si base de donnees existe
		if os.path.exists('data/bdamis.csv'):
			flag = 0
			f = open('data/bdamis.csv', 'r')
       		 # lecture du fichier CSV.
			reader = csv.reader(f,delimiter=";")
	    	# Boucle lecture lignes une par une colonne 0 (champ nom).
			for ligne in reader:
				if (amis.upper() == ligne[0]):
					flag=1
					i01.speakBlocking( amis + " fais parti de tes amis ")
					message = message.strip("Si ok")[:-22]
					envoi(message,ligne[5]) # champ adresse dans bd
			f.close() 	
			if flag==0 :
				i01.speakBlocking(amis + u" n'existe pas dans mon annuaire" )
   
		else : 
      		# la bd des amis n existe pas
			i01.speakBlocking(u"tu dois d'abord créer ton annuaire d'amis . Dis ANNUAIRE pour le créer")
       
	except IOError:
		i01.speakBlocking("le serveur est hors service , mail non transmis")
	except OSError:
		i01.speakBlocking("oups il y a une erreur")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise



def envoi(message,adresse):
	try:
		codage = 'UTF-8' # <= modif
		msg = MIMEMultipart()
		msg['From'] = expediteur
		msg['To'] = adresse
		msg['Subject'] = "Message de InMOOV"
		msg['Charset'] = codage  # <= modif
		msg['Content-Type'] = 'text/plain; charset=UTF-8' # <--modif
		body = message
		typetexte = 'plain'
		msg.attach(MIMEText(body, typetexte, 'UTF-8')) # <= modif
		#msg.attach(MIMEText(body, 'text/plain'))
		# valeur du serveur smtp securise ou pas
		#server = smtplib.SMTP('smtp.gmail.com', 587)
		server = smtplib.SMTP(serveursmtp, port)
		#server.starttls()
		server.login(expediteur, password)
		text = msg.as_string()
		server.sendmail(expediteur, adresse, text)
		sleep(3)
		i01.speakBlocking("mel transmis a " + adresse)
		server.quit()
		server.close()
	
	except IOError:
		talk("le serveur est hors service , mail non transmis")
	except OSError:
		i01.speakBlocking("oups il y a une erreur")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

def liremail(destinataire):
	try :
		# si base de donnees existe
		if os.path.exists('data/bdamis.csv'):
			flag=0
			f = open('data/bdamis.csv', 'r')
       		# lecture du fichier CSV.
			reader = csv.reader(f,delimiter=";")
	    	# Boucle lecture lignes une par une colonne 0 (champ nom).
			for ligne in reader:
				if (destinataire.upper() == ligne[0] and ligne[5] != ""):
					flag = 1
					mail = imaplib.IMAP4_SSL(serveurimap)
					# imaplib module implements connection based sur protocol IMAPv4 
					mail.login(expediteur, password)
					mail.list() 
					mail.select('inbox') # Connecter a inbox.
					(status,nbMessages) = mail.select('INBOX')
					print("connecter inbox")
					
					#Rechercher message dans expediteur
					result, data = mail.uid('search', None, '(FROM "'+ligne[6]+'")')
					i = len(data[0].split()) # data[0] supprime espace
					Totalmsg = re.findall('\d+', str(nbMessages))[0]
					print (result + ' Nombre de messages = ' + str(Totalmsg))
					i01.speakBlocking(u"il y a  au total "+str(Totalmsg)+ " messages dans ta boite mail ")
					print("trouver : " +str(i))
					i01.speakBlocking(u"jai trouver " + str(i) + " message de " + destinataire )

					for x in range(i):
						latest_email_uid = data[0].split()[x] # ID unique étiquette sélectionnée
						result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
						# Récupérer le corps de courrier électronique pour l'ID donné
						raw_email = email_data[0][1]

						# boucle 1 
						raw_email_string = raw_email.decode('utf-8')
						# Convertit  d'octet en chaîne 
						email_message = email.message_from_string(raw_email_string)

						#boucler à travers toutes les multiparties disponibles dans le mail
						for part in email_message.walk():
							if part.get_content_type() == "text/plain": # ignore html
								body = part.get_payload(decode=True)
								print(body.decode('utf-8'))
								Mreponse = (body.decode('utf-8'))
								i01.speakBlocking(u"message " + str(x+1) +". "+ Mreponse)
							if part.get_content_type() == "multipart/mixed" : # ignore piece jointe
								body = part.get_payload(decode=False)
							else:
								continue
				
					if i == 0 :
						print("pas de messages")
						sleep(4)
						i01.speakBlocking("a bientot")
						
					#fermeture IMAP
					print ("deconnecter du serveur")
					imaplib.IMAP4.close
					imaplib.IMAP4.logout
			if flag == 0 :
			    # message si pas trouver dans l annuaire
				i01.speakBlocking(u"personne inconnu dans mon annuaire ou le mail et aiedi ,ne sont pas renseigné")
       
		
		else : # la bd des amis n existe pas
			i01.speakBlocking(u"tu dois d'abord créer ton annuaire d'amis . Dis ANNUAIRE pour le créer")
   
		
	except IOError:
		i01.speakBlocking("le serveur est hors service")
	except OSError:
		i01.speakBlocking("oups il y a une erreur")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

