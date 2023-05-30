from __future__ import annotations

# ^ In case you aren't on Python 3.10
"""game.py contains the class RandomGen"""
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from random_gen import RandomGen
from hash_table import LinearProbePotionTable
from avl import AVLTree
from potion import Potion


class Game:
    """
    ADT used for your approach:
    why were they used:
    """

    def __init__(self, seed=0) -> None:
        """
         Initialises the variables
        :param self:
        :param seed:
        :returns: Returns None
        complexity: O(1)
        """
        self.rand = RandomGen(seed=seed)
        self.potion_data_hash = None
        self.potion_data_AVL = None

    def set_total_potion_data(self, potion_data: list) -> None:
        """
        A method that create a hash table to store the potion object
        (data about the potions including potion type, name, buying price and quantity)
        :param self:
        :param potion_data:
        :returns: None
        complexity: best = worst = O(N), N is number of element in potion_data list
        complexity explanation: the for loop has complexity of O(N)
        pre-condition: potion_data is not an empty list
        post-condition: creates hash table which stores the potion object using the potion name as key
        invariant: p (potion object) created has quantity = 0
        """
        # Create hash table to store potion object
        # Initialise hash table
        self.potion_data_hash = LinearProbePotionTable(len(potion_data))
        for i in range(len(potion_data)):  # O(N)
            # Create empty potion
            p = Potion.create_empty(potion_data[i][1], potion_data[i][0], potion_data[i][2])
            # Use potion name as key and stores potion object in hash table
            self.potion_data_hash.__setitem__(p.name, p)

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        """
         This method update the quantity of the potions for each potion's object in the hash table's.
         Approach : The method also creates an AVL tree to store the potion's name and it's buying price
                    for potion with quantity > 0. The tree will be use as an inventory.
        :param self:
        :param potion_name_amount_pairs:
        :returns: None
        complexity: O(Clog(n)), C is the number of potions in stock (length of potion_name_amount_pairs list)
                                 n is number of nodes in AVL tree
        complexity explanation: C because of the for loop
                                log(n) because __setitem__ function for AVL tree has a complexity of log(n)
        pre-condition: potion_name_amount_pairs cannot be empty and the potion name must exist in the hash table
        post-condition: the hash table is updated with the quantity
        """
        self.potion_count = len(potion_name_amount_pairs)
        # Initialise AVL Tree
        self.potion_data_AVL = AVLTree()
        for i in range(len(potion_name_amount_pairs)):  # O(C)
            # Update potion quantity in Hash table
            p = self.potion_data_hash.__getitem__(potion_name_amount_pairs[i][0])
            p.quantity = potion_name_amount_pairs[i][1]
            # Create AVL tree for potion which has >0 quantity
            potion_price = p.buy_price
            # Use potion price as key, potion name as item for tree node
            self.potion_data_AVL.__setitem__(potion_price, potion_name_amount_pairs[i][0])  # O(log(n))

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        """
        A method that returns a list, specifying what the vendors will sell.
        Approach : Using the RandomGen class, vendor can generate a random number p.
                   We call kth_largest method for the AVL tree to get the pth most expensive potion for the vendor.
                   After the vendor collects the potion, potion is deleted from the inventory
                   (AVL tree) to avoid next vendors from taking the same potion.
                   The potion deleted will be added back into the inventory after all vendors took their potions.
        :param self:
        :param num_vendors:
        :returns: Returns a list of tuple of 2 values (potion name and potion quantity) on what the vendors will sell.
        complexity: O(Clog(n)), C is the number of potions in stock (length of potion_name_amount_pairs list)
                                n is number of nodes in AVL tree
        complexity explanation: (i) first for-loop: the for loop has complexity of O(C)
                                                    __delitem__ function for AVL tree has complexity of O(log(n)).
                                                    kth_largest function for AVL tree has complexity of O(log(n)).
                                                    Hence, in total first for-loop has complexity of O(Clog(n)).
                                (ii) second for-loop: the for loop has complexity of O(C)
                                                      __setitem__ function for AVL tree has complexity of O(log(n)).
                                                      Hence, in total second for-loop has complexity of O(Clog(n)).
                                both the first and second for loop has a complexity of O(Clog(n)).
                                Addition of the complexity gives O(Clog(n)) + O(Clog(n)) = O(2Clog(n)),
                                this can be simplified to O(Clog(n)).
        pre-condition: number of vendors is a non-negative integer
        post-condition: returned list will contain the potions for the vendors to sell and inventory (binary tree)
                        are not changed
        invariant: The random number generated is > 0
        """
        list = []
        r = RandomGen(seed=0)
        # (i) vendor selects the pth most expensive potions
        for i in range(num_vendors):  # O(C)
            p = r.randint(self.potion_count)
            # Find node from AVL tree using kth largest
            node = self.potion_data_AVL.kth_largest(p)  # O(log(n))
            # Find the name of the potion (which is the item of the node)
            potion_name = node.item
            # delete potion from AVL tree
            self.potion_data_AVL.__delitem__(node.key)  # O(log(n))
            self.potion_count -= 1
            # find the quantity of potion from hash table using potion_name (key)
            potion_quantity = self.potion_data_hash.__getitem__(potion_name).quantity
            # append name and quantity of potion
            list.append((potion_name, potion_quantity))

        # (ii) store potion back into AVL tree after all vendors selected potion
        for i in range(len(list)):  # O(C)
            self.potion_data_AVL.__setitem__(list[i][1], list[i][0])  # O(log(n))
            self.potion_count += 1

        return list

    def mergesort(self, ls):
        """
        merge sort is an algorithm used to sort any given list.
        Approach : In this case, we are attempting to sort the profit list
                   in ascending order. The method takes in a list as input (ls)
                   The algorithm attempts to split the profit list in the middle. These two lists are  then sorted
                   respectively. Once sorted, the "merge" method will be called to
                   finally append them back together, creating a new list that has been sorted as a whole.
        :param self:
        :param ls :
        :return: Returns a sorted list
        complexity: O(nlog(n)), n is the number of elements in ls
        pre-condition: len(ls) !=0
        post-condition: returned list is sorted ls
        invariant: nxt is a temporary list
        """
        k, n = 1, len(ls)
        while k < n:
            nxt = []
            for a in range(0, n, 2 * k):
                b, c = a + k, a + 2 * k
                nxt += self.merge(ls[a:b], ls[b:c])
            ls = nxt
            k = 2 * k
        return ls

    def merge(self, l1, l2):
        """
        merge is a method used to combine 2 halves of a sorted list split by their middle element.
        Approach : l1 and l2 are the two halves af a given list. res is the new list in which l1 and l2
                   will be concatenated and returned.
        :param self:
        :param l1:
        :param l2:
        :returns: Returns a list that is the result of 2 sorted lists
        complexity: O(n) , n is the number of elements in the l1 or l2
        pre-condition: l1 and l2 have to be sorted
        post-condition: l1 and l2 are merged and sorted
        invariant: There will always be 2 lists to be merged (l1 and l2)
        """
        res = []
        n1, n2 = len(l1), len(l2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if l1[i][1] <= l2[j][1]:
                res += [l1[i]]
                i += 1
            else:
                res += [l2[j]]
                j += 1
        return res + l1[i:] + l2[j:]

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        """
        A method which returns the list containing profit earned from each day.
        Approach : First, the method creates a list containing tuples of 2 values
                   (name of potion and the profit per litre from selling the potion).
                   Then, use the mergesort function to sort the list according to the profit of the
                   potions in ascending order.We will start by purchasing the potion with the
                   highest profit (last item in list) using the available money.
                   If there is any remaining money, we will purchase from the 2nd, 3rd, 4th highest
                   profit potion and so on.When the money is depleted, we will start with
                   new amount of money for the next day and repeat the purchase and selling.
        :param self:
        :param potion_valuations:
        :param starting_money:
        :returns: Returns a list of profits earn on each day.
        complexity: O(Nlog(N) + MN), N is length of potion_valuations lists and M is length of starting_money list
        complexity explanation: (i) first for-loop: the for-loop has complexity of O(N)
                                (ii) The mergesort used for potion_profit_list has complexity of O(Nlog(N))
                                (iii) for-loops for buying and selling: the outer for-loop has complexty of O(M)
                                                                        the inner for-loop has complexity of O(N)
                                                                        Hence, in total this part has complexity of O(MN).
                                Addition of the complexity of this 3 parts will result in O(N + Nlog(N) + MN),
                                which can be simplified to O(Nlog(N) + MN)
        pre-condition: potion_valuations and starting_money cannot be empty
                       potion_valuations has to be a list containing tuples of 2 values, name of potion and
                       profit per litre
        post-condition: returned list contain money earned on each day with the best sale plan
        """
        # (i) Create a potion_profit_list list to stores the profit of each potions
        potion_profit_list = []
        for i in range(len(potion_valuations)):  # O(N)
            # profit = selling_price / buying_price
            profit = potion_valuations[i][1] / self.potion_data_hash.__getitem__(potion_valuations[i][0]).buy_price
            # append name, profit, selling price into potion_profit_list
            potion_profit_list.append((potion_valuations[i][0], profit, potion_valuations[i][1]))

        # (ii) sort the potion_profit_list using mergesort
        potion_profit_list = self.mergesort(potion_profit_list)  # O(Nlog(N))

        # (iii) Buying and selling to get profit, append to result list
        res = []
        for i in range(len(starting_money)):  # O(M)
            money = starting_money[i]
            profit = 0
            n = len(potion_profit_list) - 1
            # buying from the potion with highest profit and so on
            for j in range(len(potion_profit_list)):  # O(N)
                # Get the potion name with nth highest profit
                potion = self.potion_data_hash.__getitem__(potion_profit_list[n - j][0])
                # Get potion selling_price from potion_profit_list
                potion_selling_price = potion_profit_list[n - j][2]
                # Find the amount of quantity we can purchase with the amount of money we have
                quantity_purchase = money / potion.buy_price
                # if the available quantity is lower than the amount to purchase is the quantity available
                if quantity_purchase > potion.quantity:
                    quantity_purchase = potion.quantity
                # Subtract money spent on buying potion from the money we have
                money -= quantity_purchase * potion.buy_price
                # Add revenue into profit
                profit += (quantity_purchase * potion_selling_price)
                # if money is used up, break inner for loop, proceed to next day
                if money <= 0:
                    break
            # append profit of the day to res list
            res.append(profit)

        return res
