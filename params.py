import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from browser import br_wait, br_wait2el_click, browser
from conditions import KEY_CAR_PARAMS, PARAMS
from constants import CONDITIONS, SYM
from oper2css import OPER_CSS
from truck_config import CAR_PARAMS, CAR_SPECIAL_EDITION, CAR_TYPE


def get_menu(els):
    time.sleep(5)
    el = els.find_element(By.CLASS_NAME, OPER_CSS['car_menu'])
    el.click()
    br_wait(browser, OPER_CSS['car_menu_cntrl'])


def get_type_weight(weight):
    if weight > 12:
        return 2
    if weight < 3.5:
        return 0
    return 1


def get_value(str):
    val = ''
    for s in str:
        val += (SYM[s] if s in SYM else '')
    return val


def set_param(el, param):
    value = get_value(el.find_element(By.CLASS_NAME, OPER_CSS['cargo_param_value']).get_attribute('value'))
    if float(value) < int(param):
        el.find_element(By.CLASS_NAME, OPER_CSS['cargo_param_right']).click()
    elif float(value) > int(param):
        el.find_element(By.CLASS_NAME, OPER_CSS['cargo_param_left']).click()
    else:
        return
    set_param(el, param)


def set_euro_class(browser):
    el = br_wait2el_click(
        browser,
        OPER_CSS['euro_menu'],
        OPER_CSS['euro_button']
    )[0]
    el.click()
    el = br_wait2el_click(
        browser,
        OPER_CSS['euro_choice_menu'],
        OPER_CSS['euro_class']
    )[(CAR_PARAMS['euro'] - 1)]
    el.click()


def trailer_status(tr_field):
    return OPER_CSS['trailer_control'] in tr_field.get_attribute('class')


def br_trailer(browser):
    tr_field = br_wait2el_click(
        browser,
        OPER_CSS['trailer_menu'],
        OPER_CSS['trailer'])[0]

    if CAR_PARAMS['trailer'] != trailer_status(tr_field):
        tr_field.click()

def set_special_params(browser):
    els = br_wait2el_click(
        browser,
        OPER_CSS['cargo_params'],
        OPER_CSS['cargo_param']
    )
    for el in range(len(els) - 1):
        set_param(els[el], CAR_PARAMS[KEY_CAR_PARAMS[el]])
    set_euro_class(browser)
    br_trailer(browser)


def set_car_type(els, weight):
    el = els.find_elements(By.CLASS_NAME, OPER_CSS['truck_menu'])[1]
    el.click()
    type_weight = get_type_weight(weight)
    el = br_wait2el_click(
        browser,
        OPER_CSS['truck_type'],
        OPER_CSS['truck_button']
    )[type_weight]
    el.click()
    if CAR_SPECIAL_EDITION:
        set_special_params(browser)
    el = br_wait2el_click(
        browser,
        OPER_CSS['field_2_save'],
        OPER_CSS['save_button']
    )[0]
    el.click()


def set_params(els, params):
    el = els.find_elements(By.CLASS_NAME, OPER_CSS['way_choice'])[params]
    el.click()


def get_params(els):
    get_menu(els)
    for param in PARAMS:
        if CONDITIONS[param]:
            set_params(els, PARAMS[param])
    if CAR_TYPE['truck']:
        set_car_type(els, CAR_TYPE['weight'])
