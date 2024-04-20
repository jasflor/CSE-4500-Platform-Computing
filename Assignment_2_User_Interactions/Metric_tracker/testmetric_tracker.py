import time
from selenium import webdriver
import collections
import csv
import mysql.connector

# Function to establish a MySQL connection
def connect_to_mysql(host, username, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print("Connected to MySQL database successfully")
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)

# Function to insert metrics into MySQL database
def insert_metrics_into_mysql(connection, table_name, metrics):
    cursor = connection.cursor()
    # Prepare INSERT statement
    insert_query = f"INSERT INTO {table_name} (presence_time_seconds, scrolling_pixels) VALUES (%s, %s)"
    # Execute INSERT statement for each metric
    for presence_time, scrolling in zip(metrics["Presence time (Seconds)"], metrics["Scrolling (Pixels)"]):
        cursor.execute(insert_query, (presence_time, scrolling))
    # Commit the transaction
    connection.commit()
    print("Metrics inserted into MySQL database successfully!")

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to the page 
    driver.get("http://localhost:3000/")

    # Get the page title
    page_title = driver.title
    print("Page Title:", page_title)

    # Initialize variables
    metrics = collections.defaultdict(list)
    SAMPLE_SIZE = 2
    count = 0
    start_time = time.time()

    while count < SAMPLE_SIZE:
        # Track presence time 
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        metrics["Presence time (Seconds)"].append(presence_time)

        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
        metrics["Scrolling (Pixels)"].append(current_scroll/scroll_height)
        
        count += 1
        time.sleep(2)
    
    # Connect to MySQL database
    connection = connect_to_mysql('127.0.0.1', 'root', 'RootPass12!', 'myapp_metrics')  # Adjust credentials and database name

    # Insert metrics into MySQL database
    insert_metrics_into_mysql(connection, 'metrics_data', metrics)  # Adjust table name

    # Close the database connection
    connection.close()

    driver.quit()
    print(metrics)

if __name__ == "__main__":
    main()
