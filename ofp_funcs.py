import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def mgca(df_x,df_mg,df_ca=None,out_ca=False):
    """
    df: pandas dataframe column of with values to convert
    x_ca: float. value of element X normalized to Ca. (e.g. Sr/Ca) in mmol/mol or umol/mol
    returns: x_mgca. element X normalized to Ca + Mg (e.g. Sr/(Ca+Mg))
    """
    if df_ca: # allows us to take raw mmol or umol and normalize to Ca if not already ratios
        x_ca = df_x/df_ca
        mg_ca = (df_mg/1000)/df_ca # convert to mol/mol
    else:
        x_ca = df_x
        mg_ca = df_mg/1000 # convert to mol/mol

    # calculate the new ratio
    x_mgca = x_ca/(1+mg_ca) # needs to be mol/mol

    if out_ca:
        return x_ca,x_mgca

    else:
        return x_mgca

