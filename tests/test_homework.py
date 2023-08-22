from selene import browser, have
import os


def test_submit_form(browser_size):
    browser.open('https://demoqa.com/automation-practice-form')

    # Заполнение основных данных пользователя
    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('ivan@mail.ru')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('9270118888')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1995"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="1"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__day--002').click()

    # Заполнение адреса пользователя
    browser.element('#currentAddress').type('Gagarina 100')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    # Заполнение данных о хобби и предметах
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

    # Загрузка файла
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/fine.png'))

    # Отправка формы
    browser.element('#submit').click()

    # Проверка всей формы
    browser.element('.table').all('td').even.should(
        have.texts('Иван Иванов', 'ivan@mail.ru', 'Female', '9270118888', '02 February,1995', 'Maths', 'Sports',
                   'fine.png', 'Gagarina 100', 'NCR Delhi'))

    # Не будет ли более понятным такой вариант, для того что-бы сразу понимать, какое значение не совпало с ожидаемым?
    '''
    browser.element('.table').should(have.text('Иван'))
    browser.element('.table').should(have.text('Иванов'))
    browser.element('.table').should(have.text('ivan@mail.ru'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('9270118888'))
    browser.element('.table').should(have.text('02 February,1995'))
    browser.element('.table').should(have.text('Maths'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('fine.png'))
    browser.element('.table').should(have.text('Gagarina 100'))
    browser.element('.table').should(have.text('NCR'))
    browser.element('.table').should(have.text('Delhi'))
    '''
