import csv
import sys

def main():

    if sys.argv[2] != 'namechange' or sys.argv[2] != 'flightchange':
        sys.exit("Error 1: Function not specified")

    # Assume csv file given is in the format of a list of dictionaries
    # flights is a list of flights, each being a dictionary containing flight info
    flights = []
    filename = sys.argv[1]
    with open(filename) as file:
        csv_reader = csv.DictReader(file)
        for item in csv_reader:
            flights.append(item)

    if sys.argv[2] == 'namechange':
        namechange()
    elif sys.argv[2] == 'flightchange':
        flightchange()


def namechange(cost):
    #TODO


def flightchange(costfrom, costto):
    #TODO



if __name__ == "__main__":
    main()
