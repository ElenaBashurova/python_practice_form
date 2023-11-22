from selene import browser, have, by
import os



def test_student_registration(browser_management_demoqa):
    browser.open('/')

    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').type('Romanov')
    browser.element('#lastName').type('Ivan')
    browser.element('#userEmail').type('romanov.i@mail.com')
    browser.element('#gender-radio-1').double_click()

    browser.element('#userNumber').type('9087658909')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('February')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2002')).click()
    browser.element('.react-datepicker__day--006').click()
    browser.element('#subjectsInput').type('new').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/images.jpeg'))
    browser.element('#currentAddress').type('city Moscow, street Lenina')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    #Проверка данных
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text(
        'Romanov Ivan'
        and 'romanov.i@mail.com'
        and '9087658909'
        and '11 Nov 1992'
        and 'Haryana Karnal'))

    browser.element('.modal-footer').click()


