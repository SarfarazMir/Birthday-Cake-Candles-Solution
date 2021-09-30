def birthdayCakeCandles(candles):
    
    maxCandle = candles[0]
    counter = 0
    
    for i in range(len(candles)-1):
        if (candles[i+1] > maxCandle):
            maxCandle = candles[i+1]
            
    for j in range(len(candles)):
        if (maxCandle == candles[j]):
            counter += 1
            
    return counter
    
print(birthdayCakeCandles([3, 2, 1, 3]))
