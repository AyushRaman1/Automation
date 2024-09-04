from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time 
def linkedin():
    # Replace with the correct path to chromedriver.exe
    executable_path = 'C:/Chromedriver/chromedriver-win64/chromedriver.exe'

    # Setting up the ChromeDriver service and options
    service = Service(executable_path)
    options = webdriver.ChromeOptions()
    web = webdriver.Chrome(service=service, options=options)
    
    web.get("https://www.linkedin.com/")
    web.maximize_window()
    wait = WebDriverWait(web, 20)  # Explicit wait

    print("Clicking on the 'Sign in' button")
    sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    sign_in_button.click()

    print("Entering email")
    email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email_field.send_keys("ajaydjniranjan@gmail.com")  # Replace with your email

    print("Entering password")
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("MSDAjay005.")  # Replace with your password

    print("Clicking on the 'Sign in' button to log in")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()


    

    print("Performing a search for 'Aditya bag'")
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_box.send_keys("Aditya bag")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    print("Waiting for search results to load")
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='reusable-search__entity-result-list list-style-none']/li[1]//div[1]/a")))
    first_result.click()
    time.sleep(8)

    msg = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]")))
    msg.click()
    time.sleep(4)

    print("Navigating to 'My Network' page")
    my_network = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[2]/a")))
    my_network.click()

    print("Sending a connection request")
    try:
        connect_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div/section/div[3]/footer/button")))
        connect_button.click()
        time.sleep(3)
    except Exception as e:
        print("No connection request available or it was not found.")
        print(e)
        time.sleep(3)
    
    print("Navigating to 'Jobs' page")
    jobs = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]/a/span")))
    jobs.click()
    time.sleep(5)

    print("Searching for 'Software Engineer' jobs")
    job_search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))
    job_search_box.send_keys("Software Engineer")
    time.sleep(2)
    job_search_box.send_keys(Keys.ENTER)
    time.sleep(8)

    print("Navigating to Messages ")
    message = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[4]/a")))
    message.click()
    time.sleep(5)
    message_search=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[1]/div/div/input")))
    message_search.send_keys("Ayush Raman")
    message_search.send_keys(Keys.ENTER)
    search = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[1]/div[2]/ul/li[2]/div/a/div[2]")))
    search.click()
    time.sleep(10)

    print("Logging out")
    me_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[6]/div/button")))
    me_icon.click()
    time.sleep(5)
    sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'logout')]")))
    sign_out_button.click()

    print("Closing the browser")
    web.quit()

linkedin()
