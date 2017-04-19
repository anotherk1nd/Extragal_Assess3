import scipy as sp
import matplotlib.pyplot as pl
pl.close('all')
import astropy
import astropy.units as u
from astropy.cosmology import funcs
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
#nanojansky
SFR = 10. # M_sol/yr
beta = -2.3
lam = [365,445,550] #sp.arange(10.,400.,1)
z= sp.arange(2,6,0.1)
"""
def Lnu(lam,beta):
    if lam<91.2:
        return 0.0*(u.erg/(u.s*u.hertz))
    else:
        return (1E28*SFR*(lam/150.)**(beta+2.0))*(u.erg/(u.s*u.hertz)) #We use the SED from APS2
z = sp.arange(2,6,0.1)
"""
def Lnu(lam,z):
    return (1E28*SFR*(lam/(1+z*150.))**(beta+2.))*(u.erg/(u.s*u.hertz))

def s(lam,z):
    d = cosmo.luminosity_distance(z)#Returns in Mpc
    #print d.unit
    #print ((1+z.)*Lnu)
    return (((1+z)*Lnu(lam,z))/(4*sp.pi*d**2)).to(u.uJy)
    #return ((1+z)*Lnu(lam,z))/(4*sp.pi*d**2).to(u.uJy)
    #return ((1+z)*Lnu(lam,z))*(u.erg/(u.s*u.hertz))/(4*sp.pi*d**2)#.to(u.uJy)

for i in range(3):
    pl.plot(z,(s(lam[i],z)))
pl.show()

#THIS CODE BELOW IS WRKIN!
"""
Lnu =( 1E28*SFR*(lam/(1+z*150.))**(beta+2.))*(u.erg/(u.s*u.hertz))
print Lnu.unit
#Lnu[lam<91.2] = 0.*(u.erg/(u.s*u.hertz)) 

def s(Lnu,z):
    d = cosmo.luminosity_distance(z)#Returns in Mpc
    #print d.unit
    #print ((1+z.)*Lnu)
    #print 'here,',((1+z)*Lnu)*(u.erg/(u.s*u.hertz))/(4*sp.pi*d**2).unit
    return ((1+z)*Lnu)*(u.erg/(u.s*u.hertz))/(4*sp.pi*d**2)

z = sp.arange(2,6,0.1)
for i in range(3):
    pl.plot(z,s(Lnu,z))
    pl.show()
"""



"""
def s(lam,z): # We define the FLUX density
    d = cosmo.luminosity_distance(z)#Returns in Mpc
    #print sp.divide((1+z)*Lnu(lam*u.nm/(1+z),beta),(4*sp.pi*d**2)).unit
    print 'Lnu:,',Lnu(lam,z).unit
    print sp.divide((1+z)*Lnu(lam*u.nm/(1+z),beta),(4*sp.pi*d**2))
    #return sp.divide((1+z)*Lnu(lam,beta)*u.erg*u.s**{-1}*u.hz**{-1}*(lam*u.nm/(1+z)),4*sp.pi*d*u.megaparsec*2)
"""

#print s(100.,2.).to(u.uJy)
"""
pl.plot(z,s(365,z))
pl.plot(z,s(445,z))
pl.plot(z,s(550,z))
pl.show()
"""