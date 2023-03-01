from winotify import Notification, audio #Biblioteca para notificações do Windows
from twilio.rest import Client #API para mandar o SMS
from configparser import ConfigParser #Biblioteca para utilizar o arquivo de configuração
import logging

#Cria o objeto de log
logger = logging.getLogger('my_logger')
#Configura o nível de log
logger.setLevel(logging.INFO)
#Cria arquivo handler
handler = logging.FileHandler('Insira aqui o diretorio do arquivo de log\\log_file.log')
#Define o formato do log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
#Define o formato do log para o handler
handler.setFormatter(formatter)
#Adiciona o handler ao logger
logger.addHandler(handler)



def SendMessage(): #Função para mandar o SMS
    try:
        account_sid = 'ACe98f984026fc6fde79bb52efb7b8f503'
        auth_token = 'a4f8737cb2f427038db7226c9c7df43f'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body= texto,
                from_ = '+18139454576',
                to = Numero)
        resposta = message
        logger.info(f"SMS enviado com sucesso - {resposta}")
    except Exception as e:
        logger.error("Erro ao mandar o SMS.")


#Administração do arquivo .cfg
config_object = ConfigParser()
config_object.read(f"Insira aqui o diretorio do arquivo .cfg\\dados.cfg")
DADOS = config_object["DADOS"]
Numero = DADOS["Numero"]
Titulo = DADOS["Titulo"]
Link = DADOS["Link"]
Arquivo = DADOS["Arquivo"]
txt = DADOS["txt"]

#Lê o arquivo txt e guarda seu conteúdo em uma variavel
with open(txt) as t:
    texto = t.read()
    t.close()

try:
    #Corpo da notificação
    toast = Notification(app_id="BANCAMAIS",
                title= Titulo,
                msg= texto,
                icon="Insira aqui o diretorio do arquivo .png\\BM.png") #Path do ícone

    #Audios da notificação
    toast.set_audio(audio.Reminder, loop=False) #Som Recordatorio
        #toast.set_audio(audio.Default, loop=False) #Som Windows
        #toast.set_audio(audio.SMS, loop=False) #Som SMS
        #toast.set_audio(audio.Mail, loop=False) #Som Mail

    #Botão para abrir arquivo            
    toast.add_actions(label="Abrir Arquivo",
                    launch= Arquivo) #Path do arquivo a ser aberto
    #Botão para abrir site
    toast.add_actions(label="Abrir Site",
                    launch= Link) #Link do site a ser aberto

    #Aciona a função para mandar o SMS
    toast.show()
except Exception as x:
    logger.error(f"Erro ao mostrar a notificação.")

#Aciona a função para mandar o SMS
SendMessage()