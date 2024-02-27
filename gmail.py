import smtplib   #biblioteca necessaria para trabalhar com e-mail automatico, de baixo idem, o nome ja diz!
import email.message

def enviar_email():  
   
    #codigo padrao, mas vamos entender ele. Estamos construinda atraves de uma def funçoes, ou seja, o caminho ate o envio do e-mail
    #primeiro, vamos contruir o corpo do e-mail:
   
    corpo_email = """
    <p></p> Vamos alongar! 
    <p></p> ta doendo né?! Levante e alongue-se    
    """
#ja esta em string, olhar inicio, por isso n precisa das aspas
   
    msg = email.message.Message()
   #chamando o import
    
    #chamando o import e add as partes do email para preencher os campos titulo, de , para(se vc para si proprio so repetir os emails)
    msg['Subject'] = "lembrete de alongamento"
    msg['From'] = 'joaka6499@gmail.com'
    msg['To'] = 'joaka6499@gmail.com'
   
    #essa senha é gerada no gerenciador de contas google do e-mail
    password = 'pgyz dxqr uedu tfok ' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()
