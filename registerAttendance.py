from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def setupDriver():
    firefox_dev_binary = FirefoxBinary(
        r"C:\Program Files\Firefox Developer Edition\firefox.exe"
    )
    return webdriver.Firefox(firefox_binary=firefox_dev_binary)


def openBlackBoard(browser):
    browser.get("https://blackboard.le.ac.uk/")
    browser.maximize_window()


def login(browser, username, password):
    # get the inputs
    userNameInput = browser.find_element_by_id("userNameInput")
    passWordInput = browser.find_element_by_id("passwordInput")

    # send the credentials
    userNameInput.send_keys(username)
    passWordInput.send_keys(password)

    # submit the form.
    submitButton = browser.find_element_by_id("submitButton")
    submitButton.click()


def startProcess(browser):
    try:
        testAnnouncment = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[5]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a",
                )
            )
        )
        testAnnouncment.click()

        test = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[5]/div[2]/div/div/div[3]/form/ul/li[1]/div[1]/p[4]/a",
                )
            )
        )
        test.click()

        beginTestButton = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[5]/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/p/input[2]",
                )
            )
        )
        beginTestButton.click()

        yesRadioButton = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='radio'][value='yes_no.true']")
            )
        )
        yesRadioButton.click()

        submitButton = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
        )
        submitButton.click()

        WebDriverWait(browser, 60).until(EC.alert_is_present())

        alert = browser.switch_to.alert
        alert.accept()

        browser.close()

        print("Automation finished.")
    except TimeoutException:
        print("Loading took too long, check xpaths or increase wait..")


def startScript():
    usr, pswrd = input("Enter your username and password with a space: ").split()
    print(f"{usr} {pswrd}")
    browser = setupDriver()
    openBlackBoard(browser)
    login(browser, usr, pswrd)
    startProcess(browser)


if __name__ == "__main__":
    print(__name__)
    startScript()

