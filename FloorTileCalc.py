tSize = int(input("Please enter the size of the tile as an integer: "))
tSpan = int(input("Please enter the length of the span as an integer: "))
tTiles = ((tSpan) //(tSize))
spanToUse = tSpan - tSize
numPairs = spanToUse//(2*(tSize))
borderSize = (spanToUse%2*(tSize))/2
bTile = numPairs + 1
wTile = numPairs
gSize = borderSize
print("Number of black tiles neded: " + str(bTile))
print("Number of white tiles neded: " + str(wTile))
print("Total number of tiles needed: " + str(tTiles))
print("Gap Length: " + str(gSize))
