""" test_Pokemon.py: Holds the test for methods in Pokemon."""
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

import unittest

from tester_base import TesterBase


class TestPokemon(TesterBase):

    # MissingNo method tests
    def test_MissingNo_attack(self):
        """Test MissingNo's attack"""
        from pokemon import MissingNo
        m = MissingNo()
        try:
            self.assertEqual(m.get_attack(), 16/3 + m.get_level() - 1, msg="MissingNo's attack test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_MissingNo_speed(self):
        """Test MissingNo's speed"""
        from pokemon import MissingNo
        m = MissingNo()
        try:
            self.assertEqual(m.get_speed(), 22/3 + m.get_level() - 1, msg="MissingNo's speed test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_MissingNo_defence(self):
        """Test MissingNo's defence"""
        from pokemon import MissingNo
        m = MissingNo()
        try:
            self.assertEqual(m.get_defence(), 16/3 + m.get_level() - 1, msg="MissingNo's defence test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_MissingNo_poke_name(self):
        """Test MissingNo's poke name"""
        from pokemon import MissingNo
        m = MissingNo()
        try:
            self.assertEqual(m.get_poke_name(), "MissingNo", msg="MissingNo's pokename test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_MissingNo_attack_damage(self):
        """Test MissingNo's attack damage"""
        from pokemon import MissingNo
        m = MissingNo()
        m2 = MissingNo()
        try:
            self.assertEqual(m.damage_taken(m2), 2, msg="MissingNo's attack damage test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_MissingNo_get_constant(self):
        """Test MissingNo's get_constant"""
        from pokemon import MissingNo
        m = MissingNo()
        try:
            self.assertEqual(m.get_constant(), 0, msg="MissingNo's get constant test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    # GlitchMon methods test
    def test_GlitchMon_increase_hp(self):
        """Test MissingNo in GlitchMon's increase_hp"""
        from pokemon import MissingNo
        m = MissingNo()
        m.increase_hp(1)
        try:
            self.assertEqual(m.get_hp(), 9, msg="MissingNo's increase hp test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_GlitchMon_superpower(self):
        """Test MissingNo in GlitchMon's superpower"""
        from pokemon import MissingNo
        m = MissingNo()
        m.superpower()

        if not ((m.get_hp() == 9 and m.get_level() == 2) or (m.get_hp() == 9) or
                (m.get_level() == 2)):
            self.verificationErrors.append("MissingNo superpower is invalid")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
