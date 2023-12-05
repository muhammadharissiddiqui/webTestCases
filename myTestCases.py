from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import unittest


class HospitalManagementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # Specify the path to your ChromeDriver executable
        chrome_driver_path = "C:\\browserdrivers\\chromedriver.exe"

        # Initialize WebDriver instance and store it as a class attribute
        cls.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        # Note: Ensure that the URL includes the protocol (http/https)
        cls.base_url = "http://localhost:8080/HospitalManagement/"

    @classmethod
    def tearDownClass(cls):
        # Close the browser after all tests are done
        cls.driver.quit()

    def setUp(self):
        # Additional setup tasks for each test case (if any)
        pass

    def test_login_successful(self):
        # Perform login with valid credentials
        self.driver.get(self.base_url + "/login.php")
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_css_selector("input[type='submit']")

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        submit_button.click()

        # Verify redirection to the dashboard
        self.assertEqual(self.driver.current_url, "http://localhost:8080/HospitalManagement/admin-panel.php#app-hist")

    def test_login_failed(self):
        self.driver.get(self.base_url + "/login.php")
        # Perform login with invalid credentials
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_css_selector("input[type='submit']")

        username_input.send_keys("invalid_username")
        password_input.send_keys("invalid_password")
        submit_button.click()

        # Check if the error message is displayed
        error_message = self.driver.find_element_by_css_selector("p[style='color: red;']").text
        self.assertEqual(error_message, "Invalid username or password. Please try again.")

    def test_add_patient(self):
        self.driver.get(self.base_url + "/dashboard.php")
        # Add a patient to the system
        patient_name_input = self.driver.find_element_by_name("patient_name")
        patient_age_input = self.driver.find_element_by_name("patient_age")
        add_patient_button = self.driver.find_element_by_css_selector("input[value='Add Patient']")

        patient_name_input.send_keys("John Doe")
        patient_age_input.send_keys("30")
        add_patient_button.click()

        # Check if the success message is displayed
        success_message = self.driver.find_element_by_css_selector("p[style='color:lightgreen']").text
        self.assertEqual(success_message, "Patient added successfully.")

    def test_schedule_appointment(self):
        self.driver.get(self.base_url + "/dashboard.php")
        # Schedule an appointment for a patient
        patient_select = self.driver.find_element_by_name("patient_id")
        appointment_date_input = self.driver.find_element_by_name("appointment_date")
        schedule_button = self.driver.find_element_by_css_selector("input[value='Schedule Appointment']")

        # Assume a patient is already added, so select the patient from the dropdown
        patient_select.select_by_visible_text("John Doe")
        appointment_date_input.send_keys("2023-01-01")  # Replace with a valid date
        schedule_button.click()

        # Check if the success message is displayed
        success_message = self.driver.find_element_by_css_selector("p[style='color:lightgreen']").text
        self.assertEqual(success_message, "Appointment scheduled successfully.")

    

if __name__ == "__main__":
    unittest.main()
