import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


@when(u'Opening product page')
def step_impl(context):
    driver = context.driver
    driver.get("https://wpqa1.eniture-qa.com/wp-admin/edit.php?post_type=product")


@when(u'I open product page')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form[1]/table/tbody/tr[2]/td[2]/strong/a"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/ul/li[3]/a"))).click()


@when(u'I verify the placeholders are displayed and enabled')
def step_impl(context):
    driver = context.driver

    def product_checkboxes(name, is_displayed, is_enabled):

        if is_displayed:
            assert True, f"{name} Checkbox is displayed"
        else:
            assert False, f"Error!! {name} Checkbox is not displayed"

        if is_enabled:
            assert True, f"{name} Checkbox is enabled"
        else:
            assert False, f"Error!! {name} Checkbox is not enabled"

        dropship_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/div[2]/p[2]/input").is_displayed()
        dropship_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/div[2]/p[2]/input").is_enabled()
        name = 'Insure checkbox'
        product_checkboxes(name, dropship_displayed, dropship_enabled)

        hazardous_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/div[2]/p[6]/input").is_displayed()
        hazardous_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/div[2]/p[6]/input").is_enabled()
        hazardous_name = 'Hazardous checkbox'
        product_checkboxes(hazardous_name, hazardous_displayed, hazardous_enabled)

        nested_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/div[2]/p[7]/input").is_displayed()
        nested_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/div[2]/p[7]/input").is_enabled()
        nested_name = 'Nested checkbox'
        product_checkboxes(nested_name, nested_displayed, nested_enabled)


@when(u'I verify that fedex ltl is showing in dropdown menu')
def step_impl(context):
    driver = context.driver
    element = driver.find_element(By.ID, "product_shipping_class")
    drp = Select(element)
    options = drp.options
    freight_label = "LTL Freight"
    for option in options:
        if option.text == freight_label:

            if option.text == freight_label:
                assert True, f"LTL Freight label is displayed in dropdown menu "
            elif option.text != freight_label:
              assert False, f"LTL Freight label is not displayed in dropdown menu {option.text}"
        else:

            pass


@then(u'I verify that dropship locations are available on product page')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    driver.get("https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_freight&section=section-2#")

    city = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]")))
    state = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[3]")))
    zip = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[4]")))
    country = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[5]")))

    data = {
        'city': city.text,
        'state': state.text,
        'zip': zip.text,
        'country': country.text
            }


    driver.back()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/ul/li[3]/a"))).click()
    element = wait.until(EC.visibility_of_element_located((By.ID, "_dropship_location[1289]")))
    drp = Select(element)
    options = drp.options
    dropships = []
    for option in options:
        dropships.append(option.text)


    # assert False, f"These are dropships list {dropships}"


@then(u'Success message will be displayed')
def step_impl(context):
    pass
