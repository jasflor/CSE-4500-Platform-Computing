import time
from selenium import webdriver


def findEmoticon(driver, emoticon)->bool:
    print(driver.page_source.lower())
    return emoticon in driver.page_source
def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    emoticons = ["&#128151"]
    for emoticon in emoticons:
        if findEmoticon(driver, emoticon):
            total_reward_time += reward_time
            time.sleep(reward_time)
    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()