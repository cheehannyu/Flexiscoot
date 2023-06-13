import csv
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Error 1: filename not given")

    # Assume csv file given is in the format of a list of dictionaries
    # flights is a list of flights, each being a dictionary containing flight info
    flights = []
    filename = sys.argv[1]
    with open(filename) as file:
        csv_reader = csv.Dictreader(file, newline=',')
        for item in csv_reader:
            flights.append(item)

    #To be defined with helper function
    namechange()

    #To be defined with helper function
    flightchange()


def namechange(cost):
    #TODO


def flightchange(costfrom, costto):
    #TODO



if __name__ == "__main__":
    main()
