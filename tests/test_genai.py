import textwrap
import unittest
from api.genai_api import sprout_feedback


class TestGenAI(unittest.TestCase):
    def test_feedback(self):
        # testing gen ai function with dummy data
        mock_weather = {
            "city": "New York",
            "description": "clear sky",
            "temp": 22.5,
        }
        result = sprout_feedback("bike", 2.5, "Sapling", mock_weather)

        # wrap text at 70 characters to print a clear response
        clean_paragraph = textwrap.fill(result, width=100)

        print("\n" + clean_paragraph + "\n")

        # supports string response
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()
