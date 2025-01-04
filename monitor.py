import requests
from scapy.all import sniff

def monitor_packet(packet):
    info = str(packet.summary())  # Extract packet details
    print(f"Captured Packet: {info}")
    
    try:
        # Send packet info to the API as JSON
        response = requests.post(
            "http://127.0.0.1:8000/predict/",
            json={"text": info},  # Ensure 'text' is part of the JSON body
            headers={"Content-Type": "application/json"}  # Explicitly set headers
        )
        
        if response.status_code == 200:  # Check for a successful response
            response_data = response.json()  # Parse JSON response
            prediction = response_data.get("predicted_label")  # Extract prediction
            
            if prediction is not None:
                # Check if the packet is suspicious
                if prediction == 0:  # Example: Non-TCP classified as suspicious
                    print(f"ALERT: Suspicious packet detected: {info}")
                else:
                    print(f"Packet is normal: {info}")
            else:
                print(f"Prediction missing in API response: {response_data}")
        else:
            print(f"API returned an error: {response.status_code}, {response.text}")
    
    except Exception as e:
        print(f"Error during API call or processing: {e}")

# Capture packets (adjust count for real-time monitoring)
sniff(prn=monitor_packet, count=10)
