import unittest

class PierwszyTest (unittest.Testase):
    def setUp(self):
        print("Przygotowanie do testu")
    def test_224(self):
        # 'Prawdziwy test'
        print("Sprawdzam, czy 2+2=4")
        assert(2+2==4)
