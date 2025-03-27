import sys
sys.path.append('/Users/iagapov/workspace/ocelot')
from ocelot import *
from ocelot.cpbd.elements import *

from ocelot.gui.accelerator import *


from test_optics import *

lat = MagneticLattice(lattice_list[0:1100])


tw0 = Twiss()


#AX =2.7906447390331426 BX =6.776927886467602    PSIX =56.49535868579681  AY =-5.526446108975507
#           BY =10.553017034834932   PSIY =44.56549637932061  EX =.027326899999999998  EPX =-.005690000000000001     EY =-.0159411
#           EPY =-.0084628 DX =-1.6293750997286722e-15   DPX =1.163621669096704e-15    DZ =-1.3638179127695162e-15   
#           DP =.00055     EMITX =3.09988e-08  EMITY =3.0999e-11

# tw0.alpha_x = 2.8
# tw0.beta_x = 6.77

# tw0.alpha_y = -5.52
# tw0.beta_y = 10.5
# tw0.E = 0.99
# tw0.emit_xn = 60.e-6
# tw0.emit_yn = 10.e-6

# PSECTB
#disp PSECTB
#   AX      BX      NX      EX     EPX    Element   Length   Value      s(m)       AY      BY      NY      EY     EPY     DetR     #
#  .83305 8.80486 2.13678 -2.E-15 2.0E-17  PSECTB    .00000 0          45.013948  .81046 8.82335 1.78834  .00000  .00000  .0000  346
# -1.7141 31.0331 21.1559  .10994  .00534  $$$       .00000 0         1126.26006 1.58255 35.1286 

energy = 0.5

tw0.alpha_x = 0.83305
tw0.beta_x = 8.80

tw0.alpha_y = 0.81046
tw0.beta_y = 8.82335
tw0.E = energy
tw0.emit_xn = 3.e-8 * energy / 0.511e-3
tw0.emit_yn = 3.e-11 * energy / 0.511e-3
tw0.emit_x = 3.e-8 
tw0.emit_y = 3.e-11



tws = twiss(lat,tw0)

plot_opt_func(lat, tws,legend=False, grid=False, top_plot=['E', 'Dx'])
plt.show()