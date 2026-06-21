from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # He types "Fold away laundry"
        inputbox.send_keys("Fold away laundry")

        # When he hits Enter, the page updates and now lists:
        # "1: Fold away laundry" as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep()

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Fold away laundry" for row in rows))

        # A tet box remains to input more items
        # He types "Hang painting"
        self.fail("Finish the test!")

        # The page updates again and both items are on the list

        # Satisfied, he goes back to sleep

if __name__ == "__main__":
    unittest.main()