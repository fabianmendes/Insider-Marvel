from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(40)  # seconds
driver.get(	"https://www.marvel.com/signin?referer=https%3A%2F%2Fwww.marvel.com%2Finsider")

#Detecting items:
browser = driver
username ="email"
password ="contrasena"


WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.ID, 'disneyid-iframe')))
#framing = driver.find_element_by_id('disney-wrapper')


a = driver.find_elements_by_tag_name("div")#[2]
d = driver.find_element_by_id('disneyid-wrapper')
driver.switch_to.frame("disneyid-iframe")  # disneyid-wrapper
print("\n", a,   "\n", d
      )

yeah = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/section/section/form/section/div[1]/div/label/span[2]/input"
    )
#yeah2= driver.find_elements_by_class_name("input-wrapper")[1]
# print(str(len(yeah2)), yeah2)
yeah.click()

yeah.send_keys(username)  # email
hell = driver.find_element_by_xpath(
    '//*[@id="did-ui-view"]/div/section/section/form/section/div[2]/div/label/span[2]/input')
hell.click()
hell.send_keys(password)
hell.send_keys(Keys.ENTER)

# DONE. So far here. Now let's rocking it with the activities!.
# ------------------
