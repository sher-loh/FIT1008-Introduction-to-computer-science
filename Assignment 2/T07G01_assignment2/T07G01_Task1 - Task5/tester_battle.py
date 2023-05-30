"""tester_battle.py: Holds test for methods in Task 3, 4 and 5. """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

import unittest
from tester_base import TesterBase, captured_output


class TesterBattle(TesterBase):
    """
    return_result:
    Don't need tester in return_result because it is checked in task3_tester.py,
    there are 3 condition(Team1 win, Team2 win and draw),
    if return_result return the correct string, then will pass the tester in task3_tester.py
    """

    def test_pokemon_attack(self):
        """
        Check the attack is correct or not
        team1_pokemon's hp is 7, and team2_pokemon's hp is 9;
        The damage from team1_pokemon to team2_pokemon is 14,
        after Battle.pokemon_attack,
        team1_pokemon's hp is 7, and team2_pokemon's hp is 0
        """
        from battle import Battle
        from pokemon import Charmander, Bulbasaur
        team1_pokemon = Charmander()  # hp = 7
        team2_pokemon = Bulbasaur()  # hp = 9
        Battle.pokemon_attack(self, team1_pokemon, team2_pokemon)
        # team2_pokemon.damage_taken(team1_pokemon) is 14
        # so team1_pokemon haven't lost hp, but team2_pokemon is fainted
        try:
            assert team1_pokemon.get_hp() == 7 and team2_pokemon.get_hp() == 0
        except AssertionError:
            self.verificationErrors.append("team1_pokemon should be 7, team2_pokemon should be 0")

    def test_both_pokemon_not_fainted(self):
        """
        Check if hp is > 0, if hp lost hp or not
        team1_pokemon's hp is 7, and team2_pokemon's hp is 9;
        after check_both_pokemon_not_fainted,
        team1_pokemon's hp is 6, and team2_pokemon's hp is 8
        """
        from battle import Battle
        from pokemon import Charmander, Bulbasaur
        team1_pokemon = Charmander()  # hp = 7
        team2_pokemon = Bulbasaur()  # hp = 9
        Battle.check_both_pokemon_not_fainted(self, team1_pokemon, team2_pokemon)
        try:
            assert team1_pokemon.get_hp() == 6 and team2_pokemon.get_hp() == 8
        except AssertionError:
            self.verificationErrors.append("team1_pokemon should be 6, team2_pokemon should be 8")

    def test_battle_mode_is_zero(self):
        """
        Check the battle mode for task 3 whether is 0
        Battle mode is 0, should success
        """
        from battle import Battle
        b2 = Battle("Ash", "Misty")
        try:
            with captured_output("1 2 0\n1 0 0") as (inp, out, err):
                b2.set_mode_battle()
            self.assertEqual(b2.battle_mode, 0)
        except AssertionError:
            self.verificationErrors.append("battle mode is not 0")

    def test_battle_mode_is_one(self):
        """
        Check the battle mode for task 4 whether is 1
        Battle mode is 1, should success
        """
        from battle import Battle
        b2 = Battle("Ash", "Misty")
        try:
            with captured_output("1 2 0\n1 0 0") as (inp, out, err):
                b2.rotating_mode_battle()
            self.assertEqual(b2.battle_mode, 1)
        except AssertionError:
            self.verificationErrors.append("battle mode is not 1")

    def test_battle_mode_is_two(self):
        """
        Check the battle mode for task 5 whether it is 2
        Battle mode is 2, should success
        """
        from battle import Battle
        b2 = Battle("Cynthia", "Steven")
        try:
            with captured_output("1 2 0\n1 0 0") as (inp, out, err):
                b2.optimised_mode_battle("HP", "Level")
            self.assertEqual(b2.battle_mode, 2)
        except AssertionError:
            self.verificationErrors.append("battle mode is not 2")

    # For set_mode_battle
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
            with captured_output("2 1 1\n1 1 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")

    def test_set_mode_battle_draw(self):
        """
        Using set_mode_battle(), check if battle will result in Draw or not
        """
        from battle import Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"Battle should be Draw: {result}.")

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
            with captured_output("0 2 1\n2 2 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Gary"
        except AssertionError:
            self.verificationErrors.append(f"Gary should win: {result}.")
        try:
            assert str(
                b.team2) == "Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 2, Charmander's HP = 7 and level = 2, Bulbasaur's HP = 7 and level = 1, Bulbasaur's HP = 8 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    def test_rotating_battle_draw(self):
        """
        Using rotating_mode_battle(),
        Check if battle will result in Draw or not
        When battle is a draw, both team should be empty.
        """
        from battle import Battle
        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"Battle should be Draw: {result}.")
        try:
            assert str(b.team1) == ""
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")
        try:
            assert str(b.team2) == ""
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    #  For optimised mode battle
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
            with captured_output("2 2 0\n2 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("HP", "Level")

        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Steven"
        except AssertionError:
            self.verificationErrors.append(f"Steven should win: {result}.")
        try:
            assert str(
                b.team2) == "Charmander's HP = 7 and level = 5, Charmander's HP = 7 and " \
                            "level = 1, Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    def test_optimised_mode_battle_draw(self):
        """
        Using optimised_mode_battle(),
        Check if battle will result in Draw or not
        When battle is a draw, both team should be empty.
        """
        from battle import Battle
        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 0 1\n2 0 1") as (inp, out, err):
                result = b.optimised_mode_battle("HP", "Level")

        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"Battle should be Draw: {result}.")
        try:
            assert str(b.team1) == ""
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")
        try:
            assert str(b.team2) == ""
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    def test_optimised_mode_battle_diff_criterion(self):
        """
        Check if the winner is correct or not using different criterion input
        """
        from battle import Battle
        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 0\n2 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("Level", "Speed")

        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Steven"
        except AssertionError:
            self.verificationErrors.append(f"Steven should have won: {result}.")
        try:
            assert str(
                b.team2) == "Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")


if __name__ == '__main__':
    unittest.main()
