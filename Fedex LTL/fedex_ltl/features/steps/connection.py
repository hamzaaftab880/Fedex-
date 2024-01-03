import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'I Click on connection settings link')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/ul/li[1]/a").click()


@then(u'Connection settings page will appear')
def step_impl(context):
    driver = context.driver
    url = driver.current_url
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_freight&section"

    if url == expected_url:
        assert True, 'Connection Page Url is working fine'
    else:
        assert False, "Wrong URL"


@when(u'I enter plugin license key "{plugin_license_key}"')
def step_impl(context, plugin_license_key):
    context.driver.find_element(By.ID, "fedex_freight_plugin_licence_key").clear()
    context.driver.find_element(By.ID, "fedex_freight_plugin_licence_key").send_keys(plugin_license_key)


@when(u'I enter billing address')
def step_impl(context):
    driver = context.driver
    address = '1828 Kell Road'
    city = 'Gulf Breeze'
    state = 'FL'
    zip_code = '32563'
    country = 'US'
    driver.find_element(By.ID, "fedex_freight_shipper_bill_address").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_address").send_keys(address)
    driver.find_element(By.ID, "fedex_freight_shipper_bill_city").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_city").send_keys(city)
    driver.find_element(By.ID, "fedex_freight_shipper_bill_state").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_state").send_keys(state)
    driver.find_element(By.ID, "fedex_freight_shipper_bill_zip").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_zip").send_keys(zip_code)
    driver.find_element(By.ID, "fedex_freight_shipper_bill_country").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_country").send_keys(country)

    # Standard LTL Freight Account Information
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[2]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[2]/td/input").send_keys(address)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[3]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[3]/td/input").send_keys(city)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[4]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[4]/td/input").send_keys(state)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[5]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[5]/td/input").send_keys(zip_code)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[6]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[6]/td/input").send_keys(country)
    # time.sleep(30)


@when(u'I enter account no "{account_no}"')
def step_impl(context, account_no):
    context.driver.find_element(By.ID, "fedex_freight_bill_num").clear()
    context.driver.find_element(By.ID, "fedex_freight_bill_num").send_keys(account_no)


@when(u'I enter meter no "{meter_no}"')
def step_impl(context, meter_no):
    context.driver.find_element(By.ID, "fedex_freight_meter_num").clear()
    context.driver.find_element(By.ID, "fedex_freight_meter_num").send_keys(meter_no)


@when(u'I enter production password "{production_password}"')
def step_impl(context, production_password):
    context.driver.find_element(By.ID, "fedex_freight_password").clear()
    context.driver.find_element(By.ID, "fedex_freight_password").send_keys(production_password)


@when(u'I enter authentication key "{authentication_key}"')
def step_impl(context, authentication_key):
    context.driver.find_element(By.ID, "fedex_freight_auth_key").clear()
    context.driver.find_element(By.ID, "fedex_freight_auth_key").send_keys(authentication_key)


@when(u'I enter shipper account number "{shipper_acc}"')
def step_impl(context, shipper_acc):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[7]/td/input").clear()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[7]/td/input").send_keys(shipper_acc)


@when(u'I enter third party account number "{acc_no}"')
def step_impl(context, acc_no):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[8]/td/input").clear()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[8]/td/input").send_keys(acc_no)


@then(u'Success message will appear')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "en_ffs"))).click()
    expected_success_message = "Success! The test resulted in a successful connection."
    success_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/p")
    if success_message.text == expected_success_message:
        assert True
    else:
        assert False, f"Wrong Credentials {success_message.text}"
        driver.quit()


@then(u'Error message will appear')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "en_ffs"))).click()
    # time.sleep(50)
    error = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/p")))
    # error = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/p")))
    expected_error = "Error! Please verify credentials and try again."

    if error.text == expected_error:
        assert True, "Success"
    else:
        assert False, f"Test failed This is the error message (  {error.text}  )"


@when(u'I leave all spaces blank')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "fedex_freight_plugin_licence_key").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_address").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_city").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_state").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_zip").clear()
    driver.find_element(By.ID, "fedex_freight_shipper_bill_country").clear()

    # Standard LTL Freight Account Information
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[2]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[3]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[4]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[5]/td/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[6]/td/input").clear()

    # Billing information
    context.driver.find_element(By.ID, "fedex_freight_bill_num").clear()
    context.driver.find_element(By.ID, "fedex_freight_meter_num").clear()
    context.driver.find_element(By.ID, "fedex_freight_password").clear()
    context.driver.find_element(By.ID, "fedex_freight_auth_key").clear()

    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[7]/td/input").clear()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[8]/td/input").clear()

    wait.until(EC.element_to_be_clickable((By.ID, "en_ffs"))).click()


@then(u'Error will be shown with required data')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    def validations_check(name, message, expected_message):
        if message.text == expected_message:
            assert True, f"{name} Validation is working fine "
        else:
            assert False, f"{name} Validation is not working fine  {message.text}"

    plugin_key = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[1]/tbody/tr/td/span")))
    expected_plugin_key = "Plugin License Key is required."
    key_name = "Plugin License Key"
    validations_check(key_name, plugin_key, expected_plugin_key)

    billing_address = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[1]/td/span")))
    expected_address = 'Billing Address is required.'
    billing_name = "Billing Address"
    validations_check(billing_name, billing_address, expected_address)

    billing_city = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[2]/td/span")))
    expected_city = 'Billing City is required.'
    city_name = 'Billing City'
    validations_check(city_name, billing_city, expected_city)

    billing_state = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[3]/td/span")))
    expected_state = 'Billing State is required.'
    state_name = "Billing State"
    validations_check(state_name, billing_state, expected_state)

    billing_zip = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[4]/td/span")))
    expected_zip = 'Billing Zip is required.'
    zip_name = 'Billing Zip'
    validations_check(zip_name, billing_zip, expected_zip)

    billing_country = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[5]/td/span")))
    expected_country = 'Billing Country is required.'
    country_name = "Billing Country"
    validations_check(country_name, billing_country, expected_country)

    billing_account_no = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[6]/td/span")))
    expected_billing_account_no = 'Billing Account Number is required.'
    account_name = "Billing Account Number"
    validations_check(account_name, billing_account_no, expected_billing_account_no)

    meter_no = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[7]/td/span")))
    expected_meter_no = 'Meter Number is required.'
    meter_name = "Meter Number"
    validations_check(meter_name, meter_no, expected_meter_no)

    password = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[8]/td/span")))
    expected_password = 'Password is required.'
    password_name = "Password"
    validations_check(password_name, password, expected_password)

    authentication = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[3]/tbody/tr[9]/td/span")))
    expected_authentication = 'Authentication Key is required.'
    authentication_name = "Authentication Key"
    validations_check(authentication_name, authentication, expected_authentication)

    physical_address = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[2]/td/span")))
    expected_physical_address = 'Physical Address is required.'
    physical_address_name = 'Physical Address'
    validations_check(physical_address_name, physical_address, expected_physical_address)

    physical_city = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[3]/td/span")))
    expected_physical_city = 'Physical City is required.'
    physical_city_name = "Physical City"
    validations_check(physical_city_name, physical_city, expected_physical_city)

    physical_state = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[4]/td/span")))
    expected_physical_state = 'Physical State is required.'
    physical_state_name = "Physical state"
    validations_check(physical_state_name, physical_state, expected_physical_state)

    physical_zip = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[5]/td/span")))
    expected_physical_zip = 'Physical Zip is required.'
    physical_zip_name = "Physical Zip"
    validations_check(physical_zip_name, physical_zip, expected_physical_zip)

    physical_country = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[6]/td/span")))
    expected_physical_country = 'Physical Country is required.'
    physical_country_name = "Physical Country"
    validations_check(physical_country_name, physical_country, expected_physical_country)

    shipper_account_no = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/table[5]/tbody/tr[7]/td/span")))
    expected_shipper_account_no = 'Shipper Account Number is required.'
    shipper_name = "Shipper Account Number"
    validations_check(shipper_name, shipper_account_no, expected_shipper_account_no)


