from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to get the Text from Zoom
def getZoomText(url):

    # URL into str and start driver
    url = str(url)
    driver = webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe")

    # If URL works, scrap through the transcript and return a string of context
    try:
        driver.get(url)
        time.sleep(10)

        time.sleep(10.0)

        # Find transcript by class name and get text without the 1st index name
        transcript = driver.find_element(By.CLASS_NAME, "transcript-list")
       
        text = transcript.text
        print(text)
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
        #driver.close()
        return allstring

    # Return -1 if URL does not work or error occur
    except:
        return -1

if __name__ == "__main__":
    print(getZoomText("https://uci.zoom.us/rec/play/KFfHRIdPsXYMWjgv7oT1Gbvmbc4RALmDQfs6D_rvF5LxRW20ELKojuden0Wy2Fz-2bC9t3H2C0GRhTke.ck4FzmcgKVlTddsJ?continueMode=true&_x_zm_rtaid=_Xkj-VPjTh2QoXyVbub8sA.1645931160216.deaf91508c7d84b15dd031ceff038f31&_x_zm_rhtaid=101"))

