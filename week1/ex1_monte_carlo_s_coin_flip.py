#A Monte-Carlo computer simulation
#get 3 heads in 4 flips
from random import randint

success = 0
attempts = 100000

for i in range(attempts):
    if randint(0,1)+randint(0,1)+randint(0,1)+randint(0,1)==3:
        success+=1

print("Atempts = {}".format(attempts))
print("Heads = {}".format(success))