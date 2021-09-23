def draw_road():
    print("|    ||    |")
    print("|    ||    |")
    print("|    ||    |")
    print("|====||====|")
    print("|    ||    |")
    print("|    ||    |")

    for i in range(len(range(5))):
        spaces = " " * i

        print((spaces + "\    \\\    \ "))

    print((spaces+("|    ||    |")))
    print((spaces+("|    ||    |")))
    print((spaces+("|====||====|")))
    print((spaces+("|    ||    |")))
    print((spaces+("|    ||    |")))

    for j in range(len(range(5))):
        spaces_ = " " * (i - j)

        print(((spaces_) + "/    //    / "))

    print("road not found")
    return

draw_road()