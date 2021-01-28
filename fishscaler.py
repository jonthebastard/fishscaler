#!/usr/bin/python3

import requests
import bs4
import csv
import argparse
import re
from itertools import islice
"""
Load a CSV of Magic cards formatted like
Name,Set,Quantity
Tropical Island,Revised,2

And go pull the prices for those cards from online stores. Output another CSV.

Name,Set,Quantity,Price,Total
Tropical Island,Revised,2,200,400
"""

def clean_name(name):
    name = re.sub("[',:)]", "", name)
    name = re.sub("[ .]", "+", name).replace("++","+")
    if name.count("(") == 1 :
        name = name.replace("(", "-")
    elif name.count("(") > 1 :
        name = name.replace("(", "", (name.count("(")-1)).replace("(", "+-")
    return name.replace("+-","-")

def load_csv(path):
    """
    Read the contents of a CSV file.

    Input: path - string
    Output: inventory - list
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        inventory = list(reader)
    return inventory


def getprice_mtggoldfish(cardname, setname):
    """
    For a given card and set, get the price from mtggoldfish.

    Return "Not Found" if anything other than a decimal value comes back.

    Input: cardname - string
           setname - string

    Output: price - float
            error - string
    """
    uri = "http://www.mtggoldfish.com/price/{}/{}#paper"

    cardname = clean_name(cardname)

    setname = clean_name(setname)

    print(cardname, setname)

    page = requests.get(uri.format(setname, cardname))

    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    try:
        price = soup.find(class_='price-box paper').contents[3].text
    except:
        price = 0
        return price
    return price[2:].replace(",","")


def build_collection(inventory, outpath):
    """
    Build go get price data and format it.

    Input: inventory - list of lists
    Output: inventory - a (different) list of lists
    """
    inventory[0].append('Price')
    inventory[0].append('Total')
    with open(outpath, 'w') as outfile:
        writer = csv.writer(outfile)
        for line in islice(inventory, 1, None):
            price = getprice_mtggoldfish(line[0], line[1])
            line.append(str(price))
            line.append(str("{:.2f}".format(float(price) * float(line[2]))))
            writer.writerow(line)
    """return inventory"""


def msg(name=None):
    """Define a slightly more verbose help message."""
    message = '''fishscaler.py
                 Pass a csv file formatted like this:

                 Name,Set,Quantity
                 Tropical Island,Revised,2

                 And get back a csv formatted like this:

                 Name,Set,Quantity,Price,Total
                 Tropical Island,Revised,2,200,400
                '''
    return message


def initargparser():
    """Initialize and return an argument parser."""
    parser = argparse.ArgumentParser(usage=msg())
    parser.add_argument("infile", help="Path to formatted csv.")
    parser.add_argument("outfile", help="Output file path.")

    return parser


def main():
    """Parse arguments and perform price checks."""
    parser = initargparser()
    args = parser.parse_args()
    build_collection(load_csv(args.infile), args.outfile)


if __name__ == '__main__':
    main()
