# This is an introductory assignment to help you get on your feet with variables and print statements.

# This variable's data type is a string
full_name = "Shunsuke Honjo"
# These are both integer variables
year_of_graduation = 2026
years_at_nmh = 3
# This is an example of a list with 3 string values
hobbies = ["Coding", "Reading", "Gaming"]
# Enter your
favorite_foods = ["Sushi", "Fried Rice", "Pasta"]

print("I have been at NMH for " + str(years_at_nmh) + "years") # need to "cast" my integer so that it can concatenate with the strings

# F String print statements are very versatile. Feel free to use regular print statements as well.
print(f"Hello, my name is {full_name}.")
print(f"I am in the class of {year_of_graduation} and I have been at NMH for {years_at_nmh} years.")
print(f" Some of my hobbies are {', '.join(hobbies)}. My favorite foods are {', '.join(favorite_foods)}")