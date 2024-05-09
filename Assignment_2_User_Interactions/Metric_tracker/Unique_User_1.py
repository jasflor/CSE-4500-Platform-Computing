import time
from selenium import webdriver

def num_Words(driver, num_Characters):
    page_source = driver.page_source

    words = page_source.split()

    count = sum(1 for word in words if len(word) == num_Characters) # how many words in the "words" list have a length that is the same as the number of characters specified in main

    return count

def main():

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")

    num_Characters = 3 #preferred word length

    word_count = num_Words(driver, num_Characters) 

    reward_time = 1  # 1 second reward

    total_reward_time = reward_time * word_count

    print(f"Total reward time: {total_reward_time} seconds")

    time.sleep(total_reward_time)
    driver.quit()

if __name__ == "__main__":
    main()