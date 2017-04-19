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
lam = [365,445,550] 
z= sp.arange(2,6,0.1)
def Lnu(lam,z):
    return (1E28*SFR*(lam/(1+z*150.))**(beta+2.))*(u.erg/(u.s*u.hertz))

def s(lam,z):
    d = cosmo.luminosity_distance(z)#Returns in Mpc
    return (((1+z)*Lnu(lam,z))/(4*sp.pi*d**2)).to(u.uJy)

for i in range(3):
    pl.plot(z,(s(lam[i],z)))
pl.show()