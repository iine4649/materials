"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["Sushi", "Fried Rice", "Pasta", "Fried Chicken", "Hamburger"]

# Access items by index (first = 0):
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?



# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()

foods.append("Salad")
# TODO: Insert a food at the beginning with .insert()

foods.insert(0, "Banana")
# TODO: Remove one food from the list with .remove()

foods.remove("Salad")
# TODO: How many foods are in the list? Use len()

print(len(foods))
# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.


# Bug Exploration:
# Change your loop to go past the length of the list:
for i in range(len(foods)):
    print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?
# Because the index is out of range of the list.


# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Kevin",
    "age": 30,
    "student": False
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.

me = {
    "name": "Shunsuke",
    "age": 18,
    "student": True
    }
# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")

# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?
# It is a KeyError. You can check if a key exists before using it by using the .get() method.


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.

me["favorite_color"] = "Blue"
# TODO: Change the value of an existing key.

me["age"] = 19
# TODO: Remove one key-value pair.

me.pop("student")
# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?
# It is a KeyError.


# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()

for key, value in me.items():
    print(f"{key}: {value}")
# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?
# It only prints the keys because the dictionary is not iterable. 


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.

friends = [
    {
        "name": "Ethan",
        "favorite_food": "Bananas"
    },
    {
        "name": "Henry",
        "favorite_food": "Fried Rice"
    },
]
# TODO: Print the favorite food of the second friend.

print(friends[1]["favorite_food"])
# TODO: Loop through and print "<name> likes <food>" for each friend.

for friend in friends:
    print(f"{friend['name']} likes {friend['favorite_food']}")        
# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?
# You can check if a key exists before using it by using the .get() method.


# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# It can take different type of variables, while a dictionary can only take one type of variable.
# 2. When would you want to use a dictionary instead of a list?
# When you want to store a collection of items with a specific key.
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# When we have a collection of items and we want to store a specific key for each item.
# 4. What types of mistakes gave you the most errors today?
# Forgetting to use the .get() method when accessing a dictionary.
# 5. How might noticing errors actually help you learn?
# It helps us to understand the code better and to fix the code.