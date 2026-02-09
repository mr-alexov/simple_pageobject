from pages.registration_form import DemoQAForm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



    
def test_fill_basic_fields(browser):
    """Test filling basic form fields"""
    form = DemoQAForm(browser)
    form.open()

    form.fill_first_name("John")
    form.fill_last_name("Doe")
    form.fill_email("john.doe@example.com")
    form.select_gender("male")
    form.fill_mobile("1234567890")

    # Verify fields are filled
    assert browser.find_element(By.ID, "firstName").get_attribute("value") == "John"
    assert browser.find_element(By.ID, "lastName").get_attribute("value") == "Doe"
    assert browser.find_element(By.ID, "userEmail").get_attribute("value") == "john.doe@example.com"

def test_fill_complete_form(browser):
    """Test filling the complete form"""
    form = DemoQAForm(browser)
    form.open()

    form_data = {
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane.smith@test.com',
        'gender': 'female',
        'mobile': '9876543210',
        'date_of_birth': '15 Jan 1990',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['reading', 'music'],
        'current_address': '123 Main Street, Apartment 4B',
        'state': 'NCR',
        'city': 'Delhi'
    }

    form.fill_complete_form(form_data)

    # Verify some fields
    assert browser.find_element(By.ID, "firstName").get_attribute("value") == "Jane"
    assert browser.find_element(By.ID, "userEmail").get_attribute("value") == "jane.smith@test.com"
    assert browser.find_element(By.ID, "userNumber").get_attribute("value") == "9876543210"

def test_select_hobbies(browser):
    """Test selecting multiple hobbies"""
    form = DemoQAForm(browser)
    form.open()

    form.select_hobbies(['sports', 'reading', 'music'])

    # Verify checkboxes are checked
    sports_checkbox = browser.find_element(By.ID, "hobbies-checkbox-1")
    reading_checkbox = browser.find_element(By.ID, "hobbies-checkbox-2")
    music_checkbox = browser.find_element(By.ID, "hobbies-checkbox-3")

    assert sports_checkbox.is_selected()
    assert reading_checkbox.is_selected()
    assert music_checkbox.is_selected()

def test_fill_and_submit_form(browser):
    """Test filling and submitting the form"""
    form = DemoQAForm(browser)
    form.open()

    form_data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test.user@example.com',
        'gender': 'male',
        'mobile': '5555555555',
        'current_address': '456 Test Avenue'
    }

    form.fill_complete_form(form_data)
    form.submit_form()

    # Wait for and verify submission modal appears

    assert form.is_results_modal_displayed()

def test_state_and_city_selection(browser):
    """Test selecting state and city dropdowns"""
    form = DemoQAForm(browser)
    form.open()

    form.select_state("Haryana")
    form.select_city("Karnal")

    # Verify selections by checking the dropdown text
    state_text = browser.find_element(By.XPATH, "//div[@id='state']//div[contains(@class, 'singleValue')]").text
    city_text = browser.find_element(By.XPATH, "//div[@id='city']//div[contains(@class, 'singleValue')]").text

    assert state_text == "Haryana"
    assert city_text == "Karnal"
