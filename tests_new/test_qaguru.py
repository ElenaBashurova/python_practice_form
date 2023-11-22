from selene import browser, have, by
import os



def test_student_registration(browser_management_qaguru):
    browser.open('/')
    browser.wait_until(5)
    browser.element('/html/body/div[2]/div[3]/div[1]').click()
    browser.element('[placeholder="John"]').type('Elena')
    browser.element('[placeholder="Snow"]').type('Ivanova')
    browser.element('[placeholder="name@example.com"]').type('Ivanova@mail.com')
    browser.element('[placeholder="+1 (999) 999 99 99"]').type('9990008909')
    browser.all('.MuiFormControl-root').element_by(have.exact_text('Language')).click()
    browser.element('[data-value="Russian"]').click()
    browser.element('[aria-label="Choose date"]').click()
    browser.element('[data-timestamp="1699736400000"]').click()
    browser.element('[value="Female"]').click()
    browser.element('[value="Sports"]').click()
    browser.all('.MuiInputBase-root')['4'].element_by()

