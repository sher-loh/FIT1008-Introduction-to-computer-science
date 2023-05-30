""" pokemon_base.py: Holds the abstract pokemon class."""
__author__ = "Abdul Harith Abdul Halim , Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from abc import ABC, abstractmethod


class PokemonBase(ABC):

    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Instantiating instance variable
        :param self:
        :param hp:
        :param poke_type:
        :return: Returns None
        """
        self.set_level(1)
        # set hp
        # pre-condition using exception
        # hp >= 0
        try:
            self.set_hp(hp)
        except ValueError:
            print("Not a valid HP, HP must be greater than or equal to 0")

        # set PokeType
        # pre-condition using exception
        try:
            self.set_poke_type(poke_type)
        except TypeError:
            print("Not a valid PokeType, PokeType must be either GRASS, FIRE or WATER")

    # class level methods
    def get_hp(self) -> int:
        """
        A method to retrieve the HP of a pokemon
        :param self:
        :return: returns the hp of a pokemon
        complexity: O(1)
        """
        return self.hp

    def set_hp(self, hp: int) -> None:
        """
        A method to set the HP of a pokemon
        :param self :
        :param hp:
        :return: Sets the pokemon with a value of HP
        complexity: O(1)
        """
        if hp >= 0:
            self.hp = hp
        else:
            raise ValueError("HP is invalid, HP must be greater than or equal to 0")

    def get_level(self) -> int:
        """
        A method to get the level of a pokemon
        :param self:
        :return: returns the level of a pokemon
        complexity: O(1)
        """
        return self.level

    def set_level(self, level: int) -> None:
        """
        A method to set the level of a pokemon
        :param self:
        :param level:
        :return: Sets the pokemon with a value of level
        complexity: O(1)
        """
        if level >= 1:
            self.level = level
        else:
            raise ValueError("level is invalid")

    def set_poke_type(self, poke_type: str or None) -> None:
        """
        A method to set the type of pokemon
        :param self:
        :param poke_type:
        :return: Sets the pokemon with a value of level
        complexity: O(1)
        """
        if poke_type in ["GRASS", "FIRE", "WATER", None]:
            self.poke_type = poke_type
        else:
            raise TypeError("PokeType is invalid, PokeType must be either GRASS, FIRE, WATER or None")

    def get_poke_type(self) -> str:
        """
        A method to get the type of a pokemon
        :param self:
        :return: returns the type of a pokemon
        complexity: O(1)
        """
        return self.poke_type

    def is_fainted(self) -> bool:
        """
        Check whether the pokemon has fainted
        :param self:
        :return: return True if the hp of the pokemon is <=0 or False if otherwise
        complexity : O(1)
        """
        if self.hp <= 0:
            return True
        else:
            return False

    def level_up(self) -> None:
        """
        Increase the level of a pokemon
        :param self:
        :return: increases the level of pokemon by 1
        complexity: O(1)
        """
        self.set_level(self.get_level() + 1)

    def lose_hp(self, lost_hp: int) -> None:
        """
        Decreases the hp of a pokemon
        :param self:
        :param lost_hp:
        :return: decreases the hp of pokemon by 1
        complexity: O(1)
        """
        if self.get_hp() - lost_hp < 0:
            self.set_hp(0)
        else:
            self.set_hp(self.get_hp() - lost_hp)

    def get_criteria(self, criteria: str) -> int:
        """
        Obtain the criteria of a pokemon
        :param self:
        :param criteria:
        :return: the integer value of the pokemon based on the criteria
        complexity: O(1)
        """
        if criteria == "Level":
            return self.get_level() * 10
        elif criteria == "HP":
            return self.get_hp() * 10
        elif criteria == "Attack":
            return self.get_attack() * 10
        elif criteria == "Defence":
            return self.get_defence() * 10
        else:
            return self.get_speed() * 10

    # abstract methods
    @abstractmethod
    def get_speed(self) -> int:
        """
        An abstract method to allow the speed of a pokemon to be retrieved
        :param self:
        """
        pass

    @abstractmethod
    def damage_taken(self, opponent) -> int:
        """
        An abstract method to allow the damage taken by a pokemon to be retrieved
        :param self:
        :param opponent:
        """
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """
        An abstract method to allow the defence of a pokemon to be retrieved
        :param self:
        """
        pass

    @abstractmethod
    def get_attack(self) -> int:
        """
        An abstract method to allow the attack of a pokemon to be retrieved
        :param self:
        """
        pass

    @abstractmethod
    def get_poke_name(self) -> str:
        """
        A method to get the name of a pokemon
        :param self:
        :return: returns the name of a pokemon
        """
        pass

    # method to get the constant for optimised_mode_battle sequence
    @abstractmethod
    def get_constant(self) -> int:
        """
        Obtain the constant value that is set for each pokemon
        :param self:
        :return: an integer based on the pokemon type
        """
        pass

    def __str__(self) -> str:
        """
        A string to return details on a pokemon
        :param self:
        :return: Returns details on a pokemon in a formatted string.
        complexity: O(1)
        """
        if self.poke_type == "FIRE":
            return "Charmander's HP = " + str(int(self.hp)) + " and level = " + str(self.level)

        if self.poke_type == "GRASS":
            return "Bulbasaur's HP = " + str(int(self.hp)) + " and level = " + str(self.level)

        if self.poke_type == "WATER":
            return "Squirtle's HP = " + str(int(self.hp)) + " and level = " + str(self.level)

        if self.poke_type is None:
            return "MissingNo's HP = " + str(int(self.hp)) + " and level = " + str(self.level)
