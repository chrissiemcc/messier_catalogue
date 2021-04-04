import csv


def messier_search(messier):
    f = open('messier_catalogue.csv')
    csv_f = csv.reader(f)

    i = 0

    for row in csv_f:
        # print(i, messier)
        if i == 0:
            mNumberHeading = row[0]
            objectTypeHeading = row[8]
            nameHeading = row[9]
            magnitudeHeading = row[4]
            sizeHeading = row[5]

        if i == messier:
            if row[9] == "":
                row[9] = "No name"

            print('\n', mNumberHeading, " - ", row[0], '\n', objectTypeHeading, " - ", row[8], '\n',
                  nameHeading, " - ", row[9], '\n', magnitudeHeading, " - ", row[4], '\n',
                  sizeHeading, " - ", row[5], '\n', sep='')
            break
        i += 1


while True:  # keep the program running
    while True:  # loop until the user enters a valid integer
        try:
            number = int(input("Messier object to fetch - insert number (1 - 110): "))
            if 111 > number > 0:
                messier_search(number)  # inputted integer from 1 - 110, passed to messier_search function as parameter
                break
            else:
                print("You must enter a number from 1 - 110!")
        except ValueError:  # if user does not input a valid integer
            print("That's not a valid number!")
