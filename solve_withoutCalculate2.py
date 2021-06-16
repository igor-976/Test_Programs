import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as pylab
import pandas as pd
from SkyNet import *
import gc
import os

def calculate_xray(with_my, fileName):
  do_heat = False; do_inv = False; do_screen = False
  with open("X-ray_burst/sunet") as f:
    nuclides = [l.strip() for l in f.readlines()]

  nuclib = NuclideLibrary.CreateFromWinv("X-ray_burst/winvne_v2.0.dat", nuclides)

  opts = NetworkOptions()
  opts.ConvergenceCriterion = NetworkConvergenceCriterion.Mass
  opts.MassDeviationThreshold = 1.0E-10
  opts.IsSelfHeating = do_heat
  opts.EnableScreening = do_screen
  opts.DisableStdoutOutput = True

  helm = HelmholtzEOS(SkyNetRoot + "/data/helm_table.dat")

  strongReactionLibrary = REACLIBReactionLibrary("X-ray_burst/reaclib",
    ReactionType.Strong, do_inv, LeptonMode.TreatAllAsDecayExceptLabelEC,
    "Strong reactions", nuclib, opts, True, True)
  weakReactionLibrary = REACLIBReactionLibrary("X-ray_burst/reaclib",
    ReactionType.Weak, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
    "Weak reactions", nuclib, opts, True, True)
  symmetricFission = REACLIBReactionLibrary("X-ray_burst/nfis",
    ReactionType.Strong, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
    "Symmetric neutron induced fission with 0 neutrons emitted",
    nuclib, opts, True, True)
  spontaneousFission = REACLIBReactionLibrary("X-ray_burst/sfis",
    ReactionType.Strong, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
    "Spontaneous fission", nuclib, opts, True, True)  

  if (with_my):
    reactionLibraries = [strongReactionLibrary, weakReactionLibrary,
      symmetricFission, spontaneousFission]
  else:
    reactionLibraries = [strongReactionLibrary, weakReactionLibrary,
      symmetricFission, spontaneousFission]  

  screen = SkyNetScreening(nuclib)
  net = ReactionNetwork(nuclib, reactionLibraries, helm, screen, opts)

  #lib = net.GetNuclideLibrary()
  #fout = open("sunet", "w")
  #for n in lib.Names():
    #fout.write("%5s\n" % n)
  #fout.close()

  dat = np.loadtxt("X-ray_burst/traj_skynet")
  density_vs_time = PiecewiseLinearFunction(dat[:,0], dat[:,2], True)
  temperature_vs_time = PiecewiseLinearFunction(dat[:,0], dat[:,1], True)

  Temp0 = dat[0,1]
  t0 = dat[0,0] + 1.0e-20

  if (do_heat):
    tfinal = 1.0E+03
  else:
    tfinal = 1.242595E+03

  # initial abundance
  #nseResult = NSE.CalcFromTemperatureAndDensity(Temp0, density_vs_time(t0),
      #Ye0, net.GetNuclideLibrary())
  #np.savetxt("init_Y", nseResult.Y())

  initY = np.loadtxt("X-ray_burst/init_Y")

  if (do_heat):
    output = net.EvolveSelfHeatingWithInitialTemperature(initY, t0, tfinal,
        Temp0, density_vs_time, fileName)
  else:
    output = net.Evolve(initY, t0, tfinal, temperature_vs_time, density_vs_time,
        fileName)
  output.Close()
  net = None
  output = None
  print("Hello")

def calculate_rprocess(with_my, fileName):
  do_heat = False; do_inv = False; do_screen = False
  with open("r-process/sunet") as f:
    nuclides = [l.strip() for l in f.readlines()]

  # make trajectory
  t0 = 1.0e-3
  tfin = 1.0e9

  nuclib = NuclideLibrary.CreateFromWinv("r-process/winvne_v2.0.dat", nuclides)

  opts = NetworkOptions()
  opts.ConvergenceCriterion = NetworkConvergenceCriterion.Mass
  opts.MassDeviationThreshold = 1.0E-10
  opts.IsSelfHeating = do_heat
  opts.EnableScreening = do_screen
  opts.DisableStdoutOutput = True

  helm = HelmholtzEOS(SkyNetRoot + "/data/helm_table.dat")
  if (with_my):
    strongReactionLibrary = REACLIBReactionLibrary("reaclib_with_del_end",
      ReactionType.Strong, do_inv, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Strong reactions", nuclib, opts, True, True)
    weakReactionLibrary = REACLIBReactionLibrary("reaclib_with_del_end",
      ReactionType.Weak, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Weak reactions", nuclib, opts, True, True)
    symmetricFission = REACLIBReactionLibrary("r-process/nfis2",
    ReactionType.Strong, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
    "Symmetric neutron induced fission with 0 neutrons emitted",
    nuclib, opts, True, True)

  else:
    strongReactionLibrary = REACLIBReactionLibrary("r-process/reaclib",
      ReactionType.Strong, do_inv, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Strong reactions", nuclib, opts, True, True)
    weakReactionLibrary = REACLIBReactionLibrary("r-process/reaclib",
      ReactionType.Weak, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Weak reactions", nuclib, opts, True, True)
    symmetricFission = REACLIBReactionLibrary("r-process/nfis",
      ReactionType.Strong, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Symmetric neutron induced fission with 0 neutrons emitted",
      nuclib, opts, True, True)
  spontaneousFission = REACLIBReactionLibrary("r-process/sfis",
    ReactionType.Strong, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
    "Spontaneous fission", nuclib, opts, True, True)
  delReaction1 = REACLIBReactionLibrary("delete_reactions",
     ReactionType.Weak, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
     "Symmetric neutron induced fission with 0 neutrons emitted",
     nuclib, opts, True, True) 
  delReaction2 = REACLIBReactionLibrary("delete_reactions",
      ReactionType.Strong, do_inv, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Strong reactions", nuclib, opts, True, True)
  myLib = REACLIBReactionLibrary("mylib.txt",
      ReactionType.Weak, False, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Weak reactions", nuclib, opts, True, True)
  myLib2 = REACLIBReactionLibrary("mylib.txt",
      ReactionType.Strong, do_inv, LeptonMode.TreatAllAsDecayExceptLabelEC,
      "Strong reactions", nuclib, opts, True, True)
 
  if (with_my):
    reactionLibraries = [strongReactionLibrary, weakReactionLibrary,
      symmetricFission, spontaneousFission, delReaction1, delReaction2, myLib, myLib2]
  else:
    reactionLibraries = [strongReactionLibrary, weakReactionLibrary,
      symmetricFission, spontaneousFission]  

  screen = SkyNetScreening(nuclib)
  net = ReactionNetwork(nuclib, reactionLibraries, helm, screen, opts)

  #lib = net.GetNuclideLibrary()
  #fout = open("sunet", "w")
  #for n in lib.Names():
    #fout.write("%5s\n" % n)
  #fout.close()

  dat = np.loadtxt("r-process/traj_skynet")
  density_vs_time = PiecewiseLinearFunction(dat[:,0], dat[:,2], True)
  temperature_vs_time = PiecewiseLinearFunction(dat[:,0], dat[:,1], True)

  Ye0 = 0.07
  Temp0 = dat[0,1]
  tfinal = 5.0e8

  # initial abundance
  #nseResult = NSE.CalcFromTemperatureAndDensity(Temp0, density_vs_time(t0),
      #Ye0, net.GetNuclideLibrary())
  #np.savetxt("init_Y", nseResult.Y())

  initY = np.loadtxt("r-process/init_Y")

  if (do_heat):
    output = net.EvolveSelfHeatingWithInitialTemperature(initY, t0, tfinal,
        Temp0, density_vs_time, fileName)
  else:
    output = net.Evolve(initY, t0, tfinal, temperature_vs_time, density_vs_time, fileName)

index = 1
multiply = 1

calculate_rprocess(True, "out-r/WithMy-" + str(index))
calculate_rprocess(False, "out-r/WithoutMy-" + str(index))

# while index > 30:
#   index = index - 1
#   multiply = 10**(index)
#   os.remove("mylib.txt")
#   for file_index in range(0, len(onlyfiles)):
#     write_solution('out-sig/' + onlyfiles[file_index], multiply)
#   calculate_rprocess(True, "out-r/WithMy-" + str(index))
#   calculate_rprocess(False, "out-r/WithoutMy-" + str(index))
