import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'I Click on quote settings page link')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/ul/li[2]/a").click()


@then(u'I verify rad link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[4]/tbody/tr[3]/td/p/a[1]"))).click()
    expected_url = "https://eniture.com/woocommerce-residential-address-detection/"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f" Residential delivery link is working fine {url}"
    else:
        assert False, f"Residential delivery Link is not working fine {url}"


@then(u'I verify rad learn more link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[4]/tbody/tr[3]/td/p/a[2]"))).click()
    expected_url = "https://eniture.com/woocommerce-residential-address-detection/#documentation"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f" Residential delivery learn more link is working fine {url}"
    else:
        assert False, f"Residential delivery learn more Link is not working fine {url}"


@then(u'I verify lift gate link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[4]/tbody/tr[7]/td/p/a[1]"))).click()
    expected_url = "https://eniture.com/woocommerce-residential-address-detection/"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f"Lift gate link is working fine {url}"
    else:
        assert False, f"Lift gate link is not working fine {url}"


@then(u'I verify lift gate learn more link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[4]/tbody/tr[7]/td/p/a[2]"))).click()
    expected_url = "https://eniture.com/woocommerce-residential-address-detection/#documentation"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f" lift gate learn more link is working fine {url}"
    else:
        assert False, f"lift gate learn more link is not working fine {url}"


@then(u'I verify freight direct link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/div/p/a"))).click()
    expected_url = "https://www.fedex.com/en-us/shipping/freight-services/ltl/freight-direct.html"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f" Residential delivery learn more link is working fine {url}"
    else:
        assert False, f"Residential delivery learn more Link is not working fine {url}"


@then(u'I verify freight direct services link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[1]/td/p/a[1]"))).click()
    expected_url = "https://eniture.com/woocommerce-residential-address-detection/"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f" freight direct services link is working fine {url}"
    else:
        assert False, f"freight direct services link is not working fine {url}"


@then(u'I verify shipping slug link')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[15]/td/p/a"))).click()
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=shipping&section=classes"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    url = driver.current_url

    if url == expected_url:
        assert True, f" freight direct services link is working fine {url}"
    else:
        assert False, f"freight direct services link is not working fine {url}"


@then(u'I Verify all placeholders')
def step_impl(context):
    driver = context.driver

    def placeholders(name, displayed, enabled):
        if displayed:
            assert True, f"{name} Placeholder is displayed"
        else:
            assert False, f"{name} Placeholder is not displayed"

        if enabled:
            assert True, f"{name} Placeholder is displayed"
        else:
            assert False, f"{name} Placeholder is not displayed"

    fedex_economy_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[2]/tbody/tr[2]/td/input").is_displayed()
    fedex_economy_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[2]/tbody/tr[2]/td/input").is_enabled()
    name = 'Fedex freight economy'
    placeholders(name, fedex_economy_displayed, fedex_economy_enabled)

    hold_at_terminal_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[4]/tbody/tr[9]/td/input").is_displayed()
    hold_at_terminal_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[4]/tbody/tr[9]/td/input").is_enabled()
    terminal_name ='Hold at terminal'
    placeholders(terminal_name, hold_at_terminal_displayed, hold_at_terminal_enabled)

    fedex_economy_basic_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[3]/td/input").is_displayed()
    fedex_economy_basic_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[3]/td/input").is_enabled()
    fedex_economy_basic_name ='Fedex economy basic displayed'
    placeholders(fedex_economy_basic_name, fedex_economy_basic_displayed, fedex_economy_basic_enabled)

    fedex_priority_basic_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[4]/td/input").is_displayed()
    fedex_priority_basic_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[4]/td/input").is_enabled()
    fedex_priority_basic_name ='Fedex priority basic displayed'
    placeholders(fedex_priority_basic_name, fedex_priority_basic_displayed, fedex_priority_basic_enabled)

    economy_basic_by_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[5]/td/input").is_displayed()
    economy_basic_by_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[5]/td/input").is_enabled()
    economy_basic_by_name ='Fedex economy basic by appointment displayed'
    placeholders(economy_basic_by_name, economy_basic_by_displayed, economy_basic_by_enabled)

    priority_basic_by_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[6]/td/input").is_displayed()
    priority_basic_by_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[6]/td/input").is_enabled()
    priority_basic_by_name ='Fedex priority basic by appointment displayed'
    placeholders(priority_basic_by_name, priority_basic_by_displayed, priority_basic_by_enabled)

    direct_standard_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[7]/td/input").is_displayed()
    direct_premium_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[7]/td/input").is_enabled()
    direct_premium_name ='Fedex direct priority standard displayed'
    placeholders(direct_premium_name, direct_standard_displayed, direct_premium_enabled)

# fedex freight direct surcharges placeholders status
    basic_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[18]/td/input").is_displayed()
    basic_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[18]/td/input").is_enabled()
    basic_name = "fedex freight direct surcharges basic"
    placeholders( basic_name, basic_displayed, basic_enabled)

    basic_by_appointment_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[19]/td/input").is_displayed()
    basic_by_appointment_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[19]/td/input").is_enabled()
    basic_by_appointment_name = "fedex freight direct surcharges basic by appointment"
    placeholders(basic_by_appointment_name, basic_by_appointment_displayed, basic_by_appointment_enabled)

    standard_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[20]/td/input").is_displayed()
    standard_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[20]/td/input").is_enabled()
    standard_name = "fedex freight direct surcharges standard"
    placeholders(standard_name, standard_displayed, standard_enabled)

    premium_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[21]/td/input").is_displayed()
    premium_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[5]/tbody/tr[21]/td/input").is_enabled()
    premium_name = "fedex freight direct surcharges premium"
    placeholders(premium_name, premium_displayed, premium_enabled)

    handling_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[14]/td/input").is_displayed()
    handling_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[14]/td/input").is_enabled()
    handling_name = "Handling Fee"
    placeholders(handling_name, handling_displayed, handling_enabled)

    ignore_items_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[15]/td/input").is_displayed()
    ignore_items_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[15]/td/input").is_enabled()
    ignore_items_name = "Ignore items with following shipping classes"
    placeholders(ignore_items_name, ignore_items_displayed, ignore_items_enabled)

    allow_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[1]/label/textarea").is_displayed()
    allow_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[1]/label/textarea").is_enabled()
    allow_name = "Allow user to continue to check out and display this message"
    placeholders(allow_name, allow_displayed, allow_enabled)

    prevent_displayed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[2]/label/textarea").is_displayed()
    prevent_enabled = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[2]/label/textarea").is_enabled()
    prevent_name = "Prevent user from checking out and display this message"
    placeholders(prevent_name, prevent_displayed, prevent_enabled)


@then(u'I click on select all checkbox all checkboxes would be checked')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    select_all = wait.until(EC.visibility_of_element_located((By.ID, "direct_select_fedex_freight_services"))).is_selected()

    if not select_all:
        wait.until(EC.element_to_be_clickable((By.NAME, "direct_select_fedex_freight_services"))).click()

    fedex_freight = driver.find_elements(By.XPATH, "//input[@class='ffd_s']")

    for a in fedex_freight:
        names = a.get_attribute("id")
        status = wait.until(EC.visibility_of_element_located((By.ID, names))).is_selected()
        # assert False, f"{status} is the status of {names} checkbox"
        if status:
            assert True, "Select all checkbox is working fine"
        else:
            assert False, f"{names} checkbox is not checked when clicked on select all checkbox"

    select_all_checkbox = driver.find_element(By.ID, "all_shipment_days_fedex_ltl").is_selected()
    if not select_all_checkbox:
        wait.until(EC.element_to_be_clickable((By.ID, "all_shipment_days_fedex_ltl"))).click()

    for r in range(7, 12):

        days = driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[{r}]/td/fieldset/label/input").is_selected()
        if days:
            assert True, f"Select all checkboxes are working fine "
        else:
            assert False, f"{days} Checkbox is not checked on clicking select all checkbox"


@when(u'I verify all checkboxes are displayed enabled and selected')
def step_impl(context):
    driver = context.driver

    # Function that checks the checkboxes are enabled displayed and selected is working fine

    def quote_checkboxes(checkbox_name, enabled, displayed, selected_state, ids):
        if displayed:
            assert True, f"{checkbox_name} checkbox is displayed"
        else:
            assert False, f"{checkbox_name} checkbox is not displayed"
        if enabled:
            assert True, f"{checkbox_name} checkbox is enabled"
        else:
            assert False, f"{checkbox_name} checkbox is not enabled"

        if selected_state:
            driver.find_element(By.ID, ids).click()
            selected_state = driver.find_element(By.ID, ids).is_selected()
            if not selected_state:
                assert True, f"{checkbox_name} checkbox is selection is working fine"
            else:
                assert False, f"{checkbox_name} checkbox selection is not working fine"
        elif not selected_state:
            driver.find_element(By.ID, ids).click()
            selected_state = driver.find_element(By.ID, ids).is_selected()
            if selected_state:
                assert True, f"{checkbox_name} checkbox is selection is working fine"
            else:
                assert False, f"{checkbox_name} checkbox selection is not working fine"

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for a in checkboxes:
        identities = a.get_attribute('id')
        display = driver.find_element(By.ID, identities).is_displayed()
        enable = driver.find_element(By.ID, identities).is_enabled()
        selected = driver.find_element(By.ID, identities).is_selected()
        name = a.get_attribute('name')
        quote_checkboxes(name, enable, display, selected, identities)


@when(u'I verify all the radio buttons are enabled')
def step_impl(context):

    driver = context.driver

    def quote_radio(name, displayed, enabled):

        if displayed:
            assert True, f"{name} radio button is displayed"
        else:
            assert False, f"{name} radio button is not displayed"

        if enabled:
            assert True, f"{name} radio button is enabled"
        else:
            assert False, f"{name} radio button is not enabled"

    radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

    for b in radio_buttons:
        values = b.get_attribute("value")
        display = driver.find_element(By.XPATH, f"//input[@value='{values}']").is_displayed()
        enable = driver.find_element(By.XPATH, f"//input[@value='{values}']").is_displayed()
        select = driver.find_element(By.XPATH, f"//input[@value='{values}']").is_selected()
        radio_name = b.get_attribute("name")
        quote_radio(radio_name, display, enable)


@when(u'I verify all radio buttons are working properly')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    discount_negotiated = driver.find_element(By.XPATH, "//input[@value='prevent']").is_selected()
    discount_promotional = driver.find_element(By.XPATH, "//input[@value='allow']").is_selected()
    discount_placeholder = driver.find_element(By.XPATH, "//input[@id='fedex_freight_discount_percent']").is_enabled()

    if not discount_negotiated:
        driver.find_element(By.XPATH, "//input[@value='prevent']").click()
        discount_negotiated = driver.find_element(By.XPATH, "//input[@value='prevent']").is_selected()
        if discount_negotiated == True and discount_promotional == False and discount_placeholder == False:
            assert False, f"Discount radio buttons are working fine "
        else:
            assert False, f"Discount radio buttons are not working fine "

    if discount_negotiated:
        driver.find_element(By.XPATH, "//input[@value='allow']").click()
        discount_negotiated = driver.find_element(By.XPATH, "//input[@value='prevent']").is_selected()
        discount_promotional = driver.find_element(By.XPATH, "//input[@value='allow']").is_selected()
        discount_placeholder = driver.find_element(By.XPATH, "//input[@id='fedex_freight_discount_percent']").is_enabled()

        if discount_promotional == True and discount_placeholder == True and discount_negotiated == False:
            assert True, f"Discount radio buttons are working fine "
        else:
            assert False, f"Discount radio buttons are not working fine "

        dont_show_estimate = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[1]/label/input").is_selected()
        estimate_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[2]/label/input").is_selected()
        estimate_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[3]/label/input").is_selected()

        if not dont_show_estimate:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[1]/label/input").click()
            dont_show_estimate = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[1]/label/input").is_selected()
            estimate_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[2]/label/input").is_selected()
            estimate_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[3]/label/input").is_selected()
            cut_off = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[5]/td/input").is_enabled()
            offset_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[6]/td/input").is_enabled()

            if dont_show_estimate == True and estimate_days == False and estimate_date == False and cut_off == False and offset_days == False:
                assert True, f"Delivery estimates radio buttons are working fine"
            else:
                assert False, f"Delivery estimates radio buttons are not working fine the status of the radio buttons are {dont_show_estimate} {estimate_days} {estimate_date}"

        elif not estimate_days:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[2]/label/input").click()
            estimate_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[2]/label/input").is_selected()
            dont_show_estimate = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[1]/label/input").is_selected()
            estimate_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[3]/label/input").is_selected()
            cut_off = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[5]/td/input").is_enabled()
            offset_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[6]/td/input").is_enabled()

            if estimate_days == True and cut_off == True and offset_days == True and dont_show_estimate == False and estimate_date == False:
                assert True, f"Delivery estimates radio buttons are working fine"
            else:
                assert False, f"Delivery estimates radio buttons are not working fine the status of the radio buttons are {dont_show_estimate} {estimate_days} {estimate_date}"

        elif not estimate_date:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[3]/label/input").click()
            estimate_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[3]/label/input").is_selected()
            estimate_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[2]/label/input").is_selected()
            dont_show_estimate = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[3]/td/fieldset/ul/li[1]/label/input").is_selected()
            cut_off = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[5]/td/input").is_enabled()
            offset_days = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[6]/tbody/tr[6]/td/input").is_enabled()

            if estimate_date == True and cut_off == True and offset_days == True and dont_show_estimate == False and estimate_days == False:
                assert True, f"Delivery estimates radio buttons are working fine"
            else:
                assert False, f"Delivery estimates radio buttons are not working fine the status of the radio buttons are {dont_show_estimate} {estimate_days} {estimate_date}"

            allow = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[1]/label/input").is_selected()
            prevent = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[2]/label/input").is_selected()

            if not allow:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[1]/label/input").click()
                allow = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[1]/label/input").is_selected()
                prevent = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[2]/label/input").is_selected()
                if allow == True and prevent == False:
                    assert True, f'Allow radio button is working fine '
                else:
                    assert False, f"Allow radio button is not working fine this is the status of radio button {allow} {prevent}"

            if not prevent:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[2]/label/input").click()
                prevent = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[2]/label/input").is_selected()
                allow = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div[2]/table[7]/tbody/tr[2]/td/fieldset/ul/li[1]/label/input").is_selected()
                if prevent == True and allow == False:
                    assert True, f'Allow radio button is working fine '
                else:
                    assert False, f"Allow radio button is not working fine this is the status of radio button {allow} {prevent}"

