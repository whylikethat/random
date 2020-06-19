import smtplib, ssl

message = "\n"
f = open("new.txt", "rb")
message += f.read()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("psylock2015@gmail.com", "ldippnffmhsyavjj")
server.sendmail("psylock2015@gmail.com", "doemae19@gmail.com", message) 
server.quit()

f.close()
