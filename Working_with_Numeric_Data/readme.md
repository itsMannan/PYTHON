Here’s a beginner-friendly README.md file for your second Python practice (Numbers and Operators):

⸻

🔢 Python Numbers & Operators – README

This file contains beginner-level Python code that teaches how to work with numbers, arithmetic operators, and comparison operators.
Each example explains basic math operations and how Python handles numeric data.

⸻

🧮 1. Checking Data Types

num = 3
print(type(num))

num = 3.4
print(type(num))

➡️ type() shows what kind of data a variable holds:
	•	3 → <class 'int'> (integer)
	•	3.4 → <class 'float'> (decimal number)

⸻

➕ 2. Arithmetic Operators

Python supports the following arithmetic operations:

Operator	     Meaning	   Example	    Result
    +	        Addition	    3 + 2	      5
    -	        Subtraction	    3 - 2	      1
    *	        Multiplication	3 * 2	      6
    /	        Division	    3 / 2	      1.5
    //	        Floor Division	3 // 2	      1 (removes decimal)
    **	        Exponent	    3 ** 2	      9 (3²)
    %	        Modulus	        3 % 2	      1 (remainder)

Example:

print(3 + 2)
print(3 - 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)


⸻

🧠 3. Modulus Operator Examples

print(2 % 2)  # 0 (even number)
print(3 % 2)  # 1 (odd number)
print(4 % 2)  # 0
print(5 % 2)  # 1

➡️ % is often used to check if a number is even or odd.

⸻

🧩 4. Order of Operations (BODMAS)

print(3 * 2 + 1)   # 7
print(3 * (2 + 1)) # 9

➡️ Python follows BODMAS rule (Brackets, Orders, Division, Multiplication, Addition, Subtraction).

⸻

🔁 5. Updating Variable Values

num = 1
num *= 10  # num = num * 10
print(num)

num = 1
num += 1   # num = num + 1
print(num)

➡️ Shortcuts like +=, -=, *=, /= help update variables easily.

⸻

🧾 6. Useful Math Functions

print(abs(-3))       # Absolute value → 3
print(round(3.75))   # Rounds to nearest whole → 4
print(round(3.75, 1))# Rounds to 1 decimal → 3.8

Function	         Purpose	                      Example	        Output
  abs(x)	        Gives positive value	          abs(-7)	          7
  round(x)	        Rounds to nearest integer	    round(3.2)	          3
  round(x, n)	    Rounds to n decimal places	    round(3.756, 2)	      3.76


⸻

⚖️ 7. Comparison Operators

Operator	    Meaning	            Example	    Result
  ==	        Equal to	        3 == 2	    False
  !=	        Not equal to	    3 != 2	    True
   >	        Greater than	    3 > 2	    True
   <	        Less than	        3 < 2	    False
  >=	        Greater or equal	3 >= 2	    True
  <=	        Less or equal	    3 <= 2	    False

Example:

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)


⸻

🔤 8. Type Casting (Converting Data Types)

Sometimes numbers are stored as strings (text). You can convert them to integers for math.

numb_1 = '100'
numb_2 = '200'

print(numb_1 + numb_2)             # 100200 (string joining)
print(int(numb_1) + int(numb_2))   # 300 (numeric addition)

➡️ Use int(), float(), or str() for type conversion.

⸻

🧠 Summary Table

Concept	            Function / Operator	                Example	                 Output
Data_type_check	           type()	                    type(3)	              <class 'int'>
Addition	                  +                     	3 + 2	                    5
Subtraction	                  -                     	3 - 2	                    1
Multiplication	              *	                        3 * 2                   	6
Division	                  /	                        3 / 2                      1.5
Floor division	             //	                        3 // 2	                    1
Exponent	                 **	                        3 ** 2	                    9
Modulus	                      %	                        3 % 2	                    1
Absolute_value	            abs()	                    abs(-5)	                    5
Rounding	                round()	                    round(3.75, 1)	           3.8
Comparison	            ==,!=,>,<,>=,<=	                3 > 2	                   True
Type conversion	        int(),str(),float()	            int('100')	               100


⸻

🎯 Purpose of This File

This code helps you:
	•	Understand numeric data types (int, float)
	•	Learn arithmetic and comparison operators
	•	Practice mathematical expressions and operator shortcuts
	•	Explore type conversion between numbers and strings

