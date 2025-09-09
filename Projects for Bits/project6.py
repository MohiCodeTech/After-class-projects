def powerset(stringset, stringsetsize):
    power_set_size = 2**stringsetsize
    outer = 0
    inner = 0
    for outer in range(0 , power_set_size):
        subset = ""
        for inner in range(0, stringsetsize):
            if (outer & (1 << inner)) > 0:
                subset +=  str(stringset[inner]) + ""

        print("{", subset, "}")

stringset = input("Enter a name to see all its substrings: ")
stringsetsize = int(input("Enter the amout of letter it has: "))
set = ["" + stringset]
powerset(set, stringsetsize)