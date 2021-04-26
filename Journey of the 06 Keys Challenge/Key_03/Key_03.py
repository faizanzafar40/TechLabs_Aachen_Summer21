import numpy as np
import pandas as pd

df = pd.read_excel('Fallzahlen_Kum_Tab.xlsx')

corr = np.corrcoef(df['LKNR'], df['Inzidenz'])

print(corr[0,1])