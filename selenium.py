from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/persona/create/')
        #find the form element
        nombre = selenium.find_element_by_id('nombre')
        apellido = selenium.find_element_by_id('apellido')
        nacimiento = selenium.find_element_by_id('nacimiento')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        nombre.send_keys('Yusuf')
        apellido.send_keys('Unary')
        nacimiento.send_keys('unary')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in selenium.page_source