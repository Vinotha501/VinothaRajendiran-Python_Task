# Create a File Parser with Error Handling
import csv
import json
import xml.etree.ElementTree as ET
import logging
import os

# configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# creating csv
def create_csv(file_path):
    data=[
         ["Name", "Age", "Salary", "Department"],
         ["Johnson", 25, 15000, "Teacher"],
         ["Virginia", 30, 25000, "Bank Assistant"],
         ["Shelly", 36, 30000, "Professor"]
    ]

    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except PermissionError:
        logging.error(f"Error: Permission denied when writing to '{file_path}'.")
    except Exception as e:
        logging.error(f"An unexpected error occured while creating csv: {e}")

# creating json
def create_json(file_path):
    data=[
         {"Name": "Johnson", "Age":25, "Salary": 15000, "Department": "Teacher"},
         {"Name": "Virginia", "Age":30, "Salary": 25000, "Department": "Bank Assistant"},
         {"Name": "Shelly", "Age":36, "Salary": 30000, "Department": "Professor"}
    ]

    try:
        with open(file_path, mode='w', ) as file:
            json.dump(data,file, indent = 4)
    except PermissionError:
       logging.error(f"Error: Permission denied when writing to '{file_path}'.")
    except Exception as e:
       logging.error(f"An unexpected error occured while creating json: {e}")

# creating xml
def create_xml(file_path):
    data=[
         {"Name": "Johnson", "Age":25, "Salary": 15000, "Department": "Teacher"},
         {"Name": "Virginia", "Age":30, "Salary": 25000, "Department": "Bank Assistant"},
         {"Name": "Shelly", "Age":36, "Salary": 30000, "Department": "Professor"}
    ]

    root = ET.Element("Employees")
    for emp in data:
        emp_elem = ET.SubElement(root, "Employee")
        for key, value in emp.items():
            child_elem = ET.SubElement(emp_elem, key)
            child_elem.text = str (value)

    try:
       tree = ET.ElementTree(root)
       tree.write(file_path)
    except PermissionError:
        logging.error(f"Error: Permission denied when writing to '{file_path}'.")
    except Exception as e:
        logging.error(f"An unexpected error occured while creating xml: {e}")

# process csv file
def process_csv(file_path):
    try:
    
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader, None)

            if not headers:  
                logging.error(f"Error: The file '{file_path}' is empty.")
                return

            numeric_columns = []
            extracted_data = []

            for row in reader:
                for i, item in enumerate(row):
                    if item.replace('.', '', 1).isdigit():
                        if len(numeric_columns) <= i:  
                            numeric_columns.append([float(item)])
                        else:
                            numeric_columns[i].append(float(item))
                    else:
                        if len(numeric_columns) <= i:
                            numeric_columns.append([])

        # sum the numeric columns
        numeric_columns = [sum(column)  for column in numeric_columns if column]

        # Extract the specific data
        if row [headers.index("Name")] == "Shelly":
            extracted_data.append(row)

        print ("Headers:", headers)
        print("Sum of numeric columns:", numeric_columns)
        print("Extracting specific data:", extracted_data)


    # Error Handling
    except FileNotFoundError:
        logging.error(f"Error: The file '{file_path}' was not found.")

    except PermissionError:
        logging.error(f"Error: Permission denied while trying to write in '{file_path}'")

    except csv.Error as csv_error:
        logging.error(f"Error: Issue with csv file format: {csv_error}")

    except Exception as e:
        logging.error (f"An unexpected error occured: {e}")

# process json
def process_json(file_path):
    try:
        with open(file_path, mode='r') as file:
            data = json.load(file)
            numeric_columns = []
            extracted_data = []

            for emp in data:
                for key in ["Age", "Salary"]:
                    if key in emp:
                        numeric_columns.append(float(emp[key]))

                # Extracting specific data
                if emp["Name"] == "Virginia":
                    extracted_data.append(emp)

            # sum numeric columns
            total_age = sum(emp["Age"] for emp in data)
            total_salary = sum (emp["Salary"] for emp in data)    

            print("JSON total age:", total_age )
            print("JSON total salary:", total_salary )
            print("JSON Extracting specific data:", extracted_data)

    # Error Handling
    except FileNotFoundError:
        logging.error(f"Error: The file '{file_path}' was not found.")

    except json.JSONDecodeError:
       logging.error(f"Error: Issue with JSON format.")

    except PermissionError:
        logging.error(f"Error: Permission denied while trying to write in '{file_path}'")

    except Exception as e:
        logging.error (f"An unexpected error occured: {e}")

# process xml file
def process_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        numeric_columns = []
        extracted_data = []

        total_age = 0
        total_salary = 0

        for emp in root.findall("Employee"):
            emp_data = {child.tag: child.text for child in emp}
            
            # Check the numeric values
            for key in ["Age", "Salary"]:
                if key in emp_data:
                    numeric_columns.append(float(emp_data[key]))
                    
            # Accumulate totals
            if "Age" in emp_data:
                total_age += float(emp_data["Age"])
            if "Salary" in emp_data:
                total_salary += float(emp_data["Salary"])


            # Extracting specific data
            if emp_data["Name"] == "Shelly":
                extracted_data.append(emp_data)

        # Sum numeric columns
        age_sum = sum(float(col) for col in numeric_columns[::2])
        salary_sum = sum(float(col) for col in numeric_columns[1::2])

        print("xml total age:", total_age)
        print("xml total salary:", total_salary)
        print("xml Extracting specific data:", extracted_data)


    # Error Handling
    except FileNotFoundError:
        logging.error(f"Error: The file '{file_path}' was not found.")

    except ET.ParseError:
        logging.error(f"Error: Issue with xml file format")

    except PermissionError:
        logging.error(f"Error: Permission denied while trying to write in '{file_path}'")

    except Exception as e:
       logging.error (f"An unexpected error occured: {e}")

# create the files
csv_file_path = 'data.csv'
json_file_path = "data.json"
xml_file_path = "data.xml"

create_csv(csv_file_path)
create_json(json_file_path)
create_xml(xml_file_path)

# process the files
process_csv(csv_file_path)
print()
process_json(json_file_path)
print()
process_xml(xml_file_path)

