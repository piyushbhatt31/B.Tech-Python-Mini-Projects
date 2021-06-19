import smtplib 
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'xyz name'
email['to'] = 'xyz id'
email['subject'] = 'xyz subject'
email.set_content("Xyz content of email")
with smtlib.SMTP(host='smtp.gmail.com',port=587)as smtp:     
    smtp.ehlo()        
smtp.starttls()   
smtp.login("email_id","Password") 
smtp.send_message(email)  
print("email send")  
