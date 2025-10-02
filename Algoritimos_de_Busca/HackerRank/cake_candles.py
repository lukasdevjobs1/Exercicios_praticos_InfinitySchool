candles = [4,4,1,3]


def birthdayCakeCandles(candles):
    for i in range(len(candles)):
        if candles[i] == max(candles):
            return candles.count(max(candles))
        print(candles.count(max(candles)))
