""" pokemon.py: Holds 3 classes - Charmander, Bulbasaur, Squirtle """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from random import random
from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    # class variables
    SPEED = 7
    DEFENCE = 4
    ATTACK = 6
    NAME = "Charmander"
    CONSTANT = 3

    def __init__(self, hp=7, poke_type="FIRE") -> None:
        """
        Instantiating instance variable
        :param self:
        :param hp:
        :param poke_type:
        :return: Returns None
        """
        super().__init__(hp, poke_type)

    def get_speed(self) -> int:
        """
        A method to get the speed of Charmander
        :param self:
        :return: Returns the speed of Charmander
        complexity: O(1)
        """
        return self.SPEED + self.get_level()

    def get_defence(self) -> int:
        """
        A method to get the defence of Charmander
        :param self:
        :return: Returns the defence of Charmander
        complexity: O(1)
        """
        return self.DEFENCE

    def get_attack(self) -> int:
        """
        A method to get the attack of Charmander
        :param self:
        :return: Returns the attack of Charmander
        complexity: O(1)
        """
        return self.ATTACK + self.get_level()

    def damage_taken(self, opponent: PokemonBase) -> int:
        """
         A method to get the damage taken by Charmander
         :param self:
         :param opponent:
         :return: Returns the damage taken by Charmander
         complexity: O(1)
         """
        damage = opponent.get_attack()
        opp_poke_type = opponent.get_poke_type()

        if damage >= 0:  # check whether the damage is positive or not
            # Type Effectiveness
            if opp_poke_type in ["FIRE", "WATER", "GRASS"]:
                if opp_poke_type == "WATER":
                    damage = damage * 2
                elif opp_poke_type == "GRASS":
                    damage = damage * 0.5
            else:
                raise ValueError("Attack type is invalid.")
            # Damage after being attacked
            if damage > self.get_defence():
                return damage
            else:
                return damage // 2
        else:
            raise ValueError("Damage is invalid.")

    def get_poke_name(self) -> str:
        """
        A method to get the name of the pokemon
        :param self:
        :return: Returns the name "Charmander"
        complexity: O(1)
        """
        return self.NAME

    # method to get the constant for optimised_mode_battle sequence
    def get_constant(self) -> int:
        """
        Obtain the constant value that is set for each pokemon
        :param self:
        :return: an integer based on the pokemon type
        complexity: O(1)
        """
        return self.CONSTANT


class Bulbasaur(PokemonBase):
    # class variable
    SPEED = 7
    DEFENCE = 5
    ATTACK = 5
    NAME = "Bulbasaur"
    CONSTANT = 2

    def __init__(self, hp=9, poke_type="GRASS") -> None:
        """
        Instantiating instance variable
        :param self:
        :param hp:
        :param poke_type:
        :return: Returns None
        """
        super().__init__(hp, poke_type)

    def get_speed(self) -> int:
        """
        A method to get the speed of Bulbasaur
        :param self:
        :return: Returns the speed of Bulbasaur
        complexity: O(1)
        """
        return self.SPEED + (self.get_level() // 2)

    def get_defence(self) -> int:
        """
        A method to get the defence of Bulbasaur
        :param self:
        :return: Returns the defence of Bulbasaur
        complexity: O(1)
        """
        return self.DEFENCE

    def get_attack(self) -> int:
        """
        A method to get the attack of Bulbasaur
        :param self:
        :return: Returns the attack of Bulbasaur
        complexity: O(1)
        """
        return self.ATTACK

    def damage_taken(self, opponent: PokemonBase) -> int:
        """
        A method to get the damage taken by Bulbasaur
        :param self:
        :param opponent:
        :return: Returns the damage taken by Bulbasaur
        complexity: O(1)
        """
        damage = opponent.get_attack()
        opp_poke_type = opponent.get_poke_type()

        # check whether the damage is positive or not
        if damage >= 0:
            # Type Effectiveness
            if opp_poke_type in ["FIRE", "WATER", "GRASS"]:
                if opp_poke_type == "FIRE":
                    damage = damage * 2
                elif opp_poke_type == "WATER":
                    damage = damage * 0.5
            else:
                raise ValueError("Attack type is invalid.")

            # Damage after being attacked
            if damage > self.get_defence() + 5:
                return damage
            else:
                return damage // 2
        else:
            raise ValueError("Damage is invalid.")

    def get_poke_name(self) -> str:
        """
        A method to get the name of the pokemon
        :param self:
        :return: Returns the name "Bulbasaur"
        complexity: O(1)
        """
        return self.NAME

    # method to get the constant for optimised_mode_battle sequence
    def get_constant(self) -> int:
        """
        Obtain the constant value that is set for each pokemon
        :param self:
        :return: an integer based on the pokemon type
        complexity: O(1)
        """
        return self.CONSTANT


class Squirtle(PokemonBase):
    # class variable
    SPEED = 7
    DEFENCE = 6
    ATTACK = 4
    NAME = "Squirtle"
    CONSTANT = 1

    def __init__(self, hp=8, poke_type="WATER") -> None:
        """
        Instantiating instance variable
        :param self:
        :param hp:
        :param poke_type:
        :return: Returns None
        """
        super().__init__(hp, poke_type)

    def get_speed(self) -> int:
        """
        A method to get the speed of Squirtle
        :param self:
        :return: Returns the speed of a Squirtle
        complexity: O(1)
        """
        return self.SPEED

    def get_defence(self) -> int:
        """
        A method to get the defence of Squirtle
        :param self:
        :return: Returns the defence of Squirtle
        complexity: O(1)
        """
        return self.DEFENCE + self.get_level()

    def get_attack(self) -> int:
        """
        A method to get the attack of Squirtle
        :param self:
        :return: Returns the attack of Squirtle
        complexity: O(1)
        """
        return self.ATTACK + (self.get_level() // 2)

    def damage_taken(self, opponent: PokemonBase) -> int:
        """
        A method to get the damage taken by Squirtle
        :param self:
        :param opponent:
        :return: Returns the damage taken by Squirtle
        complexity: O(1)
        """
        damage = opponent.get_attack()
        opp_poke_type = opponent.get_poke_type()

        # check whether the damage is positive or not
        if damage >= 0:
            # Type Effectiveness
            if opp_poke_type in ["FIRE", "WATER", "GRASS"]:
                if opp_poke_type == "GRASS":
                    damage = damage * 2
                elif opp_poke_type == "FIRE":
                    damage = damage * 0.5
            else:
                raise ValueError("Attack type is invalid.")

            # Damage after being attacked
            if damage > self.get_defence() * 2:
                return damage
            else:
                return damage // 2
        else:
            raise ValueError("Damage is invalid.")

    def get_poke_name(self) -> str:
        """
        A method to get the name of the pokemon
        :param self:
        :return: Returns the name "Squirtle"
        complexity: O(1)
        """
        return self.NAME

    # method to get the constant for optimised_mode_battle sequence
    def get_constant(self) -> int:
        """
        Obtain the constant value that is set for each pokemon
        :param self:
        :return: an integer based on the pokemon type
        complexity: O(1)
        """
        return self.CONSTANT
