import time
from selenium import webdriver
import collections
import csv

#def writeTo(filename : str, metrics : dict):
#    with open(file=filename, mode="w", newline="") as fp:
#        writer = csv.DictWriter(fp, fieldnames=metrics.keys())
#        writer.writeheader()
#        writer.writerow(metrics)

def writeTo(filename: str, metrics: dict):
    with open(filename, "w", newline="") as fp:
        writer = csv.writer(fp) 
        writer.writerow(["Presence time (Seconds)", "Scrolling (Pixels)"]) 
        
        for presence_time, scrolling in zip(metrics["Presence time (Seconds)"], metrics["Scrolling (Pixels)"]):
            if presence_time != 0:  # Skip rows with zero presence time
                writer.writerow([presence_time, scrolling])

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to my page 
    driver.get("http://localhost:3000/")

    # Get my page title & print
    page_title = driver.title
    print("Page Title:", page_title)

    #initialize variables
    metrics = collections.defaultdict(list) # {Presence Time (Seconds) or Scrolling (Pixels) : Presence Time or Scrolling Time}
    SAMPLE_SIZE = 4
    count = 0
    start_time = time.time()

    while count < SAMPLE_SIZE:
        # Track presence time 
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        metrics["Presence time (Seconds)"].append(presence_time)

        # TIMESTAMP : "Presence Time (Seconds)" : Presence Time
        # TIMESTAMP : "Scrolling (Pixels)" : Scroll

    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
        metrics["Scrolling (Pixels)"].append(current_scroll/scroll_height)
        
        count += 1
        time.sleep(2)
        
        
    driver.quit()
    print(metrics)
    writeTo("metrics.csv", metrics)

if __name__ == "__main__":
    main()


