#importing libraries 
import smtplib
import time
import email
import imaplib
import traceback

#for log in in the email
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "rockybhai0707" + ORG_EMAIL
# with open('password.txt') as file:
#     FROM_PWD = file.read().split("\n")[0]
FROM_PWD = "rocky0707"
SMTP_SERVER =  "imap.gmail.com"
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        #connect server using server and port number also login using email and passwd
        mail = imaplib.IMAP4_SSL(SMTP_SERVER,SMTP_PORT)
        mail.login(FROM_EMAIL,FROM_PWD)
        
        mail.select('inbox')
        data = mail.search(None,'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print(latest_email_id)

        for (index,i) in enumerate(range(latest_email_id,first_email_id,-1)):
            data = mail.fetch(str(i),'(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr,tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    print(msg.keys())
                    email_subject = msg['subject']
                    email_from = msg['from']
                    date = msg['date']
                    # print("date: ",date,'\n')
                    # print(index+1,'From : ' + email_from + '\n')
                    # print('Subject : ' + str(email_subject) + '\n')
                    print("-"*15)
                    print(msg['Received'])
                    print("-"*100)

            if index > 3:
                break

    except Exception as e:
        traceback.print_exc()
        print(e)

read_email_from_gmail()