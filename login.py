from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


# for chrome
# browser = webdriver.Chrome()

# if selenium path is not configure then pass driver path as an argument like this:
# browser = webdriver.Firefox(executable_path=EXE_PATH)
browser = webdriver.Firefox()

browser.get("https://gmail.com")

email = "XXXXXXXXXXX"		# CHANGE THIS
ipass = "XXXXXXXXXXX"		# CHANGE THIS

# fields
pass_field = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"

# buttons
u_next_btn = "/ahtml/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span"
p_next_btn = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]"

try:
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "identifierId")))
    browser.find_element_by_id("identifierId").send_keys(email)
    browser.find_element_by_xpath(u_next_btn).click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, pass_field)))
    browser.find_element_by_xpath(pass_field).send_keys(ipass)
    browser.find_element_by_xpath(p_next_btn).click()

except TimeoutException as te:
    print("Timeout exception. " + str(te))
    browser.close()

except NoSuchElementException as nsee:
    print("Maybe Gmail login structure is changed, or there's typo in path selector. " + str(nsee))
    browser.close()

except WebDriverException as wde:
    print("Unable to locate driver. " + str(wde))
    browser.close()

finally:
    input()
    browser.close()
