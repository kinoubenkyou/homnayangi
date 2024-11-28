from selenium.webdriver.common.by import By

from main.models import User
from main.tests.test_cases.test_case import TestCase


class UserCreateTestCase(TestCase):
    def test(self):
        self.web_driver.get(f"{self.live_server_url}/user/create/")
        username = "username1"
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            username,
        )
        password = "Dr0wss@p1"  # noqa: S105
        self.web_driver.find_element(By.XPATH, '//input[@name="password1"]').send_keys(
            password,
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password2"]').send_keys(
            password,
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/?next=/user/",
        )
        self.assertEqual(
            len([
                user
                for user in User.objects.filter(username=username)
                if user.check_password(password)
            ]),
            1,
        )
