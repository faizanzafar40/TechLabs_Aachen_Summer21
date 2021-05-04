import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
% matplotlib inline
import io

df = pd.read_csv(io.StringIO(uploaded['plotdata.csv'].decode('utf-8')))

plt.imshow(df)