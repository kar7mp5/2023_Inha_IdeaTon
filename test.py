import smtplib

FROM = 'tommy1005a@gmail.com'
TO = ["tommy1005a@gmail.com"] # must be a list
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib."
PW = "hxzaewtcwtecnteq"

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(FROM, PW)
server.sendmail(FROM, TO, message)
server.quit()
# hxzaewtcwtecnteq
