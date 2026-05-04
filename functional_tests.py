from selenium import webdriver
import unittest
# Functional Test == End-to-End Test == Acceptance Test

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_todo_list(self):
        # Anthony wants to access a new To-Do App
        # He visits the homepage:
        self.browser.get("http://localhost:8000")

        # He notes the title and header mentions To-Do lists
        self.assertIn("To-Do", self.browser.title)

        # He is invited to enter a to-do item straight away
        self.fail("Remember to finish the test!")

        # He types "Fold away laundry"

        # When he hits Enter, the page updates and now lists:
        # "1: Fold away laundry" as an item in the to-do list

        # A tet box remains to input more items
        # He types "Hang painting"

        # The page updates again and both items are on the list

        # Satisfied, he goes back to sleep

if __name__ == "__main__":
    unittest.main()