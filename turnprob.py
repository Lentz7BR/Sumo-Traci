import random
import traci
import traci.constants as tc
from math import *
from bib import *

rede="circular/circular"
traci.start(['sumo-gui', '-n', rede+".net.xml", '-r', rede+'.rou.xml' ])

step = 0
id = 0
rid = 0
num = 0
rotasu = []
 
while True:
    if step == 50:
        rotas = traci.route.getIDList()
        for i in range (len(rotas)):
            if cont(traci.route.getEdges(rotas[i]),rotasu):
                rotasu.append(rotas[i])
    if traci.vehicle.getIDCount() < 1000 & step > 50:
        try:
            m=insert_veh(1,rotasu[(random.randint(0,len(rotasu)-1))],id+num)
            num += 1
        except:
            pass
    step += 1
    traci.simulationStep()