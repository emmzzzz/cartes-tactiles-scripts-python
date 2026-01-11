import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = pd.read_csv("csv_0_4.csv", sep = ",")


plt.subplots(figsize=(20,4))
ax = sns.boxplot(x=df["Classe"], y=df["Score"], data=df)

model = ols('Score ~ C(Classe)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# si l’ANOVA est significative

tukey = pairwise_tukeyhsd(
    endog=df["Score"],    
    groups=df["Classe"],     
    alpha=0.05 )
print(tukey)
tukey.plot_simultaneous()
plt.show()

