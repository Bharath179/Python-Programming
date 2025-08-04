import threading
import time


def download_page(site):
    print(f"Starting download: {site}")
    time.sleep(2)  # Simulate network delay
    print(f"Finished download: {site}")


sites = ['google.com', 'github.com', 'stackoverflow.com']

threads = []
for site in sites:
    t = threading.Thread(target=download_page, args=(site,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
