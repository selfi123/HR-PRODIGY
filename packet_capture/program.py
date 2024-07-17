from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_details(packet):
    if packet.haslayer(IP):
        ip_src=packet[IP].src
        ip_dst=packet[IP].dst
        protocol=None
        if packet.haslayer(TCP):
            protocol="TCP"
            payload=bytes(packet[TCP].payload)
        elif packet.haslayer(UDP):
            protocol="UDP"
            payload=bytes(packet[UDP].payload)
        elif packet.haslayer(ICMP):
            protocol="ICMP"
            payload=bytes(packet[ICMP].payload)
        else:
            protocol=packet[IP].proto
            payload=bytes(packet[IP].payload)

        print(f"IP {ip_src}->{ip_dst} | Protocol: {protocol} | Payload: {payload}")

sniff(filter="ip",prn=packet_details)
