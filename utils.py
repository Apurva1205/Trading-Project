import csv
from datetime import datetime
from decimal import Decimal

from .models import Candle

def process_csv(file):
    reader = csv.reader(file)
    header = next(reader)  # Read the header row

    candles = []
    for row in reader:
        # Convert the row values to the appropriate types
        date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        open_price = Decimal(row[1])
        high = Decimal(row[2])
        low = Decimal(row[3])
        close = Decimal(row[4])

        # Create a Candle instance and add it to the list of candles
        candles.append(Candle(date=date, open=open_price, high=high, low=low, close=close))

    return candles

def convert_candles(candles, timeframe):
    converted_candles = []

    for i in range(0, len(candles), timeframe):
        chunk = candles[i:i+timeframe]

        date = chunk[0].date
        open_price = chunk[0].open
        high = max(c.high for c in chunk)
        low = min(c.low for c in chunk)
        close = chunk[-1].close

        converted_candles.append(Candle(date=date, open=open_price, high=high, low=low, close=close))

    return converted_candles
