import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
import numpy as np
import matplotlib.pyplot as plt
import imgkit

#matriz de correlação wspi
corr= base[columns].astype(float).corr() 
a = corr.style.background_gradient(cmap='coolwarm').set_precision(2) 
html = a.render()
imgkit.from_string(html, 'base_correlacao.png')
