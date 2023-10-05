#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # get the defined module names
    defined_name = dir(hidden_4)
    # filter the names
    nameFilter = [name for name in defined_name if not name.startswith('__')]
    nameFilter.sort()

    for name in nameFilter:
        print(name)
