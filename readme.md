Exercise 01: Conditionals, variables
=======

Tutorials & Resources:
-------
Take a look at these online resources before you attempt this exercise. If you get stuck, check the work you've already completed. Do these before starting the exercise below.

    * http://learnpythonthehardway.org/book/ex6.html
    * http://learnpythonthehardway.org/book/ex7.html
    * http://learnpythonthehardway.org/book/ex11.html
    * http://learnpythonthehardway.org/book/ex29.html
    * http://learnpythonthehardway.org/book/ex30.html
    * http://learnpythonthehardway.org/book/ex31.html
    * http://learnpythonthehardway.org/book/ex33.html

Concepts required:
    * while loops
    * 'break' statement
    * conditionals
    * user input
    * formatting strings
    * the int() function

Introduction
-------
Programs tend to be structured around a 'main loop', which repeatedly executes the primary task of the program. It is important to understand that the primary task is not necessarily the primary function of the program. As an example, the primary function (or at least, the primary usage) of the program 'cat' is to print the contents of a file to the screen. However, the primary task in accomplishing that is printing individual lines of the file in sequence. In pseudocode, it might look like this:

    f = open_file(filename)
    for each line 'l' in file 'f':
        print l

Consider a calculator program, that lets you enter arithmetic expressions, then evaluates and prints the output until you tell it to quit. It might look like this:

    while True:
        expression = read_input()
        value = evaluate_expression(expression)
        print value

In general, a program is structured like this:

    do_setup()
    while exit_condition_not_reached:
        input = consume_input()
        output = evaluate_input(input)
        print output

In the case of 'cat', input comes from the file specified on the command line. In the calculator, input comes from the keyboard.


Description
-------
Write a program named guess.py that plays the 'number guessing game'. The computer will choose a random number between 1 and 100, and ask the user to guess the number, giving them a hint if it's high or low. A sample game looks like this:

Meringue:guessing chriszf$ python ./guess.py 
Howdy, what's your name?
(type in your name) Christian
Christian, I'm thinking of a number between 1 and 100. Try to guess my number.
Your guess? 50
Your guess is too low, try again.
Your guess? 80
Your guess is too high, try again.
Your guess? 60
Your guess is too low, try again.
Your guess? 70
Your guess is too high, try again.
Your guess? 63
Your guess is too low, try again.
Your guess? 64
Your guess is too low, try again.
Your guess? 67
Your guess is too low, try again.
Your guess? 69
Your guess is too high, try again.
Your guess? 68
Well done, Christian! You found my number in 9 tries!


A rough pseudocode outline of the program will look like this:

    greet player
    get player name
    choose random number between 1 and 100
    while True:
        get guess
        if guess is incorrect:
            give hint
        else:
            congratulate player
            
