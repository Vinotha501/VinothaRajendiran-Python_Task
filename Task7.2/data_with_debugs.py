# Debugging the data

import csv
import logging

# Configure logging
logging.basicConfig(filename="pipeline.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def read_csv(file_path):
    data=[]
    try:
        with open (file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not any(row):  # Debug : Handles empty rows properly
                    logging.warning("Empty row encountered!")
                    continue # skip empty row
                data.append(row)
    except FileNotFoundError:
        logging.error(f"Error: File {file_path} not found!")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
    return data

def process_data(data):
    processed = []
    for row in data:
        if not any(row):
            continue  # skip empty row in the processing
        try:
             # Fix: Cleaned rows to handle extra commas and space
             result = sum([int(item) for item in row if item.strip()])
             processed.append(result)
        except ValueError as e:
            logging.error(f"ValueError: Could not process row{row}. Exception: {e}")
            processed.append("")
    return processed

def write_csv(file_path, data):
    with open (file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Processed result:"])
        for row in data:
            writer.writerow([row])

def main():
    input_path = "data.csv"
    output_path = "Processed_data.csv"

    data = read_csv("data.csv")
    if data:
        processed_data = process_data(data)
        write_csv(output_path, processed_data)

    else: 
        logging.warning("No data to process.")

if __name__ == '__main__':
    main()
