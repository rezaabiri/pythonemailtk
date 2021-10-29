# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import smtplib

root = Tk()

root.title("Send email")
root.geometry("475x240+450+260")
root.iconbitmap(r'email.ico')
root.resizable(0, 0)

lbl_home1 = Label(root, text="Subject", font= "naznin 10 bold")
lbl_home1.place(x =40, y =10)

sub = Entry(root,width='30')
sub.place(x = 45, y = 35)

lbl_home5 = Label(root, text="Email body", font= "naznin 10 bold")
lbl_home5.place(x =42, y =58)

body= Text(root , width = 23 , height = 5)
body.place(x = 45, y = 80)

Email_send = Label(root, text="Sender", font= "naznin 10 bold")
Email_send.place(x =240, y =10)

sender = Entry(root,width='30')
sender.place(x = 245, y = 35)
sender.insert(0, 'info@gmail.com')

pass_e = Label(root, text="Password", font= "naznin 10 bold")
pass_e.place(x =240, y =58)

password_e = Entry(root,width='30', show = '*')
password_e.place(x = 245, y = 80)

Email_get = Label(root, text="Recevier", font= "naznin 10 bold")
Email_get.place(x =240, y =122)

recevier = Entry(root,width='30')
recevier.place(x = 245, y = 145)
recevier.insert(0, 'info2@gmail.com')

l = Label(root, text = '', font = 'aria 12 bold', fg = '#2eb82e')
l.place(x=285,y=195)

def run():
   def sendmail(from_addr, to_addr_list, cc_addr_list, subject,message,login, password, smtpserver="smtp.gmail.com:587"):

      header = "From %s\n" %from_addr
      header += "To: %s\n" % ",".join(to_addr_list)
      header += "CC: %s\n" % ",".join(cc_addr_list)

      header += "Subject: %s\n" % subject
      message = header + message
      
      server = smtplib.SMTP(smtpserver)
      server.starttls()
      server.login(login, password)
      problems = server.sendmail(from_addr, to_addr_list, message)
      server.quit()
    
      l.config(text = "Email sent!")

      return problems

   subj = str(sub.get())
   bod = str(body.get(1.0, END))

   sender_email = str(sender.get())
   password_email = str(password_e.get())

   recevier_email = str(recevier.get())


   sendmail(from_addr    =    sender_email,

            to_addr_list = [recevier_email],
            cc_addr_list = [""],
            subject         = subj,
            message     = bod,
            login             = sender_email,
            password     = password_email)

        
b1=ttk.Button(root,text="Send email", command = run).place(x=140,y=196)
b2=ttk.Button(root,text="Cancel", command = root.destroy).place(x=60,y=196)

root.resizable(False, False)

root.mainloop()
