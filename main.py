import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from browser import URL, br_wait, br_wait2el_click, browser
from oper2css import OPER_CSS
from params import get_params
from route import get_adress_field, get_route


def click_button(els, name):
    el = els.find_element(By.CLASS_NAME, name)
    el.click()


  
def main(adress_1, adress_2):
    adress_1 += '\n'
    adress_2 += '\n'
    browser.get(URL)
    br_wait(browser, OPER_CSS['map_control'])
    el = browser.find_element(By.CLASS_NAME, 'body')
    click_button(el, 'route-control__inner')
    get_adress_field(
        br_wait2el_click(browser, OPER_CSS['route_menu'], OPER_CSS['start'])[0],
        adress_1
    )
    get_adress_field(
        br_wait2el_click(browser, OPER_CSS['route_menu'], OPER_CSS['finish'])[0],
        adress_2
    )
    
    get_params(
        br_wait2el_click(
        browser, OPER_CSS['route_panel'], OPER_CSS['route_items']
        )[0]
    )
    return get_route(br_wait(browser, OPER_CSS['route_result']))


def test():
    adress_1 = 'тольяттиб карбышева, 15'
    adress_2 = 'cfhfnjd, ctntdfz 7'
    assert (main(adress_1, adress_2) == '420 км, Без учета пробок')
    adress_1 = '53.506202, 49.422735'
    adress_2 = 'Ыфкфещмб Сетеваяб 7'
    assert (main(adress_1, adress_2) == '430 км, Без учета пробок')

if __name__ == '__main__':
    print(test())
    time.sleep(60)
