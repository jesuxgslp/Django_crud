from django.test import LiveServerTestCase
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
        selenium.get('http://127.0.0.1:8080/persona/create/')
        #find the form element
        first_name = selenium.find_element_by_id('id_nombre')
        last_name = selenium.find_element_by_id('id_apellido')
        dob = selenium.find_element_by_id('id_fecha_nacimiento')

        submit = selenium.find_element_by_name('Guardar')

        #Fill the form with data
        first_name.send_keys('Jesus')
        last_name.send_keys('Reyes')
        dob.send_keys('12/01/2019')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Lista de Personas' in selenium.page_source