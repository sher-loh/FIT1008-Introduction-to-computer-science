""" primes.py : contains th method largest_prime """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"


def largest_prime(k: int) -> int:
    """
    A method that generates a prime number.
    Approach : Line 30 to 39 implements Sieve of Eratosthenes algorithm to generate prime
               numbers lower than k but greater or equal to 2. These prime numbers are then appended into a list
               called "final".If the value k is in the list, that value in the list will be removed. For instance,
               when k is 3,the prime numbers generated are 2 and 3. 3 will be removed from "final".
               This means 2 is the largest prime number strictly lesser than k.
               This coincides with the condition in line 48 saying that if the number of primes in "final" is 1,
               that number is will be the output. Once these conditions have been implemented, we proceed to finding
               the largest number in the list "final". This will lead to the desired output.

    Example 1:
    when k is 5, final will be [2,3,5]. 5 will be removed from the list resulting in [2,3]. 3 will be the output.

    Example 2:
    when k is 3, final will be [2,3]. 3 will be removed from the list resulting in [2]. 2 is the output.

    :param k:
    :returns: Returns the largest prime number strictly lesser than k.
    complexity: O(nlog(logn)) + O(n) = O(nlog(log(n)) , n is number of prime numbers generated
    pre-condition: k is larger than 2
    post-condition: "largest" is the largest number in the list "final"
    invariant: "final" holds all prime numbers lesser than k
    """
    max = k + 1
    lst = [True] * max
    for i in range(2, int(k ** 0.5 + 1)):
        if lst[i]:
            for j in range(i * i, max, i):
                lst[j] = False
    final = []
    for i in range(2, max):
        if lst[i]:
            final.append(i)

    temp_num = final[0]
    largest = 0

    for j in final:
        if j == k:
            final.pop()

    if len(final) == 1:
        largest = final[0]

    else:
        for i in final:
            if i > temp_num:
                largest = i
    return largest
