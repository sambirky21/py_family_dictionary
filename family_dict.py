my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

# we need to loop over keys and values so we will use the items method.

for fam_member, details in my_family.items():
    print(f'{details["name"]} is my {fam_member} and is {str(details["age"])} years old.')