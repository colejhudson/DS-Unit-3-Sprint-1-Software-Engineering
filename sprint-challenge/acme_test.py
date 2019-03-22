from unittest import mock
import acme_report
import unittest
import acme

class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        product = acme.Product('foo')
        self.assertEqual(product.price, 10)

    def test_default_product_weight(self):
        product = acme.Product('bar')
        self.assertEqual(product.weight, 20)

    def test_if_stealability_or_explode_crashes(self):
        product = acme.Product('baz', 52, 3, 0.9)
        self.assertEqual(product.stealability(), "Very stealable!")
        self.assertEqual(product.explode(), "...fizzle.")

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = acme_report.generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = acme_report.generate_products()
        names = [product.name for product in products]
        split = [name.split(' ') for name in names]
        valid = [
            (pair[0] in acme_report.ADJECTIVES and pair[1] in acme_report.NOUNS)
            for pair in split
        ]

        self.assertEqual(all(valid), True)

if __name__ == '__main__':
    unittest.main()
