import textwrap
import unittest
from api.genai_api import sprout_feedback


class TestGenAI(unittest.TestCase):
    def test_feedback(self):
        # testing gen ai function with dummy data
        result = sprout_feedback("Biked", 1.0, "Seedling", "Sunny")

        # wrap text at 70 characters to print a clear response
        clean_paragraph = textwrap.fill(result, width=70)

        print("\n" + clean_paragraph + "\n")

        # supports string response
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()
