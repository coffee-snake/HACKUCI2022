from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to get the Text from Zoom
def getZoomText(url):

    # URL into str and start driver
    url = str(url)
    driver = webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe")

    # If URL works, scrap through the transcript and return a string of context
    try:
        driver.get(url)

        # Find transcript by class name and get text without the 1st index name
        transcript = driver.find_element(By.CLASS_NAME, "transcript-list")
        text = transcript.text
        text = text.split('\n')
        text = text[1:]

        # Skip timestamp and add script after a time stamp
        allstring = ""
        toApp = True
        for string in text:
            if ':' in string:
                toApp= True
            else:
                if toApp:
                    allstring += string
                    allstring += "\n"
                    toApp = False

        # Return full script and close driver
        driver.close()
        return allstring

    # Return -1 if URL does not work or error occur
    except:
        return -1