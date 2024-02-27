import smtplib

def criando_notificacao():
    try:
        servidor_email = smtplib.SMTP('smtp.gmail.com',587)
        servidor_email.starttls()
        servidor_email.login('joaquimfreitasdoprado@gmail.com', 'fnor ggov vdde hdha ' )

        remetente = "joaquimfreitasdoprado@gmail.com"
        destinatario = "joaquimfreitasdoprado@gmail.com"
        conteudo = '''
        Oi joaquim! Sou eu, a ALONGANET
        
            Estou passando aqui para te lembrar fazer um alongamento. Sei que voce esta sentado a bastante tempo.
            Recomendo voce a dar uma pausa agora, se alongar, fazer as necessidades e beber agua.
        
        Ate breve e se cuide!
        '''

        servidor_email.sendmail(remetente,destinatario,conteudo)
        servidor_email.quit()
        print("enviado com sucesso!")
    
    except Exception as erro:
        print(f"erro ao enviar e-mail: {erro}")

criando_notificacao()