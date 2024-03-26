import time
from selenium import webdriver

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to my page 
    driver.get("http://localhost:3000/")

    # Get my page title & print
    page_title = driver.title
    print("Page Title:", page_title)

    metrics = []
    # Track presence time 
    start_time = time.time()
    presence_time = start_time
    while True:#presence_time < 50: # seconds
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    
        time.sleep(2)
        
        
    driver.quit()

if __name__ == "__main__":
    main()


