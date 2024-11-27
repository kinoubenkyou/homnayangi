from main.tests.test_cases.sign_in_mixin import SignInMixin
from main.tests.test_cases.test_case import TestCase


class UserReadTestCase(SignInMixin, TestCase):
    fixtures = ["user_read"]

    def test(self):
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/?next=/user/",
        )
        self.sign_in()
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        self.assertEqual(len(self.find_elements_with_text("Username: username1")), 1)
        self.assertEqual(
            len(self.find_elements_with_text("First name: first_name1")),
            1,
        )
        self.assertEqual(len(self.find_elements_with_text("Last name: last_name1")), 1)
        self.assertEqual(
            len(self.find_elements_with_text("Email: email1@email.com")),
            1,
        )
        self.assertEqual(len(self.find_elements_with_text("Is staff: True")), 1)
        self.assertEqual(len(self.find_elements_with_text("Is active: True")), 1)
        self.assertEqual(
            len(self.find_elements_with_text("Date joined: Jan. 1, 2000, midnight")),
            1,
        )
