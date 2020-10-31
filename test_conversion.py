import conversion
from unittest import TestCase

class ConversionTestCase(TestCase):
    """Currency Converter unit tests."""

    def test_converter(self):
        self.assertIsInstance(conversion.convert('USD','USD',5),str)
        self.assertEqual(conversion.convert('USD','USD',5),'5.0 US$')
        self.assertIsInstance(conversion.convert('XXX','USD',5),list)
        self.assertIsInstance(conversion.convert('USD','XXX',5),list)
        self.assertIsInstance(conversion.convert('USD','USD','dog'),list)
        self.assertListEqual(conversion.convert('XXX','ZZZ','dog'),['XXX is not a valid currency code','ZZZ is not a valid currency code','dog is not a valid currency amount'])