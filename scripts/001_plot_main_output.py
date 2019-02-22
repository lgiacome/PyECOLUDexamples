# generate example figures with main PyECLOUD outputs
# Thanks for E. Belli, L. Mether and A. Romano for preparing this script

import pylab as pl
import numpy as np

import PyECLOUD.myloadmat_to_obj as mlo
import PyECLOUD.mystyle as ms

pl.close('all')
ms.mystyle_arial(fontsz=16)
dpiset = 200

ob = mlo.myloadmat_to_obj('Pyecltest.mat')

ifig = 0


#################################
# Variables saved per time step #
#################################

#8.
ifig += 1; pl.figure(ifig)
pl.plot(ob.t, ob.lam_t_array, linewidth=2)
pl.xlabel('Time [s]')
pl.ylabel('Beam profile [p/m]')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: lam_t_array\nBeam density at each time step')
pl.subplots_adjust(top=.82, bottom=.14)

#6.
ifig += 1; pl.figure(ifig)
pl.plot(ob.t, ob.Nel_timep, linewidth=2)
pl.xlabel('Time [s]')
pl.ylabel('Number of $e^-$ per unit length [$m^{-1}$]')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: Nel_timep\nNumber of electrons in the chamber at each time step')
pl.subplots_adjust(top=.82, bottom=.14)

#5.
ifig += 1; pl.figure(ifig)
pl.plot(ob.t, ob.Nel_imp_time, linewidth=2)
pl.xlabel('Time [s]')
pl.ylabel('Number of impacting $e^-$ per unit length [$m^{-1}$]')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: Nel_imp_time\nNumber of electrons that impact the walls in each time-step')
pl.subplots_adjust(top=.82, bottom=.14)

#4.
ifig += 1; pl.figure(ifig)
pl.plot(ob.t, ob.Nel_emit_time, linewidth=2)
pl.xlabel('Time [s]')
pl.ylabel('Number of emitted $e^-$ per unit length [$m^{-1}$]')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: Nel_emit_time\nNumber of electrons emitted by walls in each time-step')
pl.subplots_adjust(top=.82, bottom=.14)

#2.
ifig += 1; pl.figure(ifig)
pl.plot(ob.t, ob.En_imp_eV_time, linewidth=2)
pl.xlabel('Time [s]')
pl.ylabel('Deposited electron energy [eV]')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: En_imp_eV_time\nElectron energy deposited on the walls in each time-step')
pl.subplots_adjust(top=.82, bottom=.14)


###############################
# Variables saved per passage #
###############################

###############################
# Variables saved in matrices #
#   (Projections are shown)   #
###############################

#The output file also contains variables represented by matrices with dimension (t_hist, xg_hist) where t_hist[i] represent the time
#right before the i-th passage in the machine and xg_hist[i] represents the position of the i-th slice inside the chamber
#--> dim(t_hist)=#passages, dim(xg_hist)=#slices


#P |----------------------|
#A |----------------------|
#S |----------------------|
#S |----------------------|
#A |----------------------|
#G |----------------------|
#E |----------------------|
            #SLICE

#9.
ifig += 1; pl.figure(ifig)
pl.plot(np.sum(ob.nel_hist, axis=1), linewidth=2)  # axis=1: sum w.r.t. columns
pl.xlabel('Passage')
pl.ylabel('Number of $e^-$ per unit length [$m^{-1}$]')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: sum(nel_hist, axis=1)\nNumber of electrons at each passage')
pl.subplots_adjust(top=.82, bottom=.14)

#10.
ifig += 1; pl.figure(ifig)
pl.plot(ob.xg_hist, np.sum(ob.nel_hist, axis=0), linewidth=2)  # axis=0: sum w.r.t. rows
pl.xlabel('Chamber bin position [m]')
pl.ylabel('Number of $e^-$ per bin')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: sum(nel_hist, axis=0)\nnumber of electrons in each slice')
pl.subplots_adjust(top=.82, bottom=.14)

#14.
ifig += 1; pl.figure(ifig)
pl.plot(ob.xg_hist, np.sum(ob.nel_impact_hist_tot, axis=0), linewidth=2)
pl.xlabel('Chamber bin position [m]')
pl.ylabel('Impacting $e^-$ per bin')
ms.scix(); pl.grid('on')
pl.suptitle('Var. name: sum(nel_impact_hist_tot, axis=0)\nNumber of impacting electrons in each slice')
pl.subplots_adjust(top=.82, bottom=.14)

#19.
ifig += 1; pl.figure(ifig)
pl.plot(np.sum(ob.energ_eV_impact_hist, axis=1), linewidth=2)
pl.xlabel('Passage')
pl.ylabel('Energy of impacting electrons [eV]')
pl.grid('on'); ms.sciy()
pl.suptitle('Var. name: sum(energ_eV_impact_hist, axis=1)\nEnergy of impacting electrons at each passage')
pl.subplots_adjust(top=.82, bottom=.14)

#20.
ifig += 1; pl.figure(ifig)
pl.plot(ob.xg_hist, np.sum(ob.energ_eV_impact_hist, axis=0), linewidth=2)
pl.xlabel('Position in the chamber [m]')
pl.ylabel('Energy of impacting electrons[eV]')
pl.grid('on'); ms.sciy(); ms.scix()
pl.suptitle('Var. name: sum(energ_eV_impact_hist, axis=0)\nTotal energy of impacting electrons per passage [eV]')
pl.subplots_adjust(top=.82, bottom=.14)


pl.show()





