from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'proibidototal120@gmail.com'
minha_senha = 'Binfae@45'

with open('template.html', 'r') as html:
    tempfile = Template(html.read())
    data_atual = datetime.now().strftime('%d%m%Y')
    corpo_msg = Template.substitute(nome='Hedris', data=data_atual)


msg = MIMEMultipart()
msg['from'] = 'Proibido'
msg['to'] = 'proibidoototal120@gmail.com'
msg['subject'] = 'Eu sei sobre você, não está sozinho'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)




with open('imagem.jpg', 'r') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso..')
    except Exception as e:
        print('E-mail não enviado..')




