import subprocess
class engine:
    ''' EXAMPLE Values - Notice how the values are strings!
    pressure = '0'
    ptype = 'psi'
    pratio = '27.2'
    fuel = 'CH4'
    oxidizer = 'O2(L)'
    OFratio = '2.0'
    FuelTemp = '298'
    OxTemp = '90.17'
    '''
    def __init__(self,pressure,ptype,pratio,fuel,oxidizer,OFratio,FuelTemp='298',OxTemp='298'):
        self.pressure = pressure    #define the chamber pressure
        self.ptype = ptype          #define the chamber pressure units
        self.pratio = pratio        #Exit/Chamber Pressure Ratio
        self.fuel = fuel            #define the fuel type
        self.oxidizer = oxidizer    #define the oxidizer type
        self.OFratio = OFratio      #define the O/F ratio
        self.FuelTemp = FuelTemp    #define the FuelTemp (K)
        self.OxTemp = OxTemp        #define the OxTemp (K)


def writefile(ARES):
    'Write the cea input file from a given rocket engine class'
    f = open('CEA\\ceaexec\\ceapy.inp','w')
    f.write('problem\n')
    f.write('rocket\n')
    pressurestr = 'p,'+ ARES.ptype + '=' + ARES.pressure + '\n'
    f.write(pressurestr)
    pratiostr = 'pc/p='+ ARES.pratio + '\n'
    f.write(pratiostr)
    OFratiostr = 'o/f=' + ARES.OFratio + '\n'
    f.write(OFratiostr)
    f.write('reac\n')
    fuelstr = 'fuel ' + ARES.fuel + ' t,k='+ ARES.FuelTemp + ' wt%=100.00' + '\n'
    oxstr = 'oxid ' + ARES.oxidizer + ' t,k='+ ARES.OxTemp + ' wt%=100.00' + '\n'
    f.write(fuelstr)
    f.write(oxstr)
    f.write('end\n')
    f.close()

def runcea():
    'Run the FCEA.exe function'
    p = subprocess.Popen("FCEA2.exe",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,cwd="CEA\\ceaexec")
    p.stdout.readline()
    p.stdin.write(b'ceapy\n')

def readcea():
    'read the values required for trajectory approximations'
    f = open('CEA\\ceaexec\\ceapy.out','r')
    for line in f:
        if 'T, K' in line:
            To = line
        if 'CF' in line:
            Cf = line
        if 'Isp' in line:
            isp = line
        if 'GAMMAs' in line:
            gam = line
        if 'Cp' in line:
            cp = line
    print(To)
    print(Cf)
    print(isp)
    print(gam)
    print(cp)
    f.close()



        
