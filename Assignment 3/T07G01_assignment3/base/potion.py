""" potion.py : contains class Potion that hold the hash methods as well as the init method """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"


class Potion:
    """
    Potion class allows us to create an object for the potions.Since these potions will eventually be stored in a hash
    table, we also need a way to hash them
    create_empty : creates potions with 0 quantity
    good_hash : hashes a potion name, given a fixed table size.
    bad_hash : hashes a potion name, given a fixed table size.
    """

    def __init__(self, potion_type: str, name: str, buy_price: float, quantity: float) -> None:
        """
        Initialise Potion variables
        :param self:
        :param potion_type:
        :param name:
        :param buy_price:
        :param quantity:
        :return: Returns None
        complexity: O(1)
        """
        self.potion_type = potion_type
        self.name = name
        self.buy_price = buy_price
        self.quantity = quantity

    @classmethod
    def create_empty(cls, potion_type: str, name: str, buy_price: float) -> 'Potion':
        """
        A class method to creates a potion with 0 quantity
        every time the class method is called, it will create potion and set the quatity to 0
        :param cls:
        :param potion_type:
        :param name:
        :param buy_price:
        :return: Returns the classification of potion with quantity 0
        complexity: O(1)
        post-condition: quantity of the potion = 0
        """
        return cls(potion_type, name, buy_price, quantity=0)

    @classmethod
    def good_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        A class method that hashes the potion name to a specific index position
        Approach : This method uses the universal hash function where a = 31415 (base) and b = 27183
                   It converts each character in the potion name into a number based on the ASCII table,
                   it then adds with the (value*a) and lastly it is mod with the table size.
                   Once the for...loop is done, it will return the final value which determines the position
                   of the potion name in the hash table
        Example  : Potion name = "Potion of Health"
                    table size = 20
                    position of the potion after good hash = 12
        :param cls:
        :param potion_name:
        :param tablesize:
        :return: Returns the hash value of potion_name
        complexity: O(1)
        pre-condition: len(potion_name) != 0
        post-condition: value is the sum of (ord(char) + a * value) % tablesize, for every char in potion name
        invariant: value is always the sum of (ord(char) + a * value) % tablesize,for each char the for...loop iterated
        """
        value = 0
        a = 31415
        b = 27183
        for char in potion_name:
            value = (ord(char) + a * value) % tablesize
            a = a * b % (tablesize - 1)
        return value

    @classmethod
    def bad_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        A class method that hashes the potion name to a specific index position
        Approach : This method uses the universal hash function where a = 35415 (base) and b = 29183
                   It converts each character in the potion name into a number based on the ASCII table,
                   it then adds with the (value*a) and lastly it is mod with the table size.
                   Once the for...loop is done, it will return the final value which determines the position
                   of the potion name in the hash table. However, the bad hash only take into account
                   the first two characters in the given string
         Example  : Potion name = "Potion of Health"
                    table size = 20
                    position of the potion after good hash = 2
         :param cls:
         :param potion_name:
         :param tablesize:
         :return: Returns the hash value of potion_name
         complexity: O(1)
         pre-condition: len(potion_name) != 0
         post-condition: value is the sum of (ord(char) + a * value) % tablesize, for the first two char in potion name
         invariant: value is always the sum of (ord(char) + a * value) % tablesize,for the first two char the for...loop
                    iterated
         """
        val = 0
        a = 35415
        b = 29183
        for char in potion_name:
            for i in range(0, 1):
                val = (ord(char[i]) + a * val) % tablesize
                a = a * b % (tablesize - 1)

        return val

