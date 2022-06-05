# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
## General
 * Why Python programming is awesome
 * What are lists and how to use them
 * What are the differences and similarities between strings and lists
 * What are the most common methods of lists and how to use them
 * How to use lists as stacks and queues
 * What are list comprehensions and how to use them
 * What are tuples and how to use them
 * When to use tuples versus lists
 * What is a sequence
 * What is tuple packing
 * What is sequence unpacking
 * What is the del statement and how to use it

## Copyright - Plagiarism
 * You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
 * You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
 * You are not allowed to publish any content of this project.
 * Any form of plagiarism is strictly forbidden and will result in removal from the program.
#Requirements

## Python Scripts
 * Allowed editors: vi, vim, emacs
 * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
 * All your files should end with a new line
 * The first line of all your files should be exactly #!/usr/bin/python3
 * A README.md file, at the root of the folder of the project, is mandatory
 * Your code should use the pycodestyle (version 2.8.*)
 * All your files must be executable
 * The length of your files will be tested using wc

## C
 * Allowed editors: vi, vim, emacs
 * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
 * All your files should end with a new line
 * Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
 * You are not allowed to use global variables
 * No more than 5 functions per file
 * In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
 * The prototypes of all your functions should be included in your header file called lists.h
 * Don’t forget to push your header file
 * All your header files should be include guarded

## Tasks 

* **0. Print a list of integers**
  * [0-print_list_integer.py](./0-print_list_integer.py): Python function that prints all
  integers of a list, one per line.
  * Without importing modules or casting integers into strings.

* **1. Secure access to an element in a list**
  * [1-element_at.py](./1-element_at.py): Python function that retrieves an element
  from a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns `None`.
  * Without import modules or using `try/except`.

* **2. Replace element**
  * [2-replace_in_list.py](./2-replace_in_list.py): Python function that replaces an element
  of a list at a specific position.
  * If `idx` is negative or out of range (greater than the number of elements
  in `my_list`), the function returns the original list.
  * Without importing modules or using `try/except`.

* **3. Print a list of integers... in reverse!**
  * [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py): Python
  function that prints all integers of a list, one per line, in reverse order.
  * Without importing modules or casting integers into strings.

* **4. Replace in a copy**
  * [4-new_in_list.py](./4-new_in_list.py): Python function that replaces an element of a
  list at a specific position without modifying the original list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns the original list.
  * Without importing modules or using `try/except`.

* **5. Can you C me now?**
  * [5-no_c.py](./5-no_c.py): Python function that removes all characters `c`
  and `C` from a string and returns the string.
  * Without importing modules or using `str.replace()`.

* **6. Lists of lists = Matrix**
  * [6-print_matrix_integer.py](./6-print_matrix_integer.py): Python function that prints
  a matrix of integers, one row per line.
  * Without casting integers into strings.

* **7. Tuples addition**
  * [7-add_tuple.py](./7-add_tuple.py): Python function that adds two tuples.
  * Returns a tuple with two integers:
    * The first element is the addition of the first element of each argument.
    * The second element is the addition of the second element of each argument.
  * If a tuple is smaller than 2, the value `0` is used for the missing integer.
  * If a tuple is larger than 2, only the first two integers are used.
  * Without importing modules.

* **8. More returns!**
  * [8-multiple_returns.py](./8-multiple_returns.py): Python function that returns a
  tuple with the length of a string and its first character.
  * If the string is empty, the first character should equal `None`.
  * Without importing modules.

* **9. Find the max**
  * [9-max_integer.py](./9-max_integer.py): Python function that finds the biggest integer
  of a list.
  * If the list is empty, the function returns `None`.
  * Without importing modules or using the builtin `max()`.

* **10. Only by 2**
  * [10-divisible_by_2.py](./10-divisible_by_2.py): Python function that finds all multiples
  of 2 in a list.  * Returns a new list of the same size. Each element of the new
  list contains either `True` or `False` corresponding to whether the integer at
  the same position in the original list is a multiple of 2.
  * Without importing modules.

* **11. Delete at**
  * [11-delete_at.py](./11-delete_at.py): Python function that deletes an item at
  a specific position in a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns the original list.
  * Without imporitng modules or using `pop()`.

* **12. Switch**
  * [12-switch.py](./12-switch.py): Python program that switches the values of
  variable `a` and `b`.
  * Completion of [this source code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py).

* **13. Linked list palindrome**
  * [13-is_palindrome.c](./13-is_palindrome.c): C function that checks if a
  singly-linked list is a palindrome.
  * If the function is not a palindrome - returns `0`.
  * If the function is a palindrome - returns `1`.
  * An empty list is considered a palindrome.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for
    testing [13-is_palindrome.c](./13-is_palindrome.c) (provided by Holberton School).
    * [lists.h](./lists.h): Header file containing definitions and prototypes for all types
    and functions used in [linked_lists.c](./linked_lists.c) and
    [13-insert_number.c](./13-insert_number.c).

* **14. CPython #0: Python lists**
  * [100-print_python_list_info.c](./100-print_python_list_info.c): C function that
  prints basic information about Python lists.
# Resources
Read or watch:

 * 3.1.3. Lists
 * Data structures (until 5.3. Tuples and Sequences included)
 * Learn to Program 6 : Lists
# Author
Asrat Asmelash <https://github.com/Assu01>
