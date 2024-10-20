import time
import traceback
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.naukri.com/nlogin/login")

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "usernameField"))
    )

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwordField"))
    )

    email_input.send_keys("Enter your email id ")
    password_input.send_keys("Enter your password")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Login' or contains(text(), 'Login')]"))
    )
    driver.execute_script("arguments[0].click();", login_button)

    link_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div[2]/div[3]/div/div[1]'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", link_element)
    link_element.click()

    anchor_tag = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/a'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", anchor_tag)
    anchor_tag.click()

    sideBar = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/div/div[3]/div[1]/div/div[3]/div'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", sideBar)
    sideBar.click()

    #keyskills clicked
    key_skills_section = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="skillDetails"]/div/p'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", key_skills_section)
    time.sleep(1)  # Adjust as necessary
    driver.execute_script("arguments[0].click();", key_skills_section)

    
    # Click on the "Skills Write" section
    skills_write_section = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="keySkillSugg"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", skills_write_section)
    skills_write_section.click()
    skills_write_section.send_keys("Communication Skills,")

    skills_write_section = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="keySkillSugg"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", skills_write_section)
    skills_write_section.click()

    #save button
    save_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-btn"]'))
    )
    save_button.click()

    # again clicked skills area for deletion of skill
    key_skills_section = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="skillDetails"]/div/p'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", key_skills_section)
    time.sleep(1)  # Adjust as necessary
    driver.execute_script("arguments[0].click();", key_skills_section)

    # Clicked for deletion of skill
    skills_deletion = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="skillDetails"]/div[1]/div/div[1]/div[1]/div/div/div[15]/a'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", skills_deletion)
    time.sleep(2)  # Adjust as necessary
    driver.execute_script("arguments[0].click();", skills_deletion)
    try:
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="skillDetails"]/div[1]/div/div[1]/div[1]/div/div/div[15]/a'))  # Adjust based on actual confirmation button XPath
        )
        confirm_button.click()
    except Exception as e:
        print("No confirmation dialog found or error occurred:", e)

    #again clicked the save button
    save_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-btn"]'))
    )
    save_button.click()

    # click on the profile picture
    link_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div[2]/div[3]/div/div[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", link_element)
    link_element.click()

    # click on the logout button
    logout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/div[4]/a'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", logout)
    logout.click()


except Exception as e:
    print("Error occurred:")
    print(traceback.format_exc())

finally:
    time.sleep(5)
    driver.quit()

