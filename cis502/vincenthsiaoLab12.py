##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 12 - Multithreaded Programming
#  Application: Using threads in Python
#  Description: Runs 4 tests concurrently
#   using threads
#  Testing Validation: below
#  Version: Python 3.10
#  Development Environment: Sublime Text 4 for MacOS
#  Solution File:  vincenthsiaoLab12.py
#  Date: 11/28/2021
##

import threading
import random

def hailstoneSeq(n,start):
    #Hailstone sequence for every number up to N
    #From CIS 502 Assignment 3
    for i in range(1,n+1):
        li = [start]
        for k in range(i-1):
            if(li[-1] % 2 == 0):
                li.append(int(li[-1] / 2))
            else:
                li.append((3 * li[-1]) + 1)
        print("Hailstone sequence of length {} starting at {}: "
            .format(i,start),li)
    
def numbersSquared(n):
    for i in range(n):
        print("{}^2 =".format(i),i**2)

def primesBetween(n):
    primes = []
    sieve_primes = [2,3,5,7]
    #Lists out all prime numbers between 0 and n using Sieve of Erathoneses
    for i in range(n):
        if(i in sieve_primes):
            primes.append(i)
        elif(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
            primes.append(i)
    print(primes)
    print("# of Primes between 0 and {}:"\
        .format(n),len(primes))

def birthdayParadoxSim(n):
    #Birthday Paradox Simulation (Runs N number of tests)
    #From CIS 254 Assignment 13
    tests = []
    for i in range(n):
        people = []
        while True:
            curBirthday = random.randint(1,365)
            if(curBirthday in people):
                tests.append(len(people))
                break
            else:
                people.append(curBirthday)
    print("Average of {} Tests: {}".format(n,sum(tests)/n))


thread1 = threading.Thread(target=hailstoneSeq,args=(20,5))
thread2 = threading.Thread(target=numbersSquared,args=(10,))
thread3 = threading.Thread(target=primesBetween,args=(100,))
thread4 = threading.Thread(target=birthdayParadoxSim,args=(50,))

def main():
    print("Thread 1, Job 1: Hailstone Sequence of every number up to N \
starting at START (n=20,start=5)")
    thread1.start()

    #waits for thread to finish before starting second
    thread1.join()

    print("\nThread 2, Job 2: Squared of every value between zero and N (n=10)"
        )
    thread2.start()

    #waits for thread to finish before starting third
    thread2.join()

    print("\nThread 3, Job 3: Prime numbers between 0 and N (n=100)")
    thread3.start()

    #waits for thread to finish before starting fourth
    thread3.join()

    print("\nThread 4, Job 4: Birthday Paradox Testing with N tests (n=50)")
    thread4.start()

    #waits for thread to finish before ending
    thread4.join()

#Starts the program
if __name__ == '__main__':
    main()

"""
Testing Output:
Thread 1, Job 1: Hailstone Sequence of every number up to N starting at START (n=20,start=5)
Hailstone sequence of length 1 starting at 5:  [5]
Hailstone sequence of length 2 starting at 5:  [5, 16]
Hailstone sequence of length 3 starting at 5:  [5, 16, 8]
Hailstone sequence of length 4 starting at 5:  [5, 16, 8, 4]
Hailstone sequence of length 5 starting at 5:  [5, 16, 8, 4, 2]
Hailstone sequence of length 6 starting at 5:  [5, 16, 8, 4, 2, 1]
Hailstone sequence of length 7 starting at 5:  [5, 16, 8, 4, 2, 1, 4]
Hailstone sequence of length 8 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2]
Hailstone sequence of length 9 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1]
Hailstone sequence of length 10 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4]
Hailstone sequence of length 11 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2]
Hailstone sequence of length 12 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1]
Hailstone sequence of length 13 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4]
Hailstone sequence of length 14 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2]
Hailstone sequence of length 15 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1]
Hailstone sequence of length 16 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4]
Hailstone sequence of length 17 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2]
Hailstone sequence of length 18 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1]
Hailstone sequence of length 19 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4]
Hailstone sequence of length 20 starting at 5:  [5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2]

Thread 2, Job 2: Squared of every value between zero and N (n=10)
0^2 = 0
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
5^2 = 25
6^2 = 36
7^2 = 49
8^2 = 64
9^2 = 81

Thread 3, Job 3: Prime numbers between 0 and N (n=100)
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# of Primes between 0 and 100: 26

Thread 4, Job 4: Birthday Paradox Testing with N tests (n=50)
Average of 50 Tests: 23.7
[Finished in 40ms]
"""