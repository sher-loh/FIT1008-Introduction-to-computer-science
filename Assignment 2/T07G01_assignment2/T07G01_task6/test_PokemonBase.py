""" test_PokemonBase.py: Holds the tests for methods in pokemon_base. """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from tester_base import TesterBase
from pokemon_base import PokemonBase
import unittest


class DummyAbstract(PokemonBase):
    """
    This class and its components bypasses the abstract methods
    in order to instantiate objects for non-abstract methods
    """

    def get_poke_name(self) -> str:
        raise NotImplementedError

    def get_speed(self) -> int:
        raise NotImplementedError

    def get_attack(self) -> int:
        raise NotImplementedError

    def get_defence(self) -> int:
        raise NotImplementedError

    def damage_taken(self, opponent) -> int:
        raise NotImplementedError

    def get_constant(self) -> int:
        raise NotImplementedError


class TestPokemonBase(TesterBase):

    def test_get_hp(self):
        """Test get hp"""
        t1 = DummyAbstract(0, None)
        t2 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.get_hp(), t2.get_hp(), msg="get hp test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_set_hp(self):
        """Test set hp"""
        t1 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.set_hp(8), None, msg="set hp test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_get_level(self):
        """Test get level"""
        t1 = DummyAbstract(0, None)
        t2 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.get_level(), t2.get_level(), msg="get level test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_set_level(self):
        """Test set level"""
        t1 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.set_level(1), None, msg="set level test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_set_poke_type(self):
        """Test set poke type"""
        t1 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.set_poke_type(None), None, msg="set poke type test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_get_poke_type(self):
        """Test get poke type"""
        t1 = DummyAbstract(0, None)
        t2 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.get_poke_type(), t2.get_poke_type(), msg="get hp test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_is_fainted(self):
        """Test is fainted"""
        t1 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.is_fainted(), True, msg="is fainted  test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_level_up(self):
        """Test level up"""
        t1 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.level_up(), None, msg="level up test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_lose_hp(self):
        """Test lose hp"""
        t1 = DummyAbstract(0, None)

        try:
            self.assertEqual(t1.lose_hp(0), None, msg="lose hp test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_get_criteria(self):
        """Test get criteria"""
        t1 = DummyAbstract(1, None)

        try:
            self.assertEqual(t1.get_criteria("HP"), 10, msg="get criteria test failed")
        except AssertionError as e:
            self.verificationErrors.append(e)

    def test_MissingNo_str(self):
        """Test string of MissingNo"""
        t1 = DummyAbstract(0, None)
        try:
            s = str(t1)
            if s != "MissingNo's HP = 0 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
