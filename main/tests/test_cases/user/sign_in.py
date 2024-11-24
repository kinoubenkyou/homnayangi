from main.tests.test_cases.sign_in_mixin import SignInMixin
from main.tests.test_cases.test_case import TestCase


class UserSignInTestCase(SignInMixin, TestCase):
    def test(self):
        self.web_driver.get(f"{self.live_server_url}/user/sign_in/")
        self.sign_in()

        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/signed_in/",
        )
