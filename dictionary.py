my_dict = {}

my_dict = {1: "Apple", 2: "Ball"}

my_dict = {"Name": "John", 1: [2, 3, 4]}

my_dict = {"Name": "Jack", "Age": 26}

print(my_dict["Name"])
print(my_dict["Age"])

my_dict["Age"] = 27
print(my_dict)

my_dict["Address"] = "Downtown"
print(my_dict)

my_dict.pop("Age")
print(my_dict)

print("Address:", my_dict.get("Address"))

my_dict.clear()
print(my_dict)