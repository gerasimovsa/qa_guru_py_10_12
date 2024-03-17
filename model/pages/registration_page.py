from selene import browser, be, have, by, command

from model.pages import resource


class StudentRegistrationPage:
    def __init__(self):
        self.submit_button = browser.element("#submit")

    def open(self):
        browser.open("/automation-practice-form")
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value: str):
        browser.element("#firstName").should(be.blank).type(value)
        return self

    def fill_last_name(self, value: str):
        browser.element("#lastName").should(be.blank).type(value)
        return self

    def fill_email(self, value: str):
        browser.element("#userEmail").should(be.blank).type(value)
        return self

    def select_gender(self, value: str):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile_number(self, value: str):
        browser.element("#userNumber").should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year: str, month: str, day: str):
        browser.element("#dateOfBirthInput").click()
        browser.element("[class='react-datepicker__year-select']").click()
        browser.element(by.text(year)).click()
        browser.element("[class='react-datepicker__month-select']").click()
        browser.element(by.text(month)).click()
        browser.element(f"[class = 'react-datepicker__day react-datepicker__day--0{day}']").click()
        return self

    def fill_subjects(self, value: str):
        browser.element("#subjectsInput").should(be.blank).type(value)
        browser.element("#react-select-2-option-0").click()
        return self

    def select_hobbies(self, value: str):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def select_picture(self, path: str):
        browser.element("#uploadPicture").send_keys(resource.path(path))
        return self

    def fill_current_address(self, value: str):
        browser.element("#currentAddress").should(be.blank).type(value)
        return self

    def select_state_and_city(self, state: str, city: str):
        self.submit_button.perform(command.js.scroll_into_view)
        browser.element("#state").click()
        browser.element(by.text(state)).click()
        browser.element("#city").click()
        browser.element(by.text(city)).click()
        return self

    def submit_form(self):
        self.submit_button.click()
        return self

    def should_have_registered(self, full_name, email, gender, mobile_number
                               , birthday, subjects, hobbies, picture, address, state_city):
        browser.element(".table").should(be.present)
        browser.all('tr td:first-child + td').should(have.exact_texts(full_name,
                                                                      email,
                                                                      gender,
                                                                      mobile_number,
                                                                      birthday,
                                                                      subjects,
                                                                      hobbies,
                                                                      picture,
                                                                      address,
                                                                      state_city))
