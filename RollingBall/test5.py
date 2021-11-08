from genome import genome 
from connection import connection
import math
ply = genome()
from history import connectionhistory
l = connectionhistory()
ply.initalizeNetwork()
ply.mutateConnection(l)
ply.mutateConnection(l)
ply.mutateConnection(l)

input = {}
input["1"] = 5
input["2"] = 1
input["3"] = 4
for i in range(0,5):
    ply.makeReady()
    output = ply.useNetwork(input)[0]
    print(output)
