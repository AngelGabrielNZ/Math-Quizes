
while True:

    want_instructions = input("do you want to see the instructions? ").lower()

    # check if user said yes/no
    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("you said no")
        break
    else:
        print("Please enter Yes / no")

print("we are done")