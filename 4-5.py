import re

email_file = 'email.txt'

def read_from_file(name):
   with open(name, "r", encoding="utf-8") as file:
      content = file.read()
   return content


content = read_from_file(email_file)

def email_sender(email):
   return re.findall(r'From: .*(<.*>)', email)

def email_recipient(email):
   return re.findall(r'To: .*(<.*>)', email)

def email_subject(email):
   return re.findall(r'Subject: (.*)', email)

def email_body(email):
   return re.findall(r"\r?\n\r?\n(.*)", email, re.DOTALL)
