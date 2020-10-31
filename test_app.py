from unittest import TestCase
from app import app

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ConversionTestCase(TestCase):
    """Integration testing of the conversion web app"""

    def test_initial_page_load(self):
        """
        Tests the initial page load of the main form page
        """
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text = True)
            self.assertEqual(resp.status_code,200)
            self.assertIn('Currency Conversion Input',html)

    def test_good_query(self):
        """
        Tests a successful currency conversion
        """
        with app.test_client() as client:
            resp = client.get('/results?from=USD&to=USD&amount=5')
            html = resp.get_data(as_text = True)
            self.assertEqual(resp.status_code,200)
            self.assertIn('5.0 US$',html)
    def test_bad_query_redirect(self):
        """
        Tests an unsuccessful currency conversion
        """
        with app.test_client() as client:
            resp = client.get('/results?from=XXX&to=USD&amount=5')
            self.assertEqual(resp.status_code,302)
            self.assertEqual(resp.location,'http://localhost/')
            resp = client.get('/results?from=XXX&to=USD&amount=5',follow_redirects = True)
            html = resp.get_data(as_text = True)
            self.assertEqual(resp.status_code,200)
            self.assertIn('XXX is not a valid currency code',html)