import unittest
import scraper
from unittest.mock import patch

# ----------------------------------------
class TestScraper(unittest.TestCase):

    # def test_exists(filename):
    #     '''Check if the file exists'''
    #     assert os.path.isfile('./clivia.txt')

    def test_numb_pages(self):
        '''Count number of pages'''
        self.assertEqual(scraper.tot_pages, 2)

if __name__ == '__main__':
   unittest.main()