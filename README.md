# fishscaler
Python utility for bulk capture of pricing data from mtggoldfish.com using Requests and Beautifulsoup. Python 3 is (maybe) required, but might run on 2.7 - I haven't tested it. 

### Installation
```
git clone https://github.com/blitzcrg/fishscaler
cd fishscaler
pip3 install -r requirements.txt
```

### Usage
`python3 fishscaler.py /path/to/input/file /path/to/output/file`

Accepts two positional arguments - an input file and an output file. The input file MUST be a CSV formatted like:

```
Name,Set,Quantity`
Tropical Island,Revised Edition,2
```

The output file will be a CSV with the same format plus two additional columns: Price, and Total. 

```
Name,Set,Quantity,Price,Total
Tropical Island,Revised Edition,2,180.32,360.64
```

Typos, incorrect set names, etc will cause unhandled errors. I'm not really sure how to preempt that without performing searches against a local database of set or card names, which is a bit more heavy lifting than is probably necessary. Just make sure your input file is formatted correctly.

### To Do
- Error handling (did I mention that it's REALLY IMPORTANT that your input file is formatted properly and error-free?).
- Expand to check APIs for popular sites (echomtg, tcgplayer, maybe others) or scrape other online data sources.
- Add a toggle to track prices for MTGO instead of paper
