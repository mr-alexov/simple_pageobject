import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class DemoQAForm:
    """Page Object for DemoQA Practice Form"""

    # URL
    URL = "https://demoqa.com/automation-practice-form"

    # Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    SUBMIT_BUTTON = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Open the practice form page"""
        self.driver.get(self.URL)
        time.sleep(2)  # Wait for page to load
        self.driver.execute_script("$('#fixedban').remove()")
        self.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, first_name):
        """Fill first name field"""
        element = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        element.clear()
        element.send_keys(first_name)

    def fill_last_name(self, last_name):
        """Fill last name field"""
        element = self.driver.find_element(*self.LAST_NAME)
        element.clear()
        element.send_keys(last_name)

    def fill_email(self, email):
        """Fill email field"""
        element = self.driver.find_element(*self.EMAIL)
        element.clear()
        element.send_keys(email)

    def select_gender(self, gender):
        """Select gender radio button
        Args:
            gender: 'male' or 'female'
        """
        if gender.lower() == 'male':
            element = self.driver.find_element(*self.GENDER_MALE)
        else:
            element = self.driver.find_element(*self.GENDER_FEMALE)
        element.click()

    def fill_mobile(self, mobile):
        """Fill mobile number field"""
        element = self.driver.find_element(*self.MOBILE)
        element.clear()
        element.send_keys(mobile)

    def fill_date_of_birth(self, date):
        """Fill date of birth
        Args:
            date: date string in format 'DD MMM YYYY' (e.g., '15 Jan 1990')
        """
        element = self.driver.find_element(*self.DATE_OF_BIRTH)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def fill_subjects(self, subjects):
        """Fill subjects field
        Args:
            subjects: list of subjects (e.g., ['Maths', 'Physics'])
        """
        element = self.driver.find_element(*self.SUBJECTS)
        for subject in subjects:
            element.send_keys(subject)
            element.send_keys(Keys.ENTER)

    def select_hobbies(self, hobbies):
        """Select hobbies checkboxes
        Args:
            hobbies: list of hobbies from ['sports', 'reading', 'music']
        """
        hobby_map = {
            'sports': self.HOBBIES_SPORTS,
            'reading': self.HOBBIES_READING,
            'music': self.HOBBIES_MUSIC
        }
        for hobby in hobbies:
            element = self.driver.find_element(*hobby_map[hobby.lower()])
            element.click()

    def fill_current_address(self, address):
        """Fill current address field"""
        element = self.driver.find_element(*self.CURRENT_ADDRESS)
        element.clear()
        element.send_keys(address)

    def select_state(self, state):
        """Select state from dropdown
        Args:
            state: state name (e.g., 'NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan')
        """
        element = self.driver.find_element(*self.STATE)
        element.click()
        state_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{state}']"))
        )
        state_option.click()

    def select_city(self, city):
        """Select city from dropdown
        Args:
            city: city name (depends on selected state)
        """
        element = self.driver.find_element(*self.CITY)
        element.click()
        city_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{city}']"))
        )
        city_option.click()

    def submit_form(self):
        """Click submit button"""
        element = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def fill_complete_form(self, data):
        """Fill all form fields with provided data
        Args:
            data: dictionary with form data
        """
        self.fill_first_name(data.get('first_name', ''))
        self.fill_last_name(data.get('last_name', ''))
        self.fill_email(data.get('email', ''))
        self.select_gender(data.get('gender', 'male'))
        self.fill_mobile(data.get('mobile', ''))

        if 'date_of_birth' in data:
            self.fill_date_of_birth(data['date_of_birth'])

        if 'subjects' in data:
            self.fill_subjects(data['subjects'])

        if 'hobbies' in data:
            self.select_hobbies(data['hobbies'])

        self.fill_current_address(data.get('current_address', ''))

        if 'state' in data:
            self.select_state(data['state'])

        if 'city' in data:
            self.select_city(data['city'])

    def is_results_modal_displayed(self):
        """Check if the results modal is displayed
        Returns:
            bool: True if modal is visible, False otherwise
        """
        try:
            modal = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
            )
            return modal.is_displayed()
        except:
            return False
