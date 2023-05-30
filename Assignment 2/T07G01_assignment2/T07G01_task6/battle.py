"""battle.py: allows users to assemble a team of Pokemon and battle with another Trainer"""
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from poke_team import PokeTeam
from pokemon_base import PokemonBase
from sorted_list import ListItem



class Battle:
    """
    Battle class allows users to assemble a team of Pokemon and battle with another Trainer
    pokemon_attack: takes pokemon from both team and allows pokemon to attack and defend each other
    depending on the Pokemon speed and MissingNo's superpower (if there is).
    check_both_pokemon_not_fainted: Check if both pokemon is not fainted, if True, reduce both pokemon HP by 1
    return_result: Return the string result of the battle.
    set_mode_battle: Allows 2 teams of Pokemon to battle using battle_mode 0
    rotating_mode_battle: Allows 2 teams of Pokemon to battle using battle_mode 1
    optimised_mode_battle : Allows 2 teams of Pokemon to battle using battle_mode 2
    """

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """
        Initialize Battle variables.
        :param self:
        :param trainer_one_name:
        :param trainer_two_name:
        :return: Returns None
        """
        self.criterion_team1 = None
        self.criterion_team2 = None
        self.trainer_one = trainer_one_name
        self.trainer_two = trainer_two_name
        self.battle_mode = None
        self.team1 = None
        self.team2 = None

    def get_superpower(self, pokemon) -> None:
        """
        Method to get the superpower for MissingNo
        :param self:
        :param pokemon:
        :return: Returns None
        complexity: O(1)
        """
        # random.seed is used to get a constant random value
        import random
        if pokemon.get_poke_type() is None:
            random.seed(2)
            random_number = random.randint(1, 4)
            # When random_number is 1, it is equivalent to 25 % - call superpower
            if random_number == 1:
                pokemon.superpower()

    def pokemon_attack(self, team1_pokemon: PokemonBase, team2_pokemon: PokemonBase) -> None:
        """
        Takes pokemon from both team and allows pokemon to attack and defend each other
        depending on the Pokemon speed and if MissingNo have superpower.
        :param self:
        :param team1_pokemon:
        :param team2_pokemon:
        :return: return None
        complexity: O(1)
        """
        if team1_pokemon.get_speed() > team2_pokemon.get_speed():
            team2_pokemon.lose_hp(team2_pokemon.damage_taken(team1_pokemon))
            self.get_superpower(team2_pokemon)
            if not team2_pokemon.is_fainted():
                team1_pokemon.lose_hp(team1_pokemon.damage_taken(team2_pokemon))
                self.get_superpower(team1_pokemon)
        elif team2_pokemon.get_speed() > team1_pokemon.get_speed():
            team1_pokemon.lose_hp(team1_pokemon.damage_taken(team2_pokemon))
            self.get_superpower(team1_pokemon)
            if not team1_pokemon.is_fainted():
                team2_pokemon.lose_hp(team2_pokemon.damage_taken(team1_pokemon))
                self.get_superpower(team2_pokemon)
        else:  # both pokemon has same speed
            team2_pokemon.lose_hp(team2_pokemon.damage_taken(team1_pokemon))
            self.get_superpower(team2_pokemon)
            team1_pokemon.lose_hp(team1_pokemon.damage_taken(team2_pokemon))
            self.get_superpower(team1_pokemon)

    def check_both_pokemon_not_fainted(self, team1_pokemon: PokemonBase, team2_pokemon: PokemonBase) -> None:
        """
        Check if both pokemon is not fainted, if True, reduce both pokemon HP by 1
        :param self:
        :param team1_pokemon:
        :param team2_pokemon:
        :return: Returns None
        complexity : O(1)
        """
        if (not team1_pokemon.is_fainted()) and (not team2_pokemon.is_fainted()):
            team1_pokemon.lose_hp(1)
            team2_pokemon.lose_hp(1)

    def return_result(self) -> str:
        """
        Return the string result of the battle.
        :param self:
        :return: Draw or the winner trainer_name as str.
        complexity : O(1)
        """
        if self.team1.team.is_empty() and self.team2.team.is_empty():
            return "Draw"
        elif self.team1.team.is_empty():
            return self.team2.trainer_name
        elif self.team2.team.is_empty():
            return self.team1.trainer_name

    def set_mode_battle(self) -> str:
        """
         Allows 2 teams of Pokemon to battle using battle_mode 0
        :param self:
        :return: Returns string result of the battle
        complexity : O(n) n is the number of times the two teams battle when either teams are empty
        """
        self.battle_mode = 0
        self.team1 = PokeTeam(self.trainer_one)
        self.team1.choose_team(self.battle_mode)
        self.team2 = PokeTeam(self.trainer_two)
        self.team2.choose_team(self.battle_mode)

        # Can use is empty function
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():

            # Call pokemon to battle
            team1_pokemon = self.team1.team.peek()
            team2_pokemon = self.team2.team.peek()

            # Check pokemon speed to decide which pokemon attack first
            self.pokemon_attack(team1_pokemon, team2_pokemon)

            # If both pokemon are still alive --> each of them lose 1 hp
            self.check_both_pokemon_not_fainted(team1_pokemon, team2_pokemon)

            # check if team 1 pokemon fainted (and team 2 pokemon alive)
            if team1_pokemon.is_fainted() and (not team2_pokemon.is_fainted()):
                team2_pokemon.level_up()
                self.team1.team.pop()
            # check if team 2 pokemon fainted (and team 1 pokemon alive)
            elif team2_pokemon.is_fainted() and (not team1_pokemon.is_fainted()):
                team1_pokemon.level_up()
                self.team2.team.pop()
            # if both pokemon fainted
            elif team1_pokemon.is_fainted() and team2_pokemon.is_fainted():
                self.team1.team.pop()
                self.team2.team.pop()

        # Return result / winner / draw
        return self.return_result()

    def rotating_mode_battle(self) -> str:
        """
        Allows 2 teams of Pokemon to battle using battle_mode 1.
        :param self:
        :return: string result of the battle
        complexity: O(n) n is the number of times the two teams battle when either teams are empty
        """
        self.battle_mode = 1
        self.team1 = PokeTeam(self.trainer_one)
        self.team1.choose_team(self.battle_mode)
        self.team2 = PokeTeam(self.trainer_two)
        self.team2.choose_team(self.battle_mode)

        while not self.team1.team.is_empty() and not self.team2.team.is_empty():

            # Call out pokemon
            team1_pokemon = self.team1.team.serve()
            team2_pokemon = self.team2.team.serve()

            # Pokemon attack each other
            # Check pokemon speed to decide which pokemon attack first
            self.pokemon_attack(team1_pokemon, team2_pokemon)

            # Both pokemon are still alive --> each of them lose 1 hp
            self.check_both_pokemon_not_fainted(team1_pokemon, team2_pokemon)

            # check if both pokemon still alive
            if (not team1_pokemon.is_fainted()) and (not team2_pokemon.is_fainted()):
                self.team1.team.append(team1_pokemon)
                self.team2.team.append(team2_pokemon)

            # check if team 1 pokemon fainted (and team 2 pokemon alive)
            elif team1_pokemon.is_fainted() and (not team2_pokemon.is_fainted()):
                team2_pokemon.level_up()
                self.team2.team.append(team2_pokemon)

            # check if team 2 pokemon fainted (and team 1 pokemon alive)
            elif team2_pokemon.is_fainted() and (not team1_pokemon.is_fainted()):
                team1_pokemon.level_up()
                self.team1.team.append(team1_pokemon)

            # Return result / winner / draw
        return self.return_result()

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        Allows 2 teams of Pokemon to battle using battle_mode 2.
        :param self:
        :param criterion_team1:
        :param criterion_team2:
        :return: string result of the battle
        complexity: O(n) n is the number of times the two teams battle when either teams are empty
        """
        self.battle_mode = 2
        self.criterion_team1 = criterion_team1
        self.criterion_team2 = criterion_team2
        self.team1 = PokeTeam(self.trainer_one)
        self.team1.choose_team(self.battle_mode, self.criterion_team1)
        self.team2 = PokeTeam(self.trainer_two)
        self.team2.choose_team(self.battle_mode, self.criterion_team2)

        while not self.team1.team.is_empty() and not self.team2.team.is_empty():

            # Call out pokemon
            team1_pokemon = self.team1.team.delete_at_index(0).value
            team2_pokemon = self.team2.team.delete_at_index(0).value

            # Pokemon attack each other
            # Check pokemon speed to decide which pokemon attack first
            self.pokemon_attack(team1_pokemon, team2_pokemon)

            # Both pokemon are still alive --> each of them lose 1 hp
            self.check_both_pokemon_not_fainted(team1_pokemon, team2_pokemon)

            # check if both pokemon still alive
            if (not team1_pokemon.is_fainted()) and (not team2_pokemon.is_fainted()):
                self.team1.team.add(
                    ListItem(team1_pokemon,
                             1000 - (team1_pokemon.get_criteria(self.criterion_team1) + team1_pokemon.get_constant())))
                self.team2.team.add(
                    ListItem(team2_pokemon,
                             1000 - (team2_pokemon.get_criteria(self.criterion_team2) + team2_pokemon.get_constant())))

            # check if team 1 pokemon fainted (and team 2 pokemon alive)
            elif team1_pokemon.is_fainted() and (not team2_pokemon.is_fainted()):
                team2_pokemon.level_up()
                self.team2.team.add(ListItem(team2_pokemon, 1000 - (
                        team2_pokemon.get_criteria(self.criterion_team2) + team2_pokemon.get_constant())))

            # check if team 2 pokemon fainted (and team 1 pokemon alive)
            elif team2_pokemon.is_fainted() and (not team1_pokemon.is_fainted()):
                team1_pokemon.level_up()
                self.team1.team.add(ListItem(team1_pokemon, 1000 - (
                        team1_pokemon.get_criteria(self.criterion_team1) + team1_pokemon.get_constant())))

        # Return result / winner / draw
        return self.return_result()
