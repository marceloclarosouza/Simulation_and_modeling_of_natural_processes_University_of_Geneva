"""
Let say that the Kinetic / Dynamic Monte-Carlo model parameters 
are k1=k2=0.2k_1=k_2=0.2k1​=k2​=0.2 and Δt=2\Delta t=2Δt=2. At time t=0t=0t=0, 
there are 4 type-A particles and 3 type-B particles. 

How many type-B particles there are after one time step at t=2t=2t=2?

Note that in this algorithm, N is the total number of particles.
It is very important to note that step (4) required N iterations 
of steps (2) and (3) before incrementing the time by Δt\Delta tΔt. 
Also, both step (2) and step (3) require one random number. 
To solve this problem, every time you need a random number pick the
 number in the following list. Start by taking the first number and then
 take the second, etc. Never reuse twice a random number. 
 You should have enough random number to answer the question.
"""

import random

k1 = 0.2
k2 = 0.2
deltaT = 2
numa = 4
numb = 3
N = numa + numb

randomNumberList = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]

for i in range(len(randomNumberList)):
    rand = float(random.shuffle(randomNumberList))
    
    if rand < (numa/N):
        rand = float(random.shuffle(randomNumberList))
        if rand < (k1*deltaT):
            numa-=1
            numb+=1
        
        
    else:
        rand = float(random.shuffle(randomNumberList))
        if rand < (k2*deltaT):
            numa+=1
            numb-=1
            
                
print("num a = {} , num b = {}". format(numa, numb))