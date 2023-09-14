# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.

for lyrics in range(99, -1, -1):
    if (lyrics>=1):
         print(lyrics, "bottles of beer on the wall,", lyrics, "bottles of beer.\n Take one down and pass it around," ,  lyrics-1 , "bottles of beer on the wall.")
    else:
        print("plus rien")
