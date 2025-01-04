####### PCAP file converted into CSV file######################################
from scapy.utils import rdpcap
import csv
from scapy.layers.inet import IP

def pcap_to_csv(pcap_file, csv_file):
    # Load packets from the PCAP file
    packets = rdpcap(pcap_file)

    # Open the CSV file for writing
    with open(csv_file, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the CSV header
        csvwriter.writerow(["Time", "Source IP", "Destination IP", "Protocol", "Length", "Info"])

        # Process each packet
        for pkt in packets:
            if IP in pkt:
                csvwriter.writerow([
                    pkt.time,  # Timestamp
                    pkt[IP].src,  # Source IP
                    pkt[IP].dst,  # Destination IP
                    pkt[IP].proto,  # Protocol
                    len(pkt),  # Length
                    pkt.summary()  # Info
                ])

# Replace with your PCAP file path and desired output file path
pcap_file_path = r"Path_of_your_PCAP"
csv_file_path = r"Path_of _your_CSV"

pcap_to_csv(pcap_file_path, csv_file_path)
