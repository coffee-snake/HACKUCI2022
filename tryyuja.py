from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def getYujaText(url, user_input, password_input):
    user = str(user_input)
    password = str(password_input)

    driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

    driver.implicitly_wait(0.5)
    driver.maximize_window()

    try:
        driver.get(str(url))
    except:
        return -1

    yuja_login = driver.find_element(By.XPATH, "//button[@id='loginButtonSSO']")
    yuja_login.click()

    driver.implicitly_wait(4.0)

    uci_id = driver.find_element(By.ID, "ucinetid")
    uci_id.send_keys(user)
    uci_pswd = driver.find_element(By.ID, "password")
    uci_pswd.send_keys(password)

    try:
        uci_login = driver.find_element(By.NAME, "login_button")
        driver.implicitly_wait(2.0)
        uci_login.click()

    except NoSuchElementException:
        return -2

    driver.implicitly_wait(5.0)

    frame1 = driver.find_element_by_css_selector("#duo_iframe > iframe")

    driver.switch_to.frame(frame1)
    duo_login = driver.find_element(By.XPATH, "//button[text()='Send Me a Push ']")
    duo_login.click()
    driver.switch_to.parent_frame()
    time.sleep(10.0)

    containers = driver.find_elements_by_css_selector(".dcmv_tabContentPanel > div > div")
    text = containers[-1].text
    return text