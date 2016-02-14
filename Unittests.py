__author__ = 'Florian Kibler'

import unittest


class TestsKorrekteAusfuehrung(unittest.TestCase):

    def test_korrekteAusfuehrungeinFile(self):
        pass;

    def test_MehrereFiles_gleicherDialekt(self):
        pass;

    def test_MehrereFiles_unterschiedlicherDialekt(self):
        pass;

class Filenichtkorrekt(unittest.TestCase):
    """
    def test_something(self):
        self.assertEqual(True, False)
    """

    def test_Dateinichtvorhanden(self):
        pass;

    def test_UngueltigerDateiinhalt(self):
        pass;

    def test_KeinDateiinhalt(self):
        pass;



if __name__ == '__main__':
    unittest.main()
