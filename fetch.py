from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Esvar:
    user_name = "standard_user"
    password = "standard_user"

    # Constructor
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Maximize and get, return URL
    def fetch_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return url
        except :
            print("Passed the incorrect URL")

    # Gets the title of the current page
    def title_webpage(self):
        return self.driver.title

    # Login with the given credentials
    def login(self):
        try:
            self.driver.find_element(By.ID, value="user-name").send_keys(self.user_name)
            sleep(1)
            self.driver.find_element(By.ID, value="password").send_keys(self.password)
            sleep(1)
            self.driver.find_element(By.ID, value="login-button").click()
            sleep(2)
        except:
            print("Login stopped by exception")

    # Create file with the content of the page
    def fetch_webcontent(self, name):
        try:
            web_content = self.driver.find_element(By.XPATH, "/html/body").text
            new_file = open(name + '.txt', 'w')
            # add the content to the created file
            new_file.write(web_content)
            new_file.close()
        except:
            print("File is not created because of the exception")

    # Close the file
    def shutdown(self):
        self.driver.quit()


# Required url
url = "https://www.saucedemo.com/"
# Required file name
n = "webpage_task_11"
# Object creation of the class
e = Esvar(url)
# Print the url of the webpage
print(e.fetch_url())
# Print the tile of the webpage
print(e.title_webpage())
# Call the created methods
e.login()
e.fetch_webcontent(n)
e.shutdown()
