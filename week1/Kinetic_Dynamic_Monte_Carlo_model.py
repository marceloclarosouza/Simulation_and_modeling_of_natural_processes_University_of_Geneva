import random

k1 = 0.2
k2 = 0.2
deltaT = 2
numa = 4
numb = 3
N = numa + numb

randomNumberList = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]

for i in range(8):
    rand = random.choice(randomNumberList)
    
    if rand < (numa/N):
        rand = random.choice(randomNumberList)
        if rand < (k1*deltaT):
            numa-=1
            numb+=1
        
        
    else:
        rand = random.choice(randomNumberList)
        if rand < (k2*deltaT):
            numa+=1
            numb-=1
            
                
print("num a = {} , num b = {}". format(numa, numb))