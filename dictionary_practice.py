

ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

name = str(input("Name: "))
age = int(input("Age: "))

ages_dict[name] = age

for name, age in ages_dict.items():
    print("{:<6} - {:>4}".format(name, age))
