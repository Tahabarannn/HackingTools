from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

eth = Ether()
arp = ARP()

eth.dst = "ff:ff:ff:ff:ff:ff"
arp.pdst = "10.10.10.1/24"

bcPckt = eth/arp
#bcPckt.show()

ans,unans = srp(bcPckt, timeout=3)
#ans.summary()
print("#"*30)
#unans.summary()

for snd,rcv in ans:
    #rcv.show()
    print(rcv.psrc, ":", rcv.src)