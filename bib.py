import random
import traci
import traci.constants as tc
from math import *

def cont(a,b):
    save = True
    for i in range (len(b)):
        if (a == traci.route.getEdges(b[i])):
            save = False
    return save


def insert_veh(num,route,id):
    edges = traci.route.getEdges(routeID=route)
    lanes = traci.edge.getLaneNumber(edgeID=edges[0])
    if num <= lanes:
        for i in range (0,num):
            traci.vehicle.addLegacy(vehID=route+"_"+str(id),routeID=route,lane="free",depart="triggered",pos=7)
            id+=1
            num-=1
    else:
        for i in range (0,lanes):
            traci.vehicle.addLegacy(vehID=route+"_"+str(id),routeID=route,lane="free",depart="triggered",pos=7)
            id+=1
            num-=1
    return num,id


def reroute(vehids,route):
    for i in range (len(vehids)):
        traci.vehicle.setRouteID(vehID=vehids[i],routeID=route)

def reroutealt(vehids,target):
    for i in range (len(vehids)):
        traci.vehicle.changeTarget(vehID=vehids[i],edgeID=target)
