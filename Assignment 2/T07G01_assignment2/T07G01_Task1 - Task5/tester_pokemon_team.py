""" tester_pokemon_team.py: The tester for task 2. """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

import unittest
from tester_base import TesterBase, captured_output


class TesterPokeTeam(TesterBase):
    """
    assign_team:
    Don't have tester in assign_team because it relates with choose_team
    When input in choose_team is valid, then will go through assign_team; Else will not
    Therefore, assign_team is already checked in task2_tester.py
    __str__ is also already checked in task2_tester.py
    """

    def test_input_valid(self):
        """
        Input the valid input, check whether will error or not
        total of 2 2 2 is equal to 6, should success
        """
        from poke_team import PokeTeam
        team = PokeTeam("Ash")
        try:
            with captured_output("2 2 2") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(e)
            return

    def test_input_invalid(self):
        """
        Input the invalid input, check whether it will print error or not
        total of 2 2 4 is greater than 6, should fail(have error because greater than 6)
        """
        import poke_team
        with self.assertRaises(ValueError) as e:
            poke_team.check_input(2, 2, 4)
        self.assertEqual(str(e.exception), "The team cannot have more than 6 Pokemon")
        return

    def test_input_isNegative(self):
        """
        Input the invalid input, check whether it will print error or not
        it has negative number, should fail(have error because negative number)
        """
        import poke_team
        with self.assertRaises(ValueError) as e:
            poke_team.check_input(-1, 2, 3)
        self.assertEqual(str(e.exception), "The number of Pokemon cannot be negative")
        return

    def test_input_isEmpty(self):
        """
        Input the invalid input, check whether it will print error or not
        it is empty, should fail(have error because team is empty)
        """
        import poke_team
        with self.assertRaises(ValueError) as e:
            poke_team.check_input(0, 0, 0)
        self.assertEqual(str(e.exception), "The team cannot have 0 Pokemon")
        return

    def test_criterion_valid(self):
        """
        Input the valid input, check whether it will print error or not
        HP is a valid input for criterion
        """
        from poke_team import PokeTeam
        team = PokeTeam("Ash")
        try:
            with captured_output("2 2 2") as (inp, out, err):
                team.choose_team(0, "HP")
        except Exception as e:
            self.verificationErrors.append(e)
            return

    def test_criterion_invalid(self):
        """
        Input the invalid input, check whether it will print error or not
        Name is an invalid input for criterion
        """
        import poke_team
        with self.assertRaises(ValueError) as e:
            poke_team.check_criterion("Name")
        self.assertEqual(str(e.exception), "Criterion can only be Level, HP, Attack, "
                                           "Defense, Speed or None ; else valid")
        return

    def test_str(self):
        """
        Check after input is valid, whether print(team) is correct or not
        """
        from poke_team import PokeTeam
        team = PokeTeam("Ash")
        with captured_output("2 2 1") as (inp, out, err):
            team.choose_team(0, None)
        try:
            assert str(
                team) == "Charmander's HP = 7 and level = 1, Charmander's" \
                         " HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_valid(self):
        """
        Check battle mode is correct or not when it is 2
        battle mode can be 2, should success
        """
        from poke_team import PokeTeam
        team = PokeTeam("Ash")

        try:
            with captured_output("1 1 1") as (inp, out, err):
                team.choose_team(2, None)
        except Exception as e:
            self.verificationErrors.append(e)

    def test_battle_mode_invalid(self):
        """
        Check battle mode is correct or not when it is 3
        battle mode can not be 3, should fail(have error because battle mode is 3)
        """
        import poke_team
        with self.assertRaises(ValueError) as e:
            poke_team.check_battle_mode(3)
        self.assertEqual(str(e.exception), "battle_mode only can be 0, 1, 2, else valid")
        return


if __name__ == '__main__':
    unittest.main()

