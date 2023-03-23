from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://yandex.ru/maps/'
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("start-maximized")
options.add_argument("--headless")

# защищаем наш IP
options.set_capability("media.peerconnection.enabled", False)

# убираем всплывающие окна
options.set_capability("dom.webnotifications.enabled", False)

# убираем отслеживание включенного удаленного управления
options.set_capability("dom.webdriver.enabled", False)
browser = Chrome(ChromeDriverManager().install(), options=options)


def br_wait(browser, block):
    br = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, block)))
    return br

def br_wait2el_click(browser, block, el_css):
    br = br_wait(browser, block)
    el = br.find_elements(By.CLASS_NAME, el_css)
    return el


def click_button(els, name):
    el = els.find_element(By.CLASS_NAME, name)
    el.click()
