class RobotEmil:
    def __init__(self, meno_suboru, pozicia):
        t = open(meno_suboru, 'r')
        self.riadok = t.readline().split()
        #print(self.riadok)
        self.pocet_riadkov = int(self.riadok[0])
        self.pocet_stlpcov = int(self.riadok[1])
        self.pole_zozbieranych = []

        self.hracia_plocha = [[0 for j in range(self.pocet_stlpcov + 2)] for i in range(self.pocet_riadkov + 2)]

        for i in range(self.pocet_stlpcov + 2):
            self.hracia_plocha[0][i] = 'xx'
            self.hracia_plocha[self.pocet_riadkov + 1][i] = 'xx'

        for j in range(self.pocet_riadkov + 2):
            self.hracia_plocha[j][0] = 'xx'
            self.hracia_plocha[j][self.pocet_stlpcov + 1] = '\n'
        

        self.robot_riadok = int(pozicia[0]) + 1
        self.robot_stlpec = int(pozicia[1]) + 1

        
        
        self.riadok = t.readline().split()
        while self.riadok != [] and self.riadok != '':
            self.hracia_plocha[int(self.riadok[1]) + 1][int(self.riadok[2]) + 1] = self.riadok[0]
            self.riadok = t.readline().split()

        #print(self.hracia_plocha)

        t.close()
        

    def __str__(self):
        self.vypis_pole = []

        for i in range(1, self.pocet_riadkov + 1):
            for j in range(1, self.pocet_stlpcov + 2):
                if i == self.robot_riadok and j == self.robot_stlpec:
                    self.vypis_pole.append('E')
                else:
                    self.vypis_pole.append(str(self.hracia_plocha[i][j]))


        for i in range(len(self.vypis_pole)):
            if self.vypis_pole[i] in '0':
                self.vypis_pole[i] = '.'


        del self.vypis_pole[-1]
        return ''.join(self.vypis_pole)

    def rob(self, prikazy):
        self.pocet_zozbieranych = 0
        for znak in prikazy:

            if znak == 'v':
                while (self.hracia_plocha[self.robot_riadok][self.robot_stlpec + 1] != 'M'
                       and self.hracia_plocha[self.robot_riadok][self.robot_stlpec + 1] != 'xx'
                       and self.hracia_plocha[self.robot_riadok][self.robot_stlpec + 1] != '\n'):
                    self.robot_stlpec += 1
                    if type(self.hracia_plocha[self.robot_riadok][self.robot_stlpec]) == str:
                        self.pole_zozbieranych.append(self.hracia_plocha[self.robot_riadok][self.robot_stlpec])
                        self.hracia_plocha[self.robot_riadok][self.robot_stlpec] = 0
                        self.pocet_zozbieranych += 1                       
                        

            if znak == 'j':
                while (self.hracia_plocha[self.robot_riadok + 1][self.robot_stlpec] != 'M'
                       and self.hracia_plocha[self.robot_riadok + 1][self.robot_stlpec] != 'xx'
                       and self.hracia_plocha[self.robot_riadok + 1][self.robot_stlpec] != '\n'):
                    self.robot_riadok += 1
                    if type(self.hracia_plocha[self.robot_riadok][self.robot_stlpec]) == str:
                        self.pole_zozbieranych.append(self.hracia_plocha[self.robot_riadok][self.robot_stlpec])
                        self.hracia_plocha[self.robot_riadok][self.robot_stlpec] = 0
                        self.pocet_zozbieranych += 1

            if znak == 'z':
                while (self.hracia_plocha[self.robot_riadok][self.robot_stlpec - 1] != 'M'
                       and self.hracia_plocha[self.robot_riadok][self.robot_stlpec - 1] != 'xx'
                       and self.hracia_plocha[self.robot_riadok][self.robot_stlpec - 1] != '\n'):
                    self.robot_stlpec -= 1
                    if type(self.hracia_plocha[self.robot_riadok][self.robot_stlpec]) == str:
                        self.pole_zozbieranych.append(self.hracia_plocha[self.robot_riadok][self.robot_stlpec])
                        self.hracia_plocha[self.robot_riadok][self.robot_stlpec] = 0
                        self.pocet_zozbieranych += 1

            if znak == 's':
                while (self.hracia_plocha[self.robot_riadok - 1][self.robot_stlpec] != 'M'
                       and self.hracia_plocha[self.robot_riadok - 1][self.robot_stlpec] != 'xx'
                       and self.hracia_plocha[self.robot_riadok - 1][self.robot_stlpec] != '\n'):
                    self.robot_riadok -= 1
                    if type(self.hracia_plocha[self.robot_riadok][self.robot_stlpec]) == str:
                        self.pole_zozbieranych.append(self.hracia_plocha[self.robot_riadok][self.robot_stlpec])
                        self.hracia_plocha[self.robot_riadok][self.robot_stlpec] = 0
                        self.pocet_zozbieranych += 1
                
        return self.pocet_zozbieranych
    
    def co_pozbieral(self):      
        return self.pole_zozbieranych

if __name__ == '__main__':
    e = RobotEmil('subor1.txt', (1, 2))
    print(e)
    print('pozbieral', e.rob('vjzsjzsvjz'))
    print(e)
    print(e.co_pozbieral())
