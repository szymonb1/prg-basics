import re
with open(r"prg-basics\08-FileHandling\email.txt", 'r') as f:
    content = f.read()

def email_sender():
    email_sender = re.findall(r"From:\s\w+\s\w+\s\<(.+@[a-z]+\.[a-z]+)>", content)
    return email_sender
def email_recipient():
    email_recipient = re.findall(r"To:\s\w+\s\w+\s\<(.+@[a-z]+\.[a-z]+)>", content)
    return email_recipient
def subject():
    subject = re.findall("Subject: (.+)\n", content)
    return subject
def email_body():
    email_body = re.findall()


print(email_sender())
print(email_recipient())
print(subject())