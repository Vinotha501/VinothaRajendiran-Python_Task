# Multi-threading and Concurrency
import threading
import requests
import time

downloaded_files = []
lock = threading.Lock()

# download a file
def download_file(url, filename):
    try:
        print(f"Starting download of {filename}")
        response = requests.get(url)
        with open (filename, 'wb') as f:
            f.write (response.content)
        print (f"Download completed: {filename}")

        with lock:
            downloaded_files.append(filename)

    except Exception as e:
        print (f"Error downloading {filename}: {e}")

# Process a file
def process_files():
    for filename in downloaded_files:
        print(f"Processing {filename}...")
        time.sleep(1)
        print(f"Processing completed: {filename}")

# list of files to download
file_urls = [
    ("https://example.com/file1.jpg", "file1.jpg"),
    ("https://example.com/file2.jpg", "file2.jpg"),
    ("https://example.com/file3.jpg", "file3.jpg"),
]


# single threaded version
print("\n---Starting Single-threaded Download---")
start_time_single = time.time()

# Download files sequentially (single-threaded)
for url, filename in file_urls:
    download_file(url, filename)

end_time_single = time.time()
print (f"Single-threaded total time: {end_time_single - start_time_single:.2f} seconds.")

# Multi thread version
print("\n---Starting Multi-threaded Download---")
start_time_multi = time.time()

downloaded_files.clear()

# creating and starting thread
threads = []
for url, filename in file_urls:
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

# wait for all threads to complete
for thread in threads:
    thread.join()

print("\nAll downloads completed. Starting file processing...")

process_files()

end_time_multi = time.time()
print(f"Multi-threaded total time: {end_time_multi - start_time_multi:.2f} seconds")
