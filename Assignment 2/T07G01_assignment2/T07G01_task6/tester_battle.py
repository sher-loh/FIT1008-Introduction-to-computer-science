"""tester_battle.py: Holds test for methods in Task 6. """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

import unittest
from tester_base import TesterBase, captured_output


class TesterBattle(TesterBase):
    """
    Testing the battle.py for Task 6
    """

    def test_get_superpower(self):
        """
        Check if MissingNo 25% of getting superpower works or not
        """
        from battle import Battle
        from pokemon import MissingNo
        team1_pokemon = MissingNo()
        Battle.get_superpower(self, team1_pokemon)
        if not ((team1_pokemon.get_hp() == 9 and team1_pokemon.get_level() == 2) or (team1_pokemon.get_hp() == 9) or
                (team1_pokemon.get_level() == 2)):
            self.verificationErrors.append("MissingNo superpower is invalid")

    def test_battle_mode_is_zero(self):
        """
        Check the battle mode whether it is 0
        Battle mode is 0, should success
        """
        from battle import Battle
        b2 = Battle("Ash", "Misty")
        try:
            with captured_output("1 2 0 0\n1 0 0 1") as (inp, out, err):
                b2.set_mode_battle()
            self.assertEqual(b2.battle_mode, 0)
        except AssertionError:
            self.verificationErrors.append("battle mode is not 0")

    def test_battle_mode_is_one(self):
        """
        Check the battle mode whether it is 1
        Battle mode is 1, should success
        """
        from battle import Battle
        b2 = Battle("Ash", "Misty")
        try:
            with captured_output("1 2 0 1\n1 0 0 1") as (inp, out, err):
                b2.rotating_mode_battle()
            self.assertEqual(b2.battle_mode, 1)
        except AssertionError:
            self.verificationErrors.append("battle mode is not 1")

    def test_battle_mode_is_two(self):
        """
        Check the battle mode whether it is 2
        Battle mode is 2, should success
        """
        from battle import Battle
        b2 = Battle("Cynthia", "Steven")
        try:
            with captured_output("1 2 0 1\n1 0 0 1") as (inp, out, err):
                b2.optimised_mode_battle("HP", "Level")
            self.assertEqual(b2.battle_mode, 2)
        except AssertionError:
            self.verificationErrors.append("battle mode is not 2")

    # For Set mode battle
    def test_set_mode_battle(self):
        """
        Using set_mode_battle(), check if the winner is correct or not
        """
        from battle import Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 1 1 1\n1 1 1 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Misty"
        except AssertionError:
            self.verificationErrors.append(f"Misty should win: {result}.")

    # For rotating_mode_battle
    def test_rotating_battle(self):
        """
        Using rotating_mode_battle(), check if the winner is correct or
        not and check if the team is correct after the battle by printing string
        """
        from battle import Battle
        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 2 1 1\n2 2 1 0") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Gary"
        except AssertionError:
            self.verificationErrors.append(f"Gary should win: {result}.")
        try:
            assert str(b.team2) == "Charmander's HP = 7 and level = 2, Bulbasaur's HP = 7 and level = 1," \
                                   " Bulbasaur's HP = 6 and level = 1, Squirtle's HP = 6 and level = 2," \
                                   " Charmander's HP = 7 and level = 3"

        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    # For Optimised mode battle
    def test_optimised_mode_battle(self):
        """
        Using optimised_mode_battle(), check if the winner is correct or
        not and check if the team is correct after the battle by printing string
        """
        from battle import Battle
        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 1 1\n2 2 0 0") as (inp, out, err):
                result = b.optimised_mode_battle("HP", "Level")

        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Cynthia"
        except AssertionError:
            self.verificationErrors.append(f"Cynthia should win: {result}.")
        try:
            assert str(
                b.team1) == "MissingNo's HP = 10 and level = 6"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")


if __name__ == '__main__':
    unittest.main()
