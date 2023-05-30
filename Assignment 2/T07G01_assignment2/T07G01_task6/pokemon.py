""" pokemon.py: Holds 5 classes - Charmander, Bulbasaur, Squirtle, GlitchMon and MissingNo. """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from random import randint
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
            if opp_poke_type in ["FIRE", "WATER", "GRASS", None]:
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
            if opp_poke_type in ["FIRE", "WATER", "GRASS", None]:
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
            if opp_poke_type in ["FIRE", "WATER", "GRASS", None]:
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


from abc import ABC, abstractmethod


class GlitchMon(PokemonBase, ABC):
    """
    GlitchMon that contains two extra methods in addition to
    the base class that you created for the previous 3 Pokemon.
    """

    def __init__(self, hp, poke_type=None) -> None:
        """
        Instantiation of instance variable
        :param self:
        :param hp:
        :param poke_type:
        :return: Returns None
        """
        super().__init__(hp, poke_type)

    def increase_hp(self, increase_hp: int) -> None:
        """
        A method to increase the HP
        :param self:
        :param increase_hp
        :return: return None
        complexity: O(1)
        """
        self.set_hp(self.get_hp() + increase_hp)

    def superpower(self) -> None:
        """
        A method which has a random chance to choose one of three effects
        :param self:
        :return: return None
        complexity: O(1)
        """
        random_number = randint(1, 3)
        # When random_number is 1, Gain 1 level
        if random_number == 1:
            self.level_up()
        # When random_number is 2, Gain 1 HP
        elif random_number == 2:
            self.increase_hp(1)
        # When random_number is 3, Gain 1 HP and 1 level
        else:
            self.level_up()
            self.increase_hp(1)

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


class MissingNo(GlitchMon):
    """
    MissingNo is a child of this GlitchMon class.
    """

    # class variables
    SPEED = 22 / 3  # [(7 + 1) + (7 + 1//2) + 7] / 3 + LEVEL
    DEFENCE = 16 / 3  # [4 + 5 + (6 + 1)] / 3 + LEVEL
    ATTACK = 16 / 3  # [(6 + 1) + 5 + (4 + 1//2)] / 3 + LEVEL
    NAME = "MissingNo"
    CONSTANT = 0

    def __init__(self, hp=8, poke_type=None) -> None:
        """
        Instantiation of instance variable
        :param self:
        :param hp:
        :param poke_type:
        :return: Returns None
        """
        super().__init__(hp, poke_type)

    def get_hp(self):
        """
        A method to get the hp of MissingNo
        :param self:
        :return: Returns the hp of MissingNo
        complexity: O(1)
        """
        return self.hp + self.get_level() - 1

    def get_speed(self) -> float:
        """
        A method to get the speed of MissingNo
        :param self:
        :return: Returns the speed of MissingNo
        complexity: O(1)
        """
        if int(self.SPEED + self.get_level() - 1) >= int(22/3):
            return self.SPEED + self.get_level() - 1
        else:
            raise ValueError("Speed cannot be lower than 22/3")

    def get_defence(self) -> float:
        """
        A method to get the defence of MissingNo
        :param self:
        :return: Returns the defence of MissingNo
        complexity: O(1)
        """
        if int(self.DEFENCE + self.get_level() - 1) >= int(16 / 3):
            return self.DEFENCE + self.get_level() - 1
        else:
            raise ValueError("Defence cannot be lower than 16/3 ")

    def get_attack(self) -> float:
        """
        A method to get the attack of MissingNo
        :param self:
        :return: Returns the attack of MissingNo
        complexity: O(1)
        """
        if int(self.ATTACK + self.get_level() - 1) >= int(16 / 3):
            return self.ATTACK + self.get_level() - 1
        else:
            raise ValueError("Attack cannot be lower than 16/3 ")

    def damage_taken(self, opponent: PokemonBase) -> int:
        """
        A method to get the damage taken by MissingNo
        :param self:
        :param opponent:
        :return: Returns the damage taken by MissingNo
        complexity: O(1)
        """
        damage = opponent.get_attack()

        if damage >= 0:  # check whether the damage is positive or not
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
        :return: Returns the name "MissingNo"
        complexity: O(1)
        """
        return self.NAME

    def get_constant(self) -> int:
        """
        Obtain the constant value that is set for each pokemon
        :param self:
        :return: an integer based on the pokemon type
        complexity: O(1)
        """
        return self.CONSTANT
