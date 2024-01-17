import unittest
from unittest.mock import patch
from io import StringIO
from cool_con_final import CoolDatabaseManager

class TestCoolDatabaseManager(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "10", "5.5", "Pizza"])
    def test_data_entry(self, mock_input):
        with CoolDatabaseManager() as db_manager:
            db_manager.data_entry()

            # Add assertions based on your expected outcomes
            # For example, you can check if the data was inserted into the database correctly

    @patch("builtins.input", side_effect=["Pharmacy A", "15.99"])
    def test_pen_insert(self, mock_input):
        with CoolDatabaseManager() as db_manager:
            db_manager.pen_insert()

            # Add assertions based on your expected outcomes
            # For example, you can check if the pen information was inserted into the database correctly

    def test_create_table(self):
        with CoolDatabaseManager() as db_manager:
            db_manager.create_table()

            # Add assertions based on your expected outcomes
            # For example, you can check if the "inject" table was created in the database

    @patch("builtins.input", side_effect=["5"])
    def test_select_table(self, mock_input):
        with CoolDatabaseManager(':memory:') as db_manager:
            # Redirect stdout to capture the print output
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                db_manager.select_table()

                # Add assertions based on your expected outcomes
                # For example, you can check if the expected rows are printed

if __name__ == "__main__":
    unittest.main()
