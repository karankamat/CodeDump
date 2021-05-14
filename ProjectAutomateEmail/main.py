import smtplib
import pandas as pd
import random
import datetime as dt

data = pd.read_csv("emails.csv")
EMAIL = //Email
PASSWORD = //yourpassword
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
RECIPIENT = data.mailid.values

with open("Data/quotes.txt", 'r') as file:
    file_data = file.readlines()
    r_quote = random.choice(file_data)
with open("Data/quotes.txt", 'w') as file:
    for line in file_data:
        if line != r_quote:
            file.write(line)
with open("Data/used_quotes.txt", 'a+') as q_file:
    q_file.write(str(r_quote))

message = f"SUBJECT:Greetings!\n\n{r_quote}\n\nRegards\nPyCode"

for recipient in RECIPIENT:
    try:
        connection = smtplib.SMTP(SMTP_SERVER, PORT)
        connection.starttls()
        connection.login(user=EMAIL,
                         password=PASSWORD
                         )
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient, 
                            msg=message,
                            )
        print("Establishing connection...")
    except ConnectionError:
        print("Mail not sent, connection error")
    except TimeoutError:
        print("Mail not sent, time error")
    else:
        pass
    finally:
        print(f"Mail sent. {dt.datetime.now()}")
        connection.close()
