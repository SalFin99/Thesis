from visualizations import visualizations
from getPolicies import loadCAPMF
import pandas as pd

df = loadCAPMF.cleanCAPFMpolicies()

print(df.head(20))

