import allure
from allure_commons.types import Severity

from model.pages.registration_page import StudentRegistrationPage


def test_student_registration_form():
    allure.dynamic.title("Student Registration Form test")
    allure.dynamic.tag("Web Interface")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label("owner", "SergeyG")
    allure.dynamic.feature("Forms tab")
    allure.dynamic.story("Verify that users can register a student")
    allure.dynamic.link("https://demoqa.com/automation-practice-form", name="Practice Form Page")

    registration_page = StudentRegistrationPage()
    with allure.step("Opening Practice Form Page"):
        registration_page.open()

    with allure.step("Filling first name field"):
        registration_page.fill_first_name("Stefan")
    with allure.step("Filling last  name field"):
        registration_page.fill_last_name("Burnett")
    with allure.step("Filling email field"):
        registration_page.fill_email("mcride_dg@gmail.com")
    with allure.step("Selecting gender"):
        registration_page.select_gender("Male")
    with allure.step("Filling mobile number"):
        registration_page.fill_mobile_number("7148088000")
    with allure.step("Selecting date of birth"):
        registration_page.fill_date_of_birth("1978", "May", "10")
    with allure.step("Adding subject"):
        registration_page.fill_subjects("Chemistry")
    with allure.step("Selecting hobbies"):
        registration_page.select_hobbies("Music")
    with allure.step("Attaching picture"):
        registration_page.select_picture("mc_ride.png")
    with allure.step("Filling current address"):
        registration_page.fill_current_address("888 East Las Olas Blvd, Suite 710")
    with allure.step("Selecting state and city"):
        registration_page.select_state_and_city("NCR", "Delhi")
    with allure.step("Submitting form"):
        registration_page.submit_form()

    with allure.step("Verifying that result form has entered user info"):
        registration_page.should_have_registered(full_name="Stefan Burnett",
                                                 email="mcride_dg@gmail.com",
                                                 gender="Male",
                                                 mobile_number="7148088000",
                                                 birthday="10 May,1978",
                                                 subjects="Chemistry",
                                                 hobbies="Music",
                                                 picture="mc_ride.png",
                                                 address="888 East Las Olas Blvd, Suite 710",
                                                 state_city="NCR Delhi")
