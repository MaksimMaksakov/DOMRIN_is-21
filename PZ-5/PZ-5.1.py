#Составить программу, в которой функцию построит изображение, в
# котором в первой строке 1 звездочка,
# во второй - 2, в третьей -3, ..., в строке с номером т - т звездочек.
import random
m = random.randrange(1, 10)
for i in range(m):
    print("*" * i)