import pandas as pd

def preprocess_csv_for_llm(csv_file, output_file):
    """
    Preprocesses packet data from a CSV file and formats it for LLM training.

    Args:
        csv_file (str): Path to the input CSV file.
        output_file (str): Path to save the processed text-based dataset.
    """
    try:
        # Load the CSV data
        df = pd.read_csv(csv_file)
        
        # Normalize data
        def normalize_ip(ip):
            return ".".join([f"{int(octet):03}" for octet in ip.split(".")]) if isinstance(ip, str) else "UNKNOWN"
        
        df['Source IP'] = df['Source IP'].apply(normalize_ip)
        df['Destination IP'] = df['Destination IP'].apply(normalize_ip)
        
        # Format rows into sequential text for LLM
        formatted_data = []
        for _, row in df.iterrows():
            protocol = row['Protocol']
            time = pd.to_datetime(row['Time'], unit='s').strftime('%Y-%m-%d %H:%M:%S')
            source = f"{row['Source IP']}:{row['Source Port']}" if not pd.isna(row.get('Source Port')) else row['Source IP']
            destination = f"{row['Destination IP']}:{row['Destination Port']}" if not pd.isna(row.get('Destination Port')) else row['Destination IP']
            length = row['Length']
            payload = row.get('Info', "No payload")
            
            formatted_data.append(f"[{time}] Protocol {protocol} packet from {source} to {destination} of length {length} with payload: \"{payload}\"")

        # Save to a text file
        with open(output_file, "w") as outfile:
            outfile.write("\n".join(formatted_data))

        print(f"Processed dataset saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")

# Input and output file paths
csv_file_path = r"csv file path"
output_file_path = r"output file formatted_dataset.txt"

# Run the preprocessing function
preprocess_csv_for_llm(csv_file_path, output_file_path)
