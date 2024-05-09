import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findWord(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        # print(driver.page_source)
        return True
    else:
        return False

def countTagElem(driver, tag_names) -> int:
    count = 0
    for tag_name in tag_names:
        count += len(driver.find_elements(By.TAG_NAME, tag_name))
    return count

def findEmoticon(driver, emoticon)->bool:
    print(driver.page_source.lower())
    return emoticon in driver.page_source

def click_link(driver, href, reward_time):
    links = driver.find_elements(By.TAG_NAME, "a")
    link_found = False
    for link in links:
        if link.get_attribute("href") == href:
            link.click()
            link_found = True
            break
    if not link_found:
        print(f"Link with href='{href}' not found.")

def userAction(action, driver, reward_time, req_lis)->float:
    total_reward_time = 10
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findWord(driver, keyword):
                print("Found",keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("Not found")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)
    elif action.upper() == "EMOTICON":
        for emoticon in req_list:
            if findEmoticon(driver, emoticon):
                print("Found", emoticon)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("Emoticon", emoticon, "not found")
    elif action.upper() == "LINK":
        for link in req_list:
            click_link(driver, link, reward_time)
            total_reward_time += reward_time

    return total_reward_time

def userAction(driver):
    reward_time = 10
    keyword = ["cooking", "reading"]

    time.sleep(reward_time)

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0

    total_reward_time += userAction("KEYWORD", driver, reward_time, ["book", "cooking"])
    tag_name = ["img"]
    total_reward_time += userAction("IMAGE", driver, reward_time, tag_name)

    emoticons = ["📚"]
    total_reward_time += userAction("EMOTICON", driver, reward_time, emoticons)

    links = ["https://github.com/jasflor"]
    total_reward_time += userAction("LINK", driver, reward_time, links)

    click_link(driver, "https://github.com/jasflor", reward_time)

    print("Presence Time:", total_reward_time)

if __name__== "__main__":
    main()