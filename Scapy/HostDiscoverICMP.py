from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

ip = IP()
icmp = ICMP()

pingPckt = ip/icmp

addr = "10.10.10."
ipList = []

for i in range(256):
    pingPckt[IP].dst=addr+str(i)
    #print(pingPckt[IP].dst)
    response = sr1(pingPckt, timeout=0.3, verbose=False)
    #print(response)

    if(response):
        #print(pingPckt[IP].dst,"is up")
        ipList.append(pingPckt[IP].dist)
    else:
        pass

print(ipList)