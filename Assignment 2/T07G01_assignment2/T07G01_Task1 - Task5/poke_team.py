"""poke_team.py: Enables users to assemble the teams."""
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from array_sorted_list import ArraySortedList
from pokemon import Charmander, Bulbasaur, Squirtle
from queue_adt import CircularQueue
from sorted_list import ListItem
from stack_adt import ArrayStack


def check_criterion(criterion: str) -> bool:
    """
    Check the battle_mode whether is Level, HP, Attack, Defense, Speed or None
    :param criterion:
    :return: return True if is Level, HP, Attack, Defense, Speed or None; else return False
    complexity : O(1)
    """
    if criterion not in ["Level", "HP", "Attack", "Defense", "Speed", None]:
        raise ValueError("Criterion can only be Level, HP, Attack, Defense, Speed or None ; else valid")
    return True


def check_battle_mode(battle_mode: int) -> bool:
    """
    Check the battle_mode whether is 0, 1, 2.
    :param battle_mode:
    :return: return True if is 0, 1, 2; else raise ValueError.
    complexity: O(1)
    """
    if battle_mode not in [0, 1, 2]:
        raise ValueError("battle_mode only can be 0, 1, 2, else valid")
    return True


def check_input(charm: int, bulb: int, squir: int) -> bool:
    """
    Check the user input for pokemon team is valid or not.
    :param charm:
    :param bulb:
    :param squir:
    :return: return True if pokemon team input is valid; else raise ValueError.
    complexity: O(1)
    """
    # The total numbers of Pokemon cannot be greater than 6
    if charm + bulb + squir > 6:
        raise ValueError("The team cannot have more than 6 Pokemon")
    # Each number of Pokemon type cannot be negative
    elif charm < 0 or bulb < 0 or squir < 0:
        raise ValueError("The number of Pokemon cannot be negative")
    # Total number of pokemon in team cannot be 0
    elif charm + bulb + squir == 0:
        raise ValueError("The team cannot have 0 Pokemon")
    else:
        return True


class PokeTeam:
    """
    PokeTeam is to take input from user and assemble the pokemon team.
    choose_team: take input from user and check whether is valid.
    assign_team: if input in choose_team is valid, pass values to assign_team.
    battle mode = 0 (assign team using Stack ADT)
    battle mode = 1 (assign team using CircularQueue ADT)
    battle mode = 2 (assign team using SortedList ADT)
    """

    def __init__(self, trainer_name) -> None:
        """
        Initialize PokeTeam variables.
        :param self:
        :param trainer_name:
        :return: Returns None
        """
        self.trainer_name = trainer_name
        self.team = None
        self.battle_mode = 0
        self.criterion = None

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """
        Check input, battle mode and criteria is valid, then assign team
        :param self:
        :param battle_mode:
        :param criterion:
        :return: return None
        complexity: O(1)
        """
        # Set battle mode (battle_mode only can be 0, 1, 2)
        # Check for battle_mode precondition using valid_mode
        valid_mode = False
        while not valid_mode:
            try:
                check_battle_mode(battle_mode)
            except ValueError:
                print("Not a valid battle_mode, battle_mode only can be 0, 1, 2, please input again")
                battle_mode = int(input())
            else:
                self.battle_mode = battle_mode
                valid_mode = True

        # Set criterion
        valid_criterion = False
        while not valid_criterion:
            try:
                check_criterion(criterion)
            except ValueError:
                print(
                    "Not a valid criterion, criterion can only be Level, HP, Attack,"
                    "Defense, Speed or None. Please enter input again")
                criterion = str(input())
            else:
                self.criterion = criterion
                valid_criterion = True

        # print the prompt
        print("Howdy Trainer! Choose your team as C B S")
        print("where C is the number of Charmanders")
        print("      B is the number of Bulbasaurs")
        print("      S is the number of Squirtles")

        # Set the pokemon team
        # Check for team precondition using valid_team
        valid_team = False
        while not valid_team:
            try:
                lst = list(map(int, input().split()))  # Split the user's input and change string to int, store in lst
                no_of_charm = lst[0]  # The 1st element in lst is the number of charm
                no_of_bulb = lst[1]  # The 2nd element in lst is the number of bulb
                no_of_squir = lst[2]  # The 3rd element in lst is the number of squir
                check_input(no_of_charm, no_of_bulb, no_of_squir)
            except ValueError:
                print(
                    "The team can only have 1 to 6 Pokemon and the number of Pokemon can only be "
                    "positive integer. Please try again.")
            except IndexError:
                print("Invalid input, input must be in the form of C B S. Please try again.")
            else:
                self.assign_team(no_of_charm, no_of_bulb, no_of_squir)
                valid_team = True

    def assign_team(self, charm: int, bulb: int, squir: int) -> None:
        """
        After input is valid, team will store the charm, bulb and squir pokemons in different ADT depending on battle_mode.
        :param self:
        :param charm:
        :param bulb:
        :param squir:
        :return: return None
        complexity: O(1)
        """
        # If battle_mode is 0 -> Set Mode battle (Stack ADT)
        if self.battle_mode == 0:
            self.team = ArrayStack(charm + bulb + squir)
            for i in range(squir):
                self.team.push(Squirtle())
            for i in range(bulb):
                self.team.push(Bulbasaur())
            for i in range(charm):
                self.team.push(Charmander())

        # If battle_mode is 1 -> Rotating Mode battle (CircularQueue ADT)
        elif self.battle_mode == 1:
            self.team = CircularQueue(6)
            for i in range(charm):
                self.team.append(Charmander())
            for i in range(bulb):
                self.team.append(Bulbasaur())
            for i in range(squir):
                self.team.append(Squirtle())

        # If battle_mode is 2 -> Optimised Mode Battle (SortedList ADT)
        else:
            self.team = ArraySortedList(charm + bulb + squir)

            for i in range(charm):
                # creating a Charmander object
                c = Charmander()
                # Charmander constant = 3 , incase there is same value in the criteria
                self.team.add(ListItem(c, 1000 - (c.get_criteria(self.criterion) + c.get_constant())))

            for i in range(bulb):
                # creating a Bulbasaur object
                b = Bulbasaur()
                # Bulbasaur constant = 2 , incase there is same value in the criteria
                self.team.add(ListItem(b, 1000 - (b.get_criteria(self.criterion) + b.get_constant())))

            for i in range(squir):
                # creating a Squirtle object
                s = Squirtle()
                # Squirtle constant = 1 , incase there is same value in the criteria
                self.team.add(ListItem(s, 1000 - (s.get_criteria(self.criterion) + s.get_constant())))

    def __str__(self) -> str:
        """
        A string to return details of the team.
        :param self:
        :return: the details of the team in a formatted string.
        complexity: O(n), n is length of self.team
        """
        return str(self.team)
