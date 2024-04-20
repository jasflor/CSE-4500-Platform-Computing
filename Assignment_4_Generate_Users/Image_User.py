import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def countElem(driver, tag_name)->int:
    return len (driver.find_elements(By.TAG_NAME, tag_name))

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    tag = ["img"]
    for tag in tag:
        num_images = countElem(driver, tag)
        total_reward_time += reward_time*num_images
        time.sleep(total_reward_time)
    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__=="__main__":
    main()
