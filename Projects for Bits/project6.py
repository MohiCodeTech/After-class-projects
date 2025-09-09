def powerset(stringset, stringsetsize):
    power_set_size = 2**stringsetsize
    for outer in range(power_set_size):
        subset = ""
        for inner in range(stringsetsize):
            if (outer & (1 << inner)) > 0:
                subset +=  str(stringset[inner]) + " "

        print("{", subset, "}")

stringset = input("Enter a name to see all its substrings: ")
chars = list(stringset)
stringsetsize = len(stringset)
powerset(stringset, stringsetsize)