#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip


inp = input().split(".")
L = len(inp)
if L > 1:
    var2 = inp[-1] 
    var1 = inp[0]
    print(var1)
    print(var2)
    print(var1+"/"+var2)
else:
    var3 = inp[0]+"/octet-stream"
    print(var3)