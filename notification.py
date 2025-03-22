import smtplib, ssl

message = "\n"
f = open("new.txt", "rb")
message += f.read()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Replace with your own providers information
server.login("psylock2015@gmail.com", "ldippnffmhsyavjj") # Replace with your own credentials for sender
server.sendmail("psylock2015@gmail.com", "doemae19@gmail.com", message) # Replace with your own credentials, the first e-mail is the sender and the second is the recepient
server.quit()

f.close()
