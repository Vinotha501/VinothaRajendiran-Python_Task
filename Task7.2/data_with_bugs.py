# Python code with bugs in the data processing

import csv
import logging

# Configure logging
logging.basicConfig(filename="pipeline.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def read_csv(file_path):
    data = []
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:  # Bug : The code fails to handle empty rows properly.
                  logging.warning("Empty row encountered!")
                data.append(row) 
    except Exception as e:
       logging.error(f"Error reading file{file_path}: {e}")
    return data

def process_data(data):
    processed = []
    for row in data:
        try:
             # Bug: Some extra empty values from rows with extra commas might be included.
            result = sum([int(item) for item in row if item.strip()])
            processed.append(result)
        except ValueError:
            logging.error(f"ValueError: Could not process row {row}")
            processed.append(None)
    return processed

def write_csv(file_path, data):
    with open (file_path, 'w', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(["Processed results"])
        for row in data:
            writer.writerow([row])


data = read_csv("data.csv")
if data:
    processed_data = process_data(data)  # Bug: overwriting the function with processed results
    write_csv("Processed_data.csv", processed_data)  
else:
    logging.error("No data to process.")