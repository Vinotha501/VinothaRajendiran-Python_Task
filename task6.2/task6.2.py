# log file analyzer

import re
from collections import Counter
from datetime import datetime

def parse_log_file(file_path, start_date=None, end_date=None, severity=None):
    #regular expression pattern for IP address, timestamp and error message  
    timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' 
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b' 
    error_pattern = r'ERROR|INFO|WARNING'

    error_count = 0
    ip_addresses = []
    log_entries = []

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    with open(file_path, 'r') as log_file:
        for line in log_file:
            if not line.strip():
                continue
            
            timestamp = re.search(timestamp_pattern, line)
            ip_address = re.search(ip_pattern, line)
            error_message = re.search(error_pattern, line)

            if timestamp:
                log_timestamp = datetime.strptime(timestamp.group(), '%Y-%m-%d %H:%M:%S')
                if (start_date and log_timestamp.date() < start_date.date()) or (end_date and log_timestamp.date() > end_date.date()):
                    continue

            if severity and severity.upper() not in line.upper(): 
               continue

            if error_message and error_message.group() == "ERROR":
                error_count += 1
                log_entries.append({
                    'timestamp': timestamp.group(), 
                    'ip': ip_address.group() if ip_address else None, 
                    'message': line.strip()
                })

            if ip_address:
                ip_addresses.append(ip_address.group())

    ip_counts = Counter(ip_addresses)
    
    return{
        "error_count": error_count,
        "most_frequent_ips": ip_counts.most_common(3),
        "log_entries": log_entries
    }

def print_log_summary(log_summary):
    print("\n---Log Summary---")
    print(f"Total Errors: {log_summary['error_count']}")
    print(f"Most Frequent IP Addresses: {log_summary['most_frequent_ips']}")  

    print("\n--- Filtered Log Entries ---")
    for entry in log_summary['log_entries']:
        print(f"Timestamp: {entry['timestamp']}, IP: {entry['ip']}, Message: {entry['message']}")

if __name__ == "__main__":
   log_file_path = 'C:/Users/User/Desktop/task6.2/server_log.txt'
   start_date = '2024-10-10'
   end_date = '2024-10-10'
   severity = 'ERROR'

   log_summary = parse_log_file(log_file_path, start_date=start_date, end_date=end_date, severity=severity)

   print_log_summary(log_summary)

