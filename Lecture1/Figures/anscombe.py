import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df, col_wrap=2, fit_reg = False, ci=None, palette=None, size=4, scatter_kws={"s": 50, "alpha": 1})
plt.savefig('anscombe.pdf')
plt.close()

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df, col_wrap=2, ci=None, palette="deep", size=4, scatter_kws={"s": 50, "alpha": 1})
plt.savefig('anscombe2.pdf')
plt.close()
