#!/usr/bin/python
#Pegasus Spikey
#Developed by Muhammad Sobri Maulana
#Author : Pegasus Hacker
#Copyright : Pegasus
#Version : 1.1

import getpass
from spammer import spam_mail

print '\nSCRIPT OUTPUT INFO : '
print '\'->\' before an output indicates it is a non-verbose log'
print '\'!>\' before an output indicates it is a verbose log'
print '\'~>\' before an output indicates it is an error log'
print '\'?>\' before an output indicates it is an input'
print '\n--------------------------------------------------'

#My Publicity :) :)
print '\n-> Pegasus Spiker'
print '-> Developed by Muhammad Sobri Maulana'
print '-> Copyright : Pegasus'
print '\n----------------------------------------------------'
mlserve = raw_input ('?> Service Provider ? (gmail/yahoo) : ')
reci = raw_input('?> Recipient\'s Email: ')
username = raw_input('?> Sender\'s Email : ')
password = getpass.getpass('?> Sender\'s Password: ')
y = raw_input('?> Do you want to include a predefined subject ? (y/n)')
set_sub = 0
if y=='y':
	subject = raw_input('?> Subject: ') 
	set_sub = 1

message_body = raw_input('?> Message: ')
files = []
y3 = raw_input('?> Do you want to attach files ? (y/n) ')
if y3=='y':
	no = input('?> Enter Number of Files to Attach ? ')
	for i in range(1,no+1):
		prompt = '?> Enter Filename#'+str(i)+' with path ? '
		files.append(raw_input(prompt))
number = input('?> Number of messages to send: ')
spam_mail(reci,username,password,message_body,mlserve,number,set_sub,files)