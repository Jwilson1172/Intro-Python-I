import math


class Assignment:
    # just a placeholder for now
    def __init__(self):
        pass

    def one(self):
        """A function that prints hello world to the attached console or tty
        """
        # print hello world on the cli
        print("hello world")
        return

    def two(self):
        """A function that prints the product of 2^65536 to the attached
        console or tty
        """
        # print 2^65536 to the cli
        print(str(2 ** 65536))
        return

    def three(self):
        """
    Python is a strongly-typed language under the hood, which means
    that the types of values matter, especially when we're trying
    to perform operations on them.
    Note that if you try running the following code without making any
    changes, you'll get a TypeError saying you can't perform an operation
    on a string and an integer.
    """

        x = 5
        y = "7"

        # Write a print statement that combines x + y into the integer value 12
        try:
            print(int(y) + x)
        except Exception as e:
            print(
                "there was an error that occured with casting the string to an int\n",
                e,
                "going to fall back to hardcoded arithmetic\n",
                print(5 + 7),
            )

        # Write a print statement that combines x + y into the string value 57
        try:
            print(str(x) + str(y))
        except Exception as e:
            print("there was a problem with casting the int to a str\n", e)
        return

    def four(self):
        """
    Python provides a number of ways to perform printing. Research
    how to print using the printf operator, the `format` string
    method, and by using f-strings.
    """

        x = 10
        y = 2.24552
        z = "I like turtles!"

        # Using the printf operator (%), print the following feeding in the values of x,
        # y, and z:
        # x is 10, y is 2.25, z is "I like turtles!"

        # Use the 'format' string method to print the same thing
        print("{} {} {}".format(x, y, z))

        # Finally, print the same thing using an f-string
        print(f"{x} {y} {z}")
        return

    def five(self):
        """A function that does various operations on list then prints the
        result of each operation.
        """
        # For the exercise, look up the methods and functions that are available for use
        # with Python lists.

        x = [1, 2, 3]
        y = [8, 9, 10]

        # For the following, DO NOT USE AN ASSIGNMENT (=).

        # Change x so that it is [1, 2, 3, 4]
        # YOUR CODE HERE
        x.append(4)
        print(x)

        # Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
        # YOUR CODE HERE
        print(x + y)
        z = x + y

        # Change x so that it is [1, 2, 3, 4, 9, 10]
        # YOUR CODE HERE
        print([i for i in (z) if i != 8])

        # Change x so that it is [1, 2, 3, 4, 9, 99, 10]
        # YOUR CODE HERE
        z.insert(6, 99)
        print(z)

        # Print the length of list x
        # YOUR CODE HERE
        print(len(x))

        # Print all the values in x multiplied by 1000
        [print(i * 1000, end=", ") for i in x]
        return

    def six(self):
        """
        Python tuples are sort of like lists, except they're immutable and
        are usually used to hold heterogenous data, as opposed to lists
        which are typically used to hold homogenous data. Tuples use
        parens instead of square brackets.
        More specifically, tuples are faster than lists. If you're looking
        to just define a constant set of values and that set of values
        never needs to be mutated, use a tuple instead of a list.
        Additionally, your code will be safer if you opt to "write-protect"
        data that does not need to be changed. Tuples enforce immutability
        automatically.
        """

        # private methods are fround upon going to add this method to the end of the assignment def's
        def dist(a, b):
            """Compute the distance between two x,y points."""
            x0, y0 = a  # Destructuring assignment
            x1, y1 = b

            return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        a = (2, 7)  # <-- x,y coordinates stored in tuples
        b = (-14, 72)

        # Prints "Distance is 66.94"
        print("Distance is: {:.2f}".format(dist(a, b)))

        # Write a function `print_tuple` that prints all the values in a tuple
        def print_tuple(tup):
            print("the values in tuple {} are:\n".format(tup))
            for i in tup:
                print(i)

        t = (1, 2, 5, 7, 99)
        print_tuple(t)  # Prints 1 2 5 7 99, one per line

        # Declare a tuple of 1 element then print it
        u = (1,)  # What needs to be added to make this work?
        print_tuple(u)
        return

    def seven(self):
        """
        Python exposes a terse and intuitive syntax for performing
        slicing on lists and strings. This makes it easy to reference
        only a portion of a list or string.
        This Stack Overflow answer provides a brief but thorough
        overview: https://stackoverflow.com/a/509295
        Use Python's slice syntax to achieve the following:
        """

        a = [2, 4, 1, 7, 9, 6]

        # Output the second element: 4:
        print(a[1])

        # Output the second-to-last element: 9
        print(a[-2])

        # Output the last three elements in the array: [7, 9, 6]
        print(a[-3:])

        # Output the two middle elements in the array: [1, 7]
        print(a[1:4])

        # Output every element except the first one: [4, 1, 7, 9, 6]
        print(a[1:])

        # Output every element except the last one: [2, 4, 1, 7, 9]
        print(a[:-1])

        # For string s...

        s = "Hello, world!"

        # Output just the 8th-12th characters: "world"
        # cheating i know
        print(s[7:-1])
        return

    def eight(self):
        """
        List comprehensions are one cool and unique feature of Python.
        They essentially act as a terse and concise way of initializing
        and populating a list given some expression that specifies how
        the list should be populated.
        Take a look at    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        for more info regarding list comprehensions.
        """
        # Write a list comprehension to produce the array [1, 2, 3, 4, 5]
        y = [x for x in range(1, 5)]
        print(y)

        # Write a list comprehension to produce the cubes of the numbers 0-9:
        # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

        y = [x ** 3 for x in range(10)]
        print(y)

        # Write a list comprehension to produce the uppercase version of all the
        # elements in array a. Hint: "foo".upper() is "FOO".

        a = ["foo", "bar", "baz"]

        y = [x.upper() for x in a if isinstance(x, str)]
        print(y)

        # Use a list comprehension to create a list containing only the _even_ elements
        # the user entered into list x.
        a = input("Enter comma-separated numbers: ").split(",")

        # What do you need between the square brackets to make it work?
        # this one is a bit compicated so let me exsplain it, im running throgh every
        # element in the list then asking the list object what index i'm at then taking
        # mod 2 of that number and checking if it is not odd.
        y = [x for x in a if a.index(x) % 2 != 1]
        print(y)
        return

    def nine(self):
        """A function that takes a given dictionary and adds a key to that dict
        then does some things to the dict to prove an understanding of how a dict
        im python works.
        """
        waypoints = [
            {"lat": 43, "lon": -121, "name": "a place"},
            {"lat": 41, "lon": -123, "name": "another place"},
            {"lat": 43, "lon": -122, "name": "a third place"},
        ]
        # Add a new waypoint to the list
        waypoints.append({"lat": 0, "lon": 0, "name": "The Painted World Of Ariandel"})

        # Modify the dictionary with name "a place" such that its longitude
        # value is -130 and change its name to "not a real place"
        # Note: It's okay to access the dictionary using bracket notation on the
        # waypoints list.
        waypoints[0]['name'] = "not a real place"
        waypoints[0]['lon'] = -130

        # Write a loop that prints out all the field values for all the waypoints
        counter = 0
        # iter through all of the elements in the list of waypoints
        # and print a header so that the user knows which waypoint is being
        # printed
        for waypoint in waypoints:
            print(f"Waypoint #{counter},", end='')
            # inter through all of the elements in the dictionary and print
            # each key value pair
            for k, v in zip(waypoint.keys(), waypoint.items()):
                print(f"\n\t{k}{v}", end='')
            # add a number to the counter so that the print will uniquely ident
            # each element in the list
            counter += 1
        return

    def ten(self):
        return

    def eleven(self):
        return

    def twelve(self):
        return

    def thirteen(self):
        return

    def fourteen(self):
        return

    def fifteen(self):
        return
