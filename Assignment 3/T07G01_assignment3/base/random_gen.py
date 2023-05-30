"""random_gen.py contains the class RandomGen"""
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"

from typing import Generator


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed


class RandomGen:
    """
    RandomGen allows us to generate 5 numbers and drop 16 bits for each of them. These numbers are then referred to
    per column and if the total binary number per column is >=3 the new binary bit will be 1, 0 otherwise.
    This is then converted into a decimal number.
    """

    def __init__(self, seed: int = 0) -> None:
        """
        Initialises the variables
        :param self:
        :param seed:
        :returns: initialises the variables
        :complexity: O(1)
        """
        self.seed = seed
        self.random_gen = lcg(pow(2, 32), 134775813, 1, seed)

    def randint(self, k: int) -> int:
        """
        A method that generates a random number via 5 others
        Approach: "numbers" is a list to contain the random numbers.
                  The first for...loop is implemented in such a way that random numbers are generated and appended to
                  "numbers".Once there are 5 numbers, this process is stopped via the break function.
                  The second for...loop is the implementation of dropping the last 6 bits of any given number
                  via python's bitwise operator indicated by >>16. Given that 5 numbers are to be generated,
                  the list of numbers is passed through count_one, a method that counts number of 1's in a
                  binary number. The numbers are converted into binary via the division and remainder process
                  where the remainder indicates the bit at which will be counted towards.
                  Going through the numbers one at a time, and eventually all of them.
                  The number ones in the same bit is checked. If in the same bit, the number of ones is
                  greater or equal than 3, it will return a true. This carries back into the third for...loop which
                  proceeds to convert the binary number generated into decimal for the calculation (number % k) + 1.
                  The conversion adheres to the multiplication process which is to multiply the bits by their power of
                  2 via the number and factor variables.
        :param self:
        :param k:
        :returns: Returns a random number
        complexity: O(1)
        pre-condition: k is != 0
        post-condition: random numbers generated > 0
        invariant: len(numbers) == 5
        """
        numbers = []  # array for random numbers
        number = 0
        factor = 1
        for j in self.random_gen:
            numbers.append(j)
            if len(numbers) == 5:  # stop when there are 5 numbers in the list
                break

        for i in range(len(numbers)):
            numbers[i] = numbers[i] >> 16  # shift the bits by 16

        for i in range(16):  # representing 16 binary bits
            if self.count_one(numbers):  # calls count_one to count the number of 1's in each random number and if true,
                number = number + factor  # number +factor

            factor = factor * 2

        return (number % k) + 1

    def count_one(self, List: list) -> bool:
        """
        A method that counts the number of ones in the random numbers
        :param self:
        :param List:
        :returns: Returns True if the numberofones is >=3 amd False if <3
        :complexity: O(1)
        :pre-condition: len(List) == 5
        :post-condition: numberofones cannot be < 0
        :invariant: i cannot be more than 5
        """
        numberofones = 0
        for i in range(5):
            if List[i] % 2 == 1:
                numberofones += 1

            List[i] //= 2

        if numberofones >= 3:  # if random digit is more than 3, return true
            return True
        return False


if __name__ == "__main__":
    generator = RandomGen()
    # print(generator.randint(74))
