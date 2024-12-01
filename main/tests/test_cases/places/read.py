from main.tests.test_cases.sign_in_mixin import SignInMixin
from main.tests.test_cases.test_case import TestCase


class PlacesReadTestCase(SignInMixin, TestCase):
    fixtures = [*SignInMixin.fixtures, "places_read"]

    def test(self):
        self.web_driver.get(f"{self.live_server_url}/places/1/")
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/?next=/places/1/",
        )
        self.sign_in()
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/places/1/",
        )
        self.assertEqual(len(self.find_elements_with_text("Address: address1")), 1)
        self.assertEqual(len(self.find_elements_with_text("Name: name1")), 1)
        self.assertEqual(len(self.find_elements_with_text("Price group: unknown")), 1)
