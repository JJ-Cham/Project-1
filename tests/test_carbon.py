import unittest
from unittest.mock import patch, MagicMock

from api import carbon_api


class TestCarbonApi(unittest.TestCase):
    @patch("api.carbon_api.API_KEY", "fake-key")
    @patch("api.carbon_api.requests.post")
    def test_estimate_emissions_returns_co2e(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"co2e": 2.4}
        mock_post.return_value = mock_response

        result = carbon_api.estimate_emissions("some-activity", 10)

        self.assertEqual(result, 2.4)

    @patch("api.carbon_api.API_KEY", None)
    def test_estimate_without_key_returns_none(self):
        self.assertIsNone(carbon_api.estimate_emissions("some-activity", 10))

    @patch("api.carbon_api.API_KEY", "fake-key")
    @patch("api.carbon_api.requests.post")
    def test_carbon_saved_bike_equals_car_emissions(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"co2e": 2.4}
        mock_post.return_value = mock_response

        self.assertEqual(carbon_api.carbon_saved("bike", 10), 2.4)

    @patch("api.carbon_api.API_KEY", "fake-key")
    @patch("api.carbon_api.requests.post")
    def test_carbon_saved_bus_is_difference(self, mock_post):
        car_response = MagicMock()
        car_response.json.return_value = {"co2e": 2.4}
        bus_response = MagicMock()
        bus_response.json.return_value = {"co2e": 1.0}
        mock_post.side_effect = [car_response, bus_response]

        self.assertEqual(carbon_api.carbon_saved("bus", 10), 1.4)


if __name__ == "__main__":
    unittest.main()
