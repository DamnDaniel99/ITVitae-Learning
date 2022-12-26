"""

Write a slightly more complicated greeter script. Use proper variable names.
1. When the script runs, the script should first print:
Hello! What's your name?
2. The user should now be able to enter their name, use the input() function and a variable.
3. Next, the script should print (where <NAME> is once again replaced with the user input from the previous step):
Hello <NAME>! What's your age?
4. The user should now be able to enter their age, as before, use the input() function and a variable.
5. Lastly, the script should now generate the following output (by now, you should know what to do with <NAME>
and <AGE> ):
So, your name <NAME> and you are <AGE> years old!


"""

name = input("Hello! What is your name? ")
age = input(f"Hello {name}! What is your age? ")

print(f"So, your name is {name} and you are {age} years old!")