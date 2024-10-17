# File Processing System
import csv
import json
import xml.etree.ElementTree as ET
import os

# exception for unsupported file formats
class UnsupportedFileFormatError(Exception):
    pass

# filtering condition
def filter_condition(row):
    try:
        return int(row.get('age', 0)) > 30
    except ValueError:
        return False
    
# Process csv file
def process_csv(input_path, output_path):
    print(f"Processing csv file: {input_path}")

    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)  
        
            writer.writeheader()  # Write header to output file
        
            for row in reader:
              if filter_condition(row):  # Apply your filtering condition here
                 writer.writerow(row)

        print(f"Filtered data has been written to {output_path}.")
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except Exception as e:
        print(f"Error processing csv file: {str(e)}")


# process json file
def process_json(input_path, output_path):
    print(f"Processing json file: {input_path}")

    try:
        with open(input_path, mode='r', encoding='utf-8') as infile, \
            open(output_path, mode='w', encoding='utf-8') as outfile:
        
            data = json.load(infile)
            filtered_data = [item for item in data if filter_condition(item)]
            json.dump(filtered_data, outfile, indent=4)

        print(f"Filtered data has been written to {output_path}.")
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{input_path}'.")
    except Exception as e:
        print(f"Error processing json file: {str(e)}")

# process xml file
def process_xml(input_path, output_path):
    print(f"Processing xml file: {input_path}")

    try:
        tree = ET.parse(input_path)
        root = tree.getroot()

        filtered_root = ET.Element(root.tag) # create a new root for the filtered data

        for elem in root:
            row = {child.tag: child.text for child in elem}
            if filter_condition(row):
               new_elem = ET.SubElement(filtered_root, elem.tag)
               for key, value in row.items():
                   child_elem = ET.SubElement(new_elem, key)
                   child_elem.text = value

        tree = ET.ElementTree(filtered_root)
        tree.write(output_path, encoding='utf-8', xml_declaration=True) # write filtered xml to output

        print(f"Filtered data has been written to {output_path}.")
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except ET.parserError:
        print(f"Error: Invalid xml format in file '{input_path}'.")
    except Exception as e:
        print(f"Error processing xml file: {str(e)}")   
        

# Run the processing system
def process_file(input_path, output_path):
    if input_path.endswith('.csv') and output_path.endswith('.csv'):
       process_csv(input_path, output_path)
    elif input_path.endswith('.json') and output_path.endswith('.json'):
        process_json(input_path, output_path)
    elif input_path.endswith('.xml') and output_path.endswith('.xml'):
        process_xml(input_path, output_path)
    else:
        raise UnsupportedFileFormatError("Unsupported file format. Please provide a CSV, JSON, or XML file.")

# main execution
if __name__ == "__main__":

   input_csv_file = "input.csv"  
   output_csv_file = "output.csv" 

   input_json_file = "input.json"  
   output_json_file = "output.json" 

   input_xml_file = "input.xml"  
   output_xml_file = "output.xml"

# process the file one by one

   try:
       process_file(input_csv_file, output_csv_file)
       process_file(input_json_file, output_json_file)
       process_file(input_xml_file, output_xml_file)

   except UnsupportedFileFormatError as e:
       print (e)

   except Exception as e:
       print (f"An error occured: {str(e)}")