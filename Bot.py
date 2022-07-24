from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

username_input = "email@gmail.com"
password_imput = "linkedinpass"
phone_number = "phonenumber"

driver = webdriver.Chrome("C:/Users/JUAN/Documents/chromedriver/chromedriver.exe")
driver.get("LinkedinSearchLink")

sign_in_button = driver.find_element("link text","Sign in")
sign_in_button.click()
time.sleep(3)

email_field = driver.find_element("id", "username")
email_field.send_keys(username_input)

password_field = driver.find_element("id","password")
password_field.send_keys(password_imput)
password_field.send_keys(Keys.ENTER)
time.sleep(3)


all_listings = driver.find_elements("css selector",".job-card-container--clickable")


for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(3)
    try:
        apply_button = driver.find_element("css selector",".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        next_button = driver.find_element("css selector","footer button")
        next_button.click()
        time.sleep(2)
        review_button = driver.find_element("class name","artdeco-button--primary")
        print("Review Button")

        review_button_text = review_button.get_attribute("aria-label")

        print(review_button_text)
        if review_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element("class name", "artdeco-button__icon")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element("class name", "artdeco-button--secondary")
            discard_button.click()
            print("Complex Application Skipped")
            continue
        else:
            review_button.click()
            time.sleep(2)
            submit_button = driver.find_element("class name","artdeco-button--primary")
            if submit_button.get_attribute("aria-label") == "Submit application":
                submit_button.click()
                time.sleep(2)
                close_button = driver.find_element("class name", "artdeco-button__icon")
                close_button.click()
            else:
                close_button = driver.find_element("class name", "artdeco-button__icon")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element("class name", "artdeco-button--secondary")
                discard_button.click()
                print("Complex Application Skipped")

    except NoSuchElementException:
        print("No application Button, Skipped")
        continue
