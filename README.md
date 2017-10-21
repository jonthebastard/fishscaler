# fishscaler
Python utility for bulk capture of pricing data from mtggoldfish.com. Python 3 is (maybe) required, but might run on 2.7 - I haven't tested it. 

## Installation
`git clone https://github.com/blitzcrg/fishscaler`
`cd fishscaler`
`pip3 install -r requirements.txt`

## Usage
Accepts two positional arguments - an input file and an output file. The input file must be a CSV formatted like

```
Name,Set,Quantity`
Tropical Island,Revised Edition,2
```

The output file will be a CSV with the same format plus two additional columns: Price, and Total. 

## To Do
- Error handling (for now it's REALLY IMPORTANT that your input file is formatted properly)
- Expand to check APIs for popular sites (echomtg, tcgplayer, maybe others) or scrape other online datasources
