""" test_Pokemon.py: Holds the test for methods in Pokemon ."""
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

import unittest

from tester_base import TesterBase


class TestPokemon(TesterBase):

    # Charmander's method tests
    def test_charmander_attack(self):
        """Test Charmander's attack"""
        from pokemon import Charmander
        c = Charmander()
        try:
            self.assertEqual(c.get_attack(), 6 + c.get_level(), msg="Charmander attack test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_charmander_speed(self):
        """Test Charmander's speed"""
        from pokemon import Charmander
        c = Charmander()
        try:
            self.assertEqual(c.get_speed(), 7 + c.get_level(), msg="Charmander speed test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_charmander_defence(self):
        """Test Charmander's defence"""
        from pokemon import Charmander
        c = Charmander()
        try:
            self.assertEqual(c.get_defence(), 4, msg="Charmander defence test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_charmander_poke_name(self):
        """Test Charmander's poke name"""
        from pokemon import Charmander
        c = Charmander()
        try:
            self.assertEqual(c.get_poke_name(), "Charmander", msg="Charmander pokename test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_charmander_attack_damage(self):
        """Test Charmander's attack damage"""
        from pokemon import Charmander
        c = Charmander()
        c2 = Charmander()
        try:
            self.assertEqual(c.damage_taken(c2), 7, msg="Charmander attack damage test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_charmander_get_constant(self):
        """Test Charmander's get_constant"""
        from pokemon import Charmander
        c = Charmander()
        try:
            self.assertEqual(c.get_constant(), 3, msg="Charmander's get constant test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    # Bulbasaur's method tests
    def test_bulbasaur_attack(self):
        """Test Bulbasaur's attack"""
        from pokemon import Bulbasaur
        b = Bulbasaur()
        try:
            self.assertEqual(b.get_attack(), 5, msg="Bulbasaur's attack test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_bulbasaur_speed(self):
        """Test Bulbasaur's speed"""
        from pokemon import Bulbasaur
        b = Bulbasaur()
        try:
            self.assertEqual(b.get_speed(), 7 + (b.get_level() // 2), msg="Bulbasaur's speed test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_bulbasaur_defence(self):
        """Test Bulbasaur's defence"""
        from pokemon import Bulbasaur
        b = Bulbasaur()
        try:
            self.assertEqual(b.get_defence(), 5, msg="Bulbasaur's defence test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_bulbasaur_poke_name(self):
        """Test Bulbasaur's poke name"""
        from pokemon import Bulbasaur
        b = Bulbasaur()
        try:
            self.assertEqual(b.get_poke_name(), "Bulbasaur", msg="Bulbasaur's pokename test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_bulbasaur_attack_damage(self):
        """Test Bulbasaur's attack damage"""
        from pokemon import Bulbasaur
        b = Bulbasaur()
        b2 = Bulbasaur()
        try:
            self.assertEqual(b.damage_taken(b2), 2, msg="Bulbasaur's attack damage test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_bulbasaur_get_constant(self):
        """Test Bulbasaur's get_constant"""
        from pokemon import Bulbasaur
        b = Bulbasaur()
        try:
            self.assertEqual(b.get_constant(), 2, msg="Bulbasaur's get constant test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    # Squirtle's method tests
    def test_squirtle_attack(self):
        """Test Squirtle's attack"""
        from pokemon import Squirtle
        s = Squirtle()
        try:
            self.assertEqual(s.get_attack(), (4 + s.get_level() // 2), msg="Squirtle's attack test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_squirtle_speed(self):
        """Test Squirtle's speed"""
        from pokemon import Squirtle
        s = Squirtle()
        try:
            self.assertEqual(s.get_speed(), 7, msg="Squirtle's speed test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_squirtle_defence(self):
        """Test Squirtle's defence"""
        from pokemon import Squirtle
        s = Squirtle()
        try:
            self.assertEqual(s.get_defence(), 7, msg="Squirtle's defence test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_squirtle_poke_name(self):
        """Test Squirtle's poke name"""
        from pokemon import Squirtle
        s = Squirtle()
        try:
            self.assertEqual(s.get_poke_name(), "Squirtle", msg="Squirtle's pokename test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_squirtle_attack_damage(self):
        """Test Squirtle's attack damage"""
        from pokemon import Squirtle
        s = Squirtle()
        s2 = Squirtle()
        try:
            self.assertEqual(s.damage_taken(s2), 2, msg="Squirtle's attack damage test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_squirtle_get_constant(self):
        """Test Squirtle's get_constant"""
        from pokemon import Squirtle
        s = Squirtle()
        try:
            self.assertEqual(s.get_constant(), 1, msg="Squirtle's get constant test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
