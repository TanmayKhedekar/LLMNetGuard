from scapy.all import sniff
import requests

def monitor_packet(packet):
    info = str(packet.summary())
    response = requests.post("http://127.0.0.9:2005/predict/", json={"text": info})
    print(f"Packet Info: {info} | Prediction: {response.json()}")

sniff(prn=monitor_packet, count=10)  # Adjust count for real-time capture
