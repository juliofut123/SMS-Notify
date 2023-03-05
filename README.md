Script de envio de notificação e SMS
Este script em Python utiliza a biblioteca winotify para notificações no Windows e a API Twilio para enviar mensagens SMS. O script também usa a biblioteca ConfigParser para ler de um arquivo de configuração.

Pré-requisitos
Antes de executar este script, certifique-se de instalar as bibliotecas necessárias executando:
pip install winotify twilio configparser

Configuração
Este script requer um arquivo de configuração chamado dados.cfg no mesmo diretório que o script. O arquivo de configuração deve ter as seguintes chaves:

Numero: O número de telefone para o qual a mensagem SMS será enviada.
Titulo: O título da notificação.
Link: O link para abrir quando o botão "Abrir Site" for clicado.
Arquivo: O caminho para o arquivo a ser aberto quando o botão "Abrir Arquivo" for clicado.
txt: O caminho para o arquivo de texto contendo a mensagem a ser enviada na SMS.

Uso
Para usar este script, basta executá-lo usando o Python:
python notification_sms_sender.py

Logging
Este script registra eventos em um arquivo chamado log_file.log no mesmo diretório que o script. O arquivo de log incluirá informações sobre quando a SMS foi enviada com sucesso, bem como quaisquer erros que ocorreram.

Nota
Por favor, observe que o SID da conta Twilio e o token de autenticação precisarão ser alterados na função SendMessage() para corresponder às informações da sua própria conta.
