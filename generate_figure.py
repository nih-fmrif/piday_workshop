# coding: utf-8
import matplotlib as mpl
mpl.use('Agg')
import seaborn as sns


# add a comment
df_tips = sns.load_dataset('tips')
seaborn_plot = sns.pairplot(df_tips)
seaborn_plot.savefig('pairplot.png')
