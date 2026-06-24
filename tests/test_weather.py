import unittest
from unittest.mock import patch, MagicMock

from api import weather_api


FAKE_RESPONSE = {
    "name": "London",
    "weather": [{"main": "Clear", "description": "clear sky"}],
    "main": {"temp": 18, "feels_like": 17, "humidity": 55},
    "wind": {"speed": 3.5},
}


class TestWeatherApi(unittest.TestCase):
    @patch("api.weather_api.API_KEY", "fake-key")
    @patch("api.weather_api.requests.get")
    def test_get_weather_parses_fields(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = FAKE_RESPONSE
        mock_get.return_value = mock_response

        result = weather_api.get_weather("London")

        self.assertEqual(result["city"], "London")
        self.assertEqual(result["condition"], "Clear")
        self.assertEqual(result["temp"], 18)

    @patch("api.weather_api.API_KEY", None)
    def test_get_weather_without_key_returns_none(self):
        self.assertIsNone(weather_api.get_weather("London"))

    @patch("api.weather_api.API_KEY", "fake-key")
    @patch("api.weather_api.requests.get")
    def test_is_good_weather_true_for_clear(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = FAKE_RESPONSE
        mock_get.return_value = mock_response

        self.assertTrue(weather_api.is_good_weather("London"))


if __name__ == "__main__":
    unittest.main()
