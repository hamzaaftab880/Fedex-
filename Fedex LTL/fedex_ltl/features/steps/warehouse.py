import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'I Open Login Page warehouse')
def step_impl(context):
    context.driver.get("https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_freight&section=section-2#")


@then(u'Warehouse page will be displayed')
def step_impl(context):
    url = context.driver.current_url
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_freight&section=section-2#"
    if url == expected_url:
        assert True, "Warehouse page link is Working Fine"
    else:
        assert False, "Invalid link"


@then(u'Checking placeholders are enabled and displayed')
def step_impl(context):
    driver = context.driver

    driver.find_element(By.NAME, "avc").click()

    def placeholder_check(name, displayed, enabled):
        if enabled:
            assert True, f"{name} Placeholder is Enabled"
        if displayed:
            assert True, f"{name} Placeholder is Displayed"

    street_address_displayed = driver.find_element(By.ID, "en_wd_origin_address").is_displayed
    street_address_enabled = driver.find_element(By.ID, "en_wd_origin_address").is_enabled
    s_name = "Street Address"
    placeholder_check(s_name, street_address_displayed, street_address_enabled)
    zip_displayed = driver.find_element(By.ID, "en_wd_origin_zip").is_displayed()
    zip_enabled = driver.find_element(By.ID, "en_wd_origin_zip").is_enabled()
    z_name = "Zip Code"
    placeholder_check(z_name, zip_displayed, zip_enabled)
    city_displayed = driver.find_element(By.ID, "en_wd_origin_city").is_displayed()
    city_enabled = driver.find_element(By.ID, "en_wd_origin_city").is_enabled()
    c_name = "Zip Code"
    placeholder_check(c_name, city_displayed, city_enabled)

    state_displayed = driver.find_element(By.ID, "en_wd_origin_state").is_displayed()
    state_enabled = driver.find_element(By.ID, "en_wd_origin_state").is_enabled()
    state_name = "State "
    placeholder_check(state_name, state_displayed, state_enabled)

    country_displayed = driver.find_element(By.ID, "en_wd_origin_country").is_displayed()
    country_enabled = driver.find_element(By.ID, "en_wd_origin_country").is_enabled()
    country_name = "Country "
    placeholder_check(country_name, country_displayed, country_enabled)

    address_miles_displayed = driver.find_element(By.ID, "instore-pickup-address").is_displayed()
    address_miles_enabled = driver.find_element(By.ID, "instore-pickup-address").is_enabled()
    address_miles_name = "Offer Address within miles "
    placeholder_check(address_miles_name, address_miles_displayed, address_miles_enabled)

    address_zip_displayed = driver.find_element(By.ID, "instore-pickup-zipmatch").is_displayed()
    address_zip_enabled = driver.find_element(By.ID, "instore-pickup-zipmatch").is_enabled()
    address_zip_name = "Offer Address if zip code matches "
    placeholder_check(address_zip_name, address_zip_displayed, address_zip_enabled)

    is_checkout_description_displayed = driver.find_element(By.ID, "instore-pickup-desc").is_displayed()
    is_checkout_description_enabled = driver.find_element(By.ID, "instore-pickup-desc").is_enabled()
    is_checkout_description_name = "Checkout Description "
    placeholder_check(is_checkout_description_name, is_checkout_description_displayed, is_checkout_description_enabled)

    is_phone_displayed = driver.find_element(By.ID, "instore-pickup-desc").is_displayed()
    is_phone_enabled = driver.find_element(By.ID, "instore-pickup-desc").is_enabled()
    is_phone_name = "Phone Number "
    placeholder_check(is_phone_name, is_phone_displayed, is_phone_enabled)

    ld_address_miles_displayed = driver.find_element(By.ID, "local-delivery-address").is_displayed()
    ld_address_miles_enabled = driver.find_element(By.ID, "local-delivery-address").is_enabled()
    ld_name = "(Local Delivery )Offer address within miles  "
    placeholder_check(ld_name, ld_address_miles_displayed, ld_address_miles_enabled)

    ld_address_zip_displayed = driver.find_element(By.ID, "local-delivery-zipmatch").is_displayed()
    ld_address_zip_enabled = driver.find_element(By.ID, "local-delivery-zipmatch").is_enabled()
    ld_zip_name = "(Local Delivery )Offer address within miles  "
    placeholder_check(ld_zip_name, ld_address_zip_displayed, ld_address_zip_enabled)

    ld_checkout_displayed = driver.find_element(By.ID, "local-delivery-desc").is_displayed()
    ld_checkout_enabled = driver.find_element(By.ID, "local-delivery-desc").is_enabled()
    ld_checkout_name = "(Local Delivery )Offer address within miles  "
    placeholder_check(ld_checkout_name, ld_checkout_displayed, ld_checkout_enabled)

    local_delivery_displayed = driver.find_element(By.ID, "local-delivery-desc").is_displayed()
    local_delivery_enabled = driver.find_element(By.ID, "local-delivery-desc").is_enabled()
    local_delivery_name = "(Local Delivery )Offer address within miles  "
    placeholder_check(local_delivery_name, local_delivery_displayed, local_delivery_enabled)

    local_delivery_fee_displayed = driver.find_element(By.ID, "local-delivery-desc").is_displayed()
    local_delivery_fee_enabled = driver.find_element(By.ID, "local-delivery-desc").is_enabled()
    local_delivery_fee_name = "(Local Delivery )Offer address within miles  "
    placeholder_check(local_delivery_fee_name, local_delivery_fee_displayed, local_delivery_fee_enabled)


@then(u'Checking checkboxes are enabled and working properly')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.NAME, "avc"))).click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="checkbox"]')))
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        enabled = checkbox.is_enabled()
        selected = checkbox.is_selected()
        name = checkbox.get_attribute('name')
        if enabled:
            assert True, f"{name} Checkboxes are enabled"
        else:
            assert False, f"{name} Checkboxes are not enabled"

        if selected:
            wait.until(EC.element_to_be_clickable((By.NAME, name))).click()
            # checkbox.click()
            selected = checkbox.is_selected()
            if not selected:
                assert True, f"{name} Checkbox is working properly "
        elif not selected:
            # checkbox.click()
            wait.until(EC.element_to_be_clickable((By.NAME, name))).click()
            selected = checkbox.is_selected()
            if selected:
                assert True, f"{name} Checkbox is working properly "
        else:
            assert False, f"{name} Checkboxes are not displayed"


@when(u'I Click on submit button without entering data')
def step_impl(context):
    driver = context.driver
    # Clicking on add warehouse button
    driver.find_element(By.NAME, "avc").click()
    time.sleep(1)
    # Clicking on submit button without entering data on add warehouse window
    driver.find_element(By.NAME, "en_wd_submit_warehouse").click()
    time.sleep(1)


@then(u'Validations will be displayed')
def step_impl(context):
    driver = context.driver

    # This is the expected error message
    expected_zip_message = "Zip is required."
    expected_city_message = "City is required."
    expected_state_message = "State is required."
    expected_country_message = "Country is required."

    # Getting data validations data from the form on add warehouse page

    zip_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[2]/span")
    city_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[3]/span")
    state_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[5]/span")
    country_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[6]/span")

    # Verifying data with the expected output
    if (zip_message.text == expected_zip_message and city_message.text == expected_city_message
            and state_message.text == expected_state_message and country_message.text == expected_country_message):

        assert True, f'''Validations are working properly {zip_message.text},
        {city_message.text}, {state_message.text}, {country_message.text}'''
    else:
        assert False, "Validations are not working properly "


@when(u'I enter city name "{city}"')
def step_impl(context, city):
    driver = context.driver
    # Clicking on add warehouse button
    driver.find_element(By.NAME, "avc").click()
    time.sleep(1)
    # Clicking on submit button without entering data on add warehouse window
    driver.find_element(By.ID, "en_wd_origin_city").clear()
    driver.find_element(By.ID, "en_wd_origin_city").send_keys(city)
    driver.find_element(By.NAME, "en_wd_submit_warehouse").click()


@when(u'I enter state name "{state}"')
def step_impl(context, state):
    driver = context.driver
    # Clicking on add warehouse button
    driver.find_element(By.NAME, "avc").click()
    time.sleep(1)
    driver.find_element(By.ID, "en_wd_origin_state").clear()
    driver.find_element(By.ID, "en_wd_origin_state").send_keys(state)
    driver.find_element(By.NAME, "en_wd_submit_warehouse").click()


@when(u'I enter country name "{country}"')
def step_impl(context, country):
    driver = context.driver
    # Clicking on add warehouse button
    driver.find_element(By.NAME, "avc").click()
    time.sleep(1)
    driver.find_element(By.ID, "en_wd_origin_country").clear()
    driver.find_element(By.ID, "en_wd_origin_country").send_keys(country)
    driver.find_element(By.NAME, "en_wd_submit_warehouse").click()


@then(u'Error message with required credentials')
def step_impl(context):
    driver = context.driver
    # Expected Validation Message
    expected_zip_message = "Zip is required."
    expected_city_message = "City is required."
    expected_state_message = "State is required."
    expected_country_message = "Country is required."

    # Getting Validation Message from form
    zip_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[2]/span")
    city_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[3]/span")
    state_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[5]/span")
    country_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/form/div[6]/span")

    # Verifying the error message
    if city_message.text != expected_city_message:
        if (zip_message.text == expected_zip_message and country_message.text == expected_country_message
                and state_message.text == expected_state_message):
            assert True, f'''this is the validation message 
                                {zip_message.text}, {state_message.text}, 
                                {country_message.text} '''
        else:
            assert False, f'Validations are not working properly '
    if state_message.text != expected_state_message:
        if (zip_message.text == expected_zip_message and country_message.text == expected_country_message
                and city_message.text == expected_city_message):
            assert True, f'''this is the validation message 
                                {zip_message.text}, {city_message.text}, 
                                {country_message.text} '''
        else:
            assert False, f'Validations are not working properly '
    if country_message.text != expected_country_message:
        if (zip_message.text == expected_zip_message and city_message.text == expected_city_message
                and state_message.text == expected_state_message):
            assert True, f'''this is the validation message 
                                {zip_message.text}, {city_message.text}, 
                                {state_message.text} '''
        else:
            assert False, f'Validations are not working properly '


@when(u'I click on add button and enter new zip code')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    all_zip = [30605, 30216, 30214, 30215, 54822, 30213, 35004, 99501, 85001, 71601, 90001]

    warehouse_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr/td[3]")
    dropship_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr/td[4]")
    zip_codes = []

    #getting warehouse zip codes
    for a in warehouse_codes:
        zip_codes.append(a.text)
    # getting dropship zip codes
    for b in dropship_codes:
        zip_codes.append(b.text)

    for num in zip_codes:
        for number in all_zip:
            if num == str(number):
                all_zip.remove(number)

    wait.until(EC.element_to_be_clickable((By.NAME, "avc"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "en_wd_origin_zip"))).clear()
    # driver.find_element(By.NAME, "en_wd_origin_zip").clear()
    wait.until(EC.visibility_of_element_located((By.NAME, "en_wd_origin_zip"))).send_keys(all_zip[0])
    wait.until(EC.visibility_of_element_located((By.NAME, "en_wd_origin_address"))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_warehouse"))).click()


@then(u'Warehouse successfully added')
def step_impl(context):

    driver = context.driver
    wait = WebDriverWait(driver, 10)

    message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/div/div[4]/p")))
    expected_message = "Success! New warehouse added successfully."

    if message.text == expected_message:
        assert True, "Warehouse added successfully"

    else:
        assert False, f"Error Adding Warehouse {message.text}"

    driver.quit()


@when(u'I click on add button and enter existing zip code')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    code = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr[1]/td[3]")))
    ids = code.text
    wait.until(EC.element_to_be_clickable((By.NAME, "avc"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_origin_zip"))).clear()
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_origin_zip"))).send_keys(ids)
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_origin_city"))).click()
    time.sleep(3)
    submit = wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_warehouse"))).click()


@then(u'Error zip code already exists')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[2]/div/div/div[1]")))
    expected_error_message = "Error! Zip code already exists."

    if error.text == expected_error_message:
        assert True, "Zip code already exists"
    else:
        assert False, f"Error! implementing this scenario{error.text}"


@when(u'I click on update button and enter new zip code')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    all_zip = [30605, 30216, 30214, 30215, 54822, 30213, 35004, 99501, 85001, 71601, 90001]

    warehouse_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr/td[3]")
    dropship_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr/td[4]")
    zip_codes = []

    #getting warehouse zip codes
    for a in warehouse_codes:
        zip_codes.append(a.text)
    # getting dropship zip codes
    for b in dropship_codes:
        zip_codes.append(b.text)

    for num in zip_codes:
        for number in all_zip:
            if num == str(number):
                all_zip.remove(number)

    row = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr[1]")))
    id = row.get_attribute('id')
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='{id}']/td[5]/a[1]/img"))).click()
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_origin_zip"))).clear()
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_origin_zip"))).send_keys(all_zip[0])
    wait.until(EC.element_to_be_clickable((By.ID, "en_wd_origin_city"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "en_wd_origin_city"))).click()
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_warehouse"))).click()


@then(u'Warehouse updated successfully')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    expected_message = "Success! Warehouse updated successfully."
    message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/div[5]/p")))

    if message.text == expected_message:
        assert True, f"This is the message {message.text}"
    else:
        assert False, f"wrong!! {message.text}"


@when(u'I click on delete button')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    code = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr[1]")
    identity = code.get_attribute('id')
    wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='{identity}']/td[5]/a[2]/img"))).click()


@then(u'Warehouse deleted successfully')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/div/div[3]/p")))
    expected_message = "Success! Warehouse deleted successfully."
    if message.text == expected_message:
        assert True, f"This is the message {message.text}"
    else:
        assert False, "Error deleting warehouse"


@then(u'Checking all placeholders are enabled and displayed')
def step_impl(context):
    driver = context.driver

    def placeholders_dropship(name, displayed, enabled):
        if displayed:
            assert True, f"{name} Placeholder is displayed "
        elif not displayed:
            assert False, f"{name} Placeholder is not Displayed"
        else:
            assert False, "Error finding element!!!"
        if enabled:
            assert True, f"{name} Placeholder is Enabled "
        elif not enabled:
            assert False, f"{name} Placeholder is not Enabled"
        else:
            assert False, "Error finding element!!!"

        nickname_displayed = driver.find_element(By.ID, "en_wd_dropship_nickname").is_displayed()
        nickname_enabled = driver.find_element(By.ID, "en_wd_dropship_nickname").is_enabled()
        nick_name = "Nickname "
        placeholders_dropship(nick_name, nickname_displayed, nickname_enabled)

        street_address_displayed = driver.find_element(By.ID, "en_wd_dropship_address").is_displayed()
        street_address_enabled = driver.find_element(By.ID, "en_wd_dropship_address").is_enabled()
        street_address_name = "Street Address "
        placeholders_dropship(street_address_name, street_address_displayed, street_address_enabled)

        zip_code_displayed = driver.find_element(By.ID, "en_wd_dropship_zip").is_displayed()
        zip_code_enabled = driver.find_element(By.ID, "en_wd_dropship_zip").is_enabled()
        zip_code_name = "Zip Code "
        placeholders_dropship(zip_code_name, zip_code_displayed, zip_code_enabled)

        city_displayed = driver.find_element(By.ID, "en_wd_dropship_city").is_displayed()
        city_enabled = driver.find_element(By.ID, "en_wd_dropship_city").is_enabled()
        city_name = "City "
        placeholders_dropship(city_name, city_displayed, city_enabled)

        state_displayed = driver.find_element(By.ID, "en_wd_dropship_state").is_displayed()
        state_enabled = driver.find_element(By.ID, "en_wd_dropship_state").is_enabled()
        state_name = "State "
        placeholders_dropship(state_name, state_displayed, state_enabled)

        country_displayed = driver.find_element(By.ID, "en_wd_dropship_country").is_displayed()
        country_enabled = driver.find_element(By.ID, "en_wd_dropship_country").is_enabled()
        country_name = "State "
        placeholders_dropship(country_name, country_displayed, country_enabled)

        is_address_miles_displayed = driver.find_element(By.ID, "instore-pickup-address").is_displayed()
        is_address_miles_enabled = driver.find_element(By.ID, "instore-pickup-address").is_enabled()
        is_address_miles_name = "In-Store offer delivery within miles "
        placeholders_dropship(is_address_miles_name, is_address_miles_displayed, is_address_miles_enabled)

        is_address_zip_displayed = driver.find_element(By.ID, "instore-pickup-zipmatch").is_displayed()
        is_address_zip_enabled = driver.find_element(By.ID, "instore-pickup-zipmatch").is_enabled()
        is_address_zip_name = "In-Store offer delivery if zip code matches "
        placeholders_dropship(is_address_zip_name, is_address_zip_displayed, is_address_zip_enabled)

        is_checkout_displayed = driver.find_element(By.ID, "instore-pickup-desc").is_displayed()
        is_checkout_zip_enabled = driver.find_element(By.ID, "instore-pickup-desc").is_enabled()
        is_checkout_zip_name = "In-Store Checkout  "
        placeholders_dropship(is_checkout_zip_name, is_checkout_displayed, is_checkout_zip_enabled)

        is_phone_displayed = driver.find_element(By.ID, "en-phone-number").is_displayed()
        is_phone_zip_enabled = driver.find_element(By.ID, "en-phone-number").is_enabled()
        is_phone_zip_name = "In-Store Phone Number "
        placeholders_dropship(is_phone_zip_name, is_phone_displayed, is_phone_zip_enabled)

        ld_address_miles_displayed = driver.find_element(By.ID, "local-delivery-address").is_displayed()
        ld_address_miles_enabled = driver.find_element(By.ID, "local-delivery-address").is_enabled()
        ld_address_miles_name = "Local Delivery offer delivery within miles "
        placeholders_dropship(ld_address_miles_name, ld_address_miles_displayed, ld_address_miles_enabled)

        ld_address_zip_displayed = driver.find_element(By.ID, "local-delivery-zipmatch").is_displayed()
        ld_address_zip_enabled = driver.find_element(By.ID, "local-delivery-zipmatch").is_enabled()
        ld_address_zip_name = "Local Delivery offer delivery if zip code matches "
        placeholders_dropship(ld_address_zip_name, ld_address_zip_displayed, ld_address_zip_enabled)

        ld_checkout_displayed = driver.find_element(By.ID, "local-delivery-desc").is_displayed()
        ld_checkout_zip_enabled = driver.find_element(By.ID, "local-delivery-desc").is_enabled()
        ld_checkout_zip_name = "Local Delivery Checkout  "
        placeholders_dropship(ld_checkout_zip_name, ld_checkout_displayed, ld_checkout_zip_enabled)

        ld_fee_displayed = driver.find_element(By.ID, "local-delivery-fee").is_displayed()
        ld_fee_enabled = driver.find_element(By.ID, "local-delivery-fee").is_enabled()
        ld_fee_name = "Local Delivery Fee  "
        placeholders_dropship(ld_fee_name, ld_fee_displayed, ld_fee_enabled)


@when(u'I Click on submit button without entering data in dropship')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a")))
    element.click()
    # time.sleep(50)
    wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship"))).click()
    # driver.find_element(By.NAME, "en_wd_submit_dropship").click()


@then(u'Validations will be displayed on dropship')
def step_impl(context):
    driver = context.driver

    expected_zip = 'Zip is required.'
    expected_city = 'City is required.'
    expected_state = 'State is required.'
    expected_country = 'Country is required.'

    zip_code = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[3]/span")
    city = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[4]/span")
    state = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[6]/span")
    country = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[7]/span")

    if (zip_code.text == expected_zip and city.text == expected_city
        and state.text == expected_state and country.text == expected_country):
        assert True, f" This is the validation message {zip_code.text}"
    else:
        assert False, "Validations are not working properly "


@when(u'I enter city name "{city}" in dropship')
def step_impl(context, city):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a")))
    element.click()
    driver.find_element(By.ID, "en_wd_dropship_city").send_keys(city)
    submit = wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship")))
    submit.click()
    # driver.find_element(By.ID, "en_wd_submit_dropship").click()


@when(u'I enter state name "{state}" in dropship')
def step_impl(context, state):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a")))
    element.click()
    # time.sleep(10)
    driver.find_element(By.ID, "en_wd_dropship_state").send_keys(state)
    # time.sleep(10)
    submit = wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship")))
    submit.click()
    # time.sleep(10)


@when(u'I enter country name "{country}" in dropship')
def step_impl(context, country):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a")))
    element.click()
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_dropship_country"))).send_keys(country)
    submit = wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship")))
    submit.click()


@when(u'I enter the zip code and check the local delivery checkbox')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a")))
    element.click()
    zip_code = '30605'
    driver.find_element(By.ID, "en_wd_dropship_zip").send_keys(zip_code)
    driver.find_element(By.NAME, "en_wd_dropship_city").click()
    time.sleep(3)
    local_delivery = driver.find_element(By.ID, "enable-local-delivery").is_selected()

    if not local_delivery:
        local_delivery_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[17]/div/input"))).click()
        local_delivery = driver.find_element(By.ID, "enable-local-delivery").is_selected()
        # assert False, f"This is the status of local delivery checkbox {local_delivery}"
        submit = wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship")))
        submit.click()
        time.sleep(5)


@then(u'Error message with required credentials dropship')
def step_impl(context):
    driver = context.driver
    # Expected Validation Message
    expected_zip_message = "Zip is required."
    expected_city_message = "City is required."
    expected_state_message = "State is required."
    expected_country_message = "Country is required."
    expected_local_delivery = "Local delivery fee is required."

    # Getting Validation Message from form
    zip_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[3]/span")
    city_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[4]/span")
    state_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[6]/span")
    country_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[7]/span")
    local_delivery = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/form/div[21]/span")


    if city_message.text != expected_city_message:

        if (zip_message.text == expected_zip_message and country_message.text == expected_country_message
                and state_message.text == expected_state_message):
            assert True, f'''this is the validation message 
                                 {zip_message.text}, {state_message.text}, 
                                 {country_message.text} '''

        elif local_delivery.text == expected_local_delivery:
            assert True, f"This is the local delivery message {local_delivery.text}"

        else:
            assert False, f'Validations are not working properly {local_delivery.text}'

    if state_message.text != expected_state_message:

        if (zip_message.text == expected_zip_message and country_message.text == expected_country_message
                and city_message.text == expected_city_message):
            assert True, f'''this is the validation message
                                 {zip_message.text}, {city_message.text},
                                 {country_message.text} '''
        elif local_delivery.text == expected_local_delivery:
            assert True, f"This is the local delivery message {local_delivery.text}"

        else:
            assert False, f'Validations are not working properly {local_delivery.text} '

    if country_message.text != expected_country_message:
        if (zip_message.text == expected_zip_message and city_message.text == expected_city_message
                and state_message.text == expected_state_message):
            assert True, f'''this is the validation message
                                 {zip_message.text}, {city_message.text},
                                 {state_message.text} '''
        elif local_delivery.text == expected_local_delivery:
            assert True, f"This is the local delivery message {local_delivery.text}"

        else:
            assert False, f'Validations are not working properly {zip_message.text}'


@when(u'I click on add button and enter zip code dropship')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    all_zip = [30605, 30216, 30214, 30215, 54822, 30213, 35004, 99501, 85001, 71601, 90001]

    warehouse_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr/td[3]")
    dropship_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr/td[4]")
    zip_codes = []

    #getting warehouse zip codes
    for a in warehouse_codes:
        zip_codes.append(a.text)
    # getting dropship zip codes
    for b in dropship_codes:
        zip_codes.append(b.text)

    for num in zip_codes:
        for number in all_zip:
            if num == str(number):
                all_zip.remove(number)
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_dropship_zip"))).send_keys(all_zip[0])
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_dropship_city"))).click()
    # driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a").click()
    # driver.find_element(By.ID, "en_wd_dropship_zip").send_keys(all_zip[0])
    driver.find_element(By.ID, "en_wd_dropship_city").click()
    time.sleep(4)
    # driver.find_element(By.NAME, "en_wd_submit_dropship").click()
    wait.until(EC.visibility_of_element_located((By.NAME, "en_wd_submit_dropship"))).click()




@then(u'Dropship Successfully Added')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    expected_message = "Success! New drop ship added successfully."
    success = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/div/div[3]/p")))
    # expected_error_message = "Error! Zip code already exists."
    # error = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/div[3]/div[3]/div/div/div[1]")
    if success.text == expected_message:
        assert True, f"Dropship Added successfully"
    # elif error.text == expected_error_message:
    #     assert False, "Zip Code already exists"
    else:
        assert False, "Error Adding dropship"


@when(u'I click on add button and enter zip code')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    # code = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr[1]/td[3]")
    # code = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]")))
    code = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr[1]/td[3]")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/a"))).click()
    zip_code = code.text
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_dropship_zip"))).send_keys(zip_code)
    wait.until(EC.element_to_be_clickable((By.ID, "en_wd_dropship_city"))).click()
    time.sleep(4)
    element = wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship"))).click()


@then(u'Error zip code of dropship already exists')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[3]/div/div/div[1]")))
    expected_message = "Error! Zip code already exists."
    if message.text == expected_message:
        assert True, f"Zip code already exists "
    else:
        assert False, f"This is the error message {message.text}"


@when(u'I click on update button and enter zip code')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    all_zip = [30605, 30216, 30214, 30215, 54822, 30213, 35004, 99501, 85001, 71601, 90001]

    warehouse_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[1]/table/tbody/tr/td[3]")
    dropship_codes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr/td[4]")
    zip_codes = []

    # getting warehouse zip codes
    for a in warehouse_codes:
        zip_codes.append(a.text)
    # getting dropship zip codes
    for b in dropship_codes:
        zip_codes.append(b.text)

    for num in zip_codes:
        for number in all_zip:
            if num == str(number):
                all_zip.remove(number)

    code = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[1]")))
    id = code.get_attribute('id')
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='{id}']/td[6]/a[1]/img"))).click()
    driver.find_element(By.XPATH, f"//*[@id='{id}']/td[6]/a[1]/img").click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_dropship_zip"))).clear()
    wait.until(EC.visibility_of_element_located((By.ID, "en_wd_dropship_zip"))).send_keys(all_zip[0])
    wait.until(EC.element_to_be_clickable((By.ID, "en_wd_dropship_city"))).click()
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.NAME, "en_wd_submit_dropship"))).click()


@then(u'Dropship updated successfully')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    expected_mess = "Success! Drop ship updated successfully."
    message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/div[4]/p")))

    if message.text == expected_mess:
        assert True, f"Dropship updated successfully {message.text}"
    else:
        assert False, "Error Updating Dropship"


@when(u'I click on delete button in dropship')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    code = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/table/tbody/tr[1]")))
    # code = driver.find_element
    id = code.get_attribute('id')
    delete_icon = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='{id}']/td[6]/a[2]/img")))
    delete_icon.click()
    # message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[3]/div[3]/div[1]/div/p")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[1]/div/div/a[2]").click()


@then(u'Dropship deleted successfully')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    expected_delete_message = "Success! Drop ship deleted successfully."
    deleting_message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div[3]/div[2]/div/div[5]/p")))
    if deleting_message.text == expected_delete_message:
        assert True, f" This is the message {deleting_message.text}"
    else:
        assert False, f"Deleting dropship message is not appeared {deleting_message.text}"
