import unittest

from primes import largest_prime

class TestPrimes(unittest.TestCase):
    
    def test_some_values(self):
        inputs = [3, 20, 47]
        outputs = [2, 19, 43]
        for i, o in zip(inputs, outputs):
            self.assertEqual(largest_prime(i), o)


    def test_prime(self):
        input = [5, 29, 99]
        output = [3, 23, 93]

        for i in range(0,2):
            self.assertEqual(largest_prime(input[i]),output[i],msg="prime test failed")




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimes)
    unittest.TextTestRunner(verbosity=0).run(suite)
