import pandas as pd
import numpy as np

dados = pd.read_csv('StudentsPerformance.csv', sep=',')

print(dados.describe())
