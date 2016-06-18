from math import sin, cos, pi
from copy import copy, deepcopy

class BeeldVerwerking:
    def __init__(self):
        self.matrix = []
        for i in range(4):
            self.matrix.append([])
            for j in range(4):
                if i == j:
                    self.matrix[i].append(1)
                else:
                    self.matrix[i].append(0)

    def rads(self,degrees):
        return degrees * (pi / 180)

    def rotation(self,angle,pos):
        m = deepcopy(self.matrix)
        a = self.rads(angle)
        m[pos][pos] = round(cos(a),3)
        m[(pos+1)%3][pos] = round(-sin(a),3)
        m[pos][(pos+1)%3] = round(sin(a),3)
        m[(pos+1)%3][(pos+1)%3] = round(cos(a),3)
        print "m ",m

        result = []
        for i in range(4):
            result.append([])
            for j in range(4):
                som = 0
                for k in range(4):
                    som += m[i][k] * self.m[k][j]
                result[i].append(som)
        print "result ", result
        self.m = result

    def createMatrix(self,pitch,roll,yaw,v):
        self.m = deepcopy(self.matrix)
        self.rotation(pitch,0)
        self.rotation(roll,1)
        self.rotation(yaw,2)
        for i in range(3):
            self.m[i][3] = v[i]
        self.transform = self.m

    def calcPos(self,pos):
        r = []
        for i in range(4):
            som = 0
            for j in range(4):
                som += self.transform[i][j] * pos[j]
            r.append(som)
        return r

    def calcAll(self,positions,roll,pitch,yaw,v):
        self.createMatrix(roll,pitch,yaw,v)
        r = []
        for i in positions:
            r.append(self.calcPos(i))
        return r