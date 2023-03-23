from selenium.webdriver.common.by import By

from oper2css import OPER_CSS


def write_adress(el, adress):
    el.send_keys(str(adress))


def get_adress_field(els, adress):
    write_adress(els.find_element(By.TAG_NAME, 'input'), adress)


def get_route(els):
    route_time = els.find_element(By.CLASS_NAME, OPER_CSS['route_time']).text
    route_range = els.find_element(By.CLASS_NAME, OPER_CSS['route_ramge']).text
    print(route_time)
    return route_range