from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

# callback function
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # protocol type
        if protocol == 1:
            protocol_name = "ICMP"
        elif protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Unknown Protocol"

        # details
        print(f"Protocol: {protocol_name}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

        # payload
        if Raw in packet:
            payload_data = packet[Raw].load
            print(f"Payload: {payload_data}")
        else:
            print("No Payload.")

        print("-" * 50)

sniff(prn=packet_callback, store=False)
