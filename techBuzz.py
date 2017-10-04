#! /usr/bin/env python
from __future__ import division
import random
import pickle


# main


# Large word list
adj = ["interoperable", "agile", "mobile", "cloud-based", "scalable", "integrated", "lightweight", "support", "reinforced", "extensible", "maximal", "data-oriented", "distributed", "anomaly-based", "enterprise", "cross-platform", "cross-functional", "deep-learning", "large-scope", "adaptive", "cluster"]
anchor = ["artificial intelligence", "data analytics", "services", "cloud", "virtual reality", "internet of things", "data science", "microservices", "solutions", "development", "blockchain", "machine-learning", "reinforcement learning", "platform"]

# Small test list
#adj = ["interoperable", "agile", "cloud-based", "scalable", "integrated", "lightweight", "reinforced", "extensible", "data-oriented", "anomaly-based", "cross-platform", "adaptive"]
#anchor = ["services", "virtual reality", "internet of things", "microservices", "solutions", "blockchain"]

# Grabbing data from file
dataFile = open(r'data.txt', 'rb')
matrix = pickle.load(dataFile)
dataFile.close()

# Grabbing configs from file
configFile = open(r'config.txt', 'rb')
configs = pickle.load(configFile)
baseReq = configs[0]
avgHits = configs[1]
configFile.close()

# for testing
secure_random = random.SystemRandom()
userIn = 100

adjs = random.sample(range(0, len(adj)+1), 2) 

adj1 = adjs[0]
adj2 = adjs[1]
anchor1 = random.sample(range(0, len(anchor)+1), 1)[0]

print("PRESENTING: " + adj[adj1] + " " + adj[adj2] + " " + anchor[anchor1])
userIn = random.sample(range(1, 6), 1)[0] 

#while userIn != 0: 
for i in range(50000):
    # "ML algorithm" 
    userIn = int(userIn)/5.0
    # print userIn
    userIn = random.sample(range(1, 6), 1)[0] 
    matrix[adj1][adj2][anchor1][0] = (matrix[adj1][adj2][anchor1][0]*matrix[adj1][adj2][anchor1][1] + userIn)/(matrix[adj1][adj2][anchor1][1] + 1)
    matrix[adj1][adj2][anchor1][1] = matrix[adj1][adj2][anchor1][1] + 1
    
    # makes random buzzword
    adjs = random.sample(range(0, len(adj)), 2) 
    adj1 = adjs[0]
    adj2 = adjs[1]
    anchor1 = random.sample(range(0, len(anchor)), 1)[0]
    
    # buzzword too historically bad or overrepresented, so reroll until it's good
    #while matrix[adj1][adj2][anchor1][2] < baseReq or matrix[adj1][adj2][anchor1][2] > avgHits + 2:
    adjs = random.sample(range(0, len(adj)), 2) 
    adj1 = adjs[0]
    adj2 = adjs[1]
    anchor1 = random.sample(range(0, len(anchor)), 1)[0]
        
    print("PRESENTING: " + adj[adj1] + " " + adj[adj2] + " " + anchor[anchor1])
    userIn = random.sample(range(1, 6), 1)[0] 
    
afile = open(r'data.txt', 'wb')
pickle.dump(matrix, afile)
afile.close()