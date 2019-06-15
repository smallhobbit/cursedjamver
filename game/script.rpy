
# Variables stored here

# day check

define daycheck = 0

# action/time check

define timecheck = 3  # start with 3, can change it later

# event days

define event = [3,6,9]

# progression variables here



# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Lillian")

# the ROs

define harvey = Character("Harvey")

define edwin = Character("Edwin")

define flecher = Character("Flecher")

define lucien = Character("Lucien")

# the other ladies

define blanche = Character("Blanche")

define isablelle = Character("Isabelle")

define margert = Character("Margert")

define rosalind = Character("Rosalind")

define polly = Character("Polly")

# The game starts here.

label start:

    $ save_name = "Prologue" # I don't know if we want to start with this

    #  insert prologue/intro here?

    label nextday:

    # add new day

    $ daycheck += 1

    if daycheck in event:
        $ lbl="event"+str(daycheck)
        call expression lbl
    else:

        # refresh actions for next day

        if timecheck == 0:

            $ timecheck = 3

        label dayactions:

            if timecheck == 0:

                # add event for day end here

                jump nextday

            $ save_name = "Day [daycheck]; with [timecheck] options left"

            "It's day [daycheck] with [timecheck] actions left" # create images for this?

            $ timecheck -= 1
            # these choices can be changed; just a loose example (can also check actions for day/night system or days for character schedule changes)
            menu:

                "Spend time in communal area":

                    # Add script here

                    "Spent some time with people in the communal area"

                "Stay in the ladies dorm":

                    # Add script here

                    "Stayed in the ladies dorm"

                "Sneak out":

                    # Probably won't be using; just wanted to add more options

                    "Snuck out"

        jump dayactions

    label event3:

        # curse progression/group vist possibly?

        jump dayaction # not sure if these should be treated as their own days

    label event6:

        # curse progression/group vist possibly?

        jump dayaction # not sure if these should be treated as their own days

    label event9:

        # curse progression/end game?

        return


    return
