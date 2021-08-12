import unittest
import scraper

# ----------------------------------------
class TestScraper(unittest.TestCase):

    def test_url_access(self):
        '''Check if the webpage is accessible'''
        self.assertEqual(scraper.browser.status_code, 200)

    def test_current_txt(self):
        '''Check if file is accessible/has been created'''
        self.assertIsNotNone(scraper.old_clivia)
        # self.assertIsNone(scraper.old_clivia)

    def test_num_pages(self):
        '''Count number of pages'''
        self.assertEqual(scraper.tot_pages, 2)
        self.assertEqual(scraper.tot_pages, 10)
    
    def test_latest_plants(self):
        '''Check difference between between lists'''
        self.assertEqual(scraper.new_clivia, [])

    def test_notification(self):
        '''Does the notification send'''
        if scraper.new_clivia != []:
            self.assertEqual(scraper.notification.message, "New clivias are on sale.")

if __name__ == '__main__':
   unittest.main()