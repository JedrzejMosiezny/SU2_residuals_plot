import os
from argparse import ArgumentParser
import platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="history", help="Open specified file")
args = parser.parse_args()
history = args.history

hist = pd.DataFrame(pd.read_csv(history, delimiter=",", decimal='.', header=0, skiprows=0, usecols=["Iteration", "Res_Flow[0]", "Res_Flow[1]", "Res_Flow[2]", "Res_Flow[3]", "Res_Flow[4]", "Res_Turb[0]", "Res_Turb[1]"])).set_index('Iteration')
unscalled = hist.apply(lambda x: 10**(x), axis=1)
n5 = pd.DataFrame(unscalled.iloc[0:5].max()).transpose()
scalled = unscalled.div(n5.iloc[0],axis='columns')

scalled.plot(figsize=(20, 10)); plt.yscale('log')
plt.savefig('residuals.png')
plt.close()