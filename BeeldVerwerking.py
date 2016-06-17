from math import sin, cos, pi

class BeeldVerwerking:
    def __init__(self):
        self.m = []
        for i in range(4):
            self.m.append([])
            for j in range(4):
                if i == j:
                    self.m[i].append(1)
                else:
                    self.m[i].append(0)

    def rads(self,degrees):
        return degrees * (pi / 180)

    def calc(self,value,posx,posy,m):
        if m[posy][posx] == 0:
            m[posy][posx] = round(value,3)
        else:
            m[posy][posx] *= round(value,3)

    def rotation(self,angle,pos,m):
        a = self.rads(angle)
        self.calc(cos(a),pos,pos,m)
        self.calc(-sin(a),(pos+1)%3,pos,m)
        self.calc(sin(a),pos,(pos+1)%3,m)
        self.calc(cos(a),(pos+1)%3,(pos+1)%3,m)

    def createMatrix(self,pitch,roll,yaw,v):
        m = self.m
        self.rotation(pitch,0,m)
        self.rotation(roll,1,m)
        self.rotation(yaw,2,m)
        for i in range(3):
            m[i][3] = v[i]
        self.transform = m

    def calcPos(self,pos):
        r = []
        for i in range(4):
            som = 0
            for j in range(4):
                som += self.transform[i][j] * pos[j]
            r.append(som)
        return r

    def calcAll(self,positions,pitch,roll,yaw,v):
        self.createMatrix(pitch,roll,yaw,v)
        r = []
        for i in positions:
            r.append(self.calcPos(i))
        print "all new positions",r
        return r