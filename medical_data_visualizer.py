import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('/workspace/boilerplate-medical-data-visualizer/medical_examination.csv')

# 2
df['overweight'] = df['weight']/((df['height']/100)**2)
df['overweight'] = df['overweight'] = [1 if x > 25 else 0 for x in df['overweight']]

# 3
df['cholesterol'] = [0 if i == 1 else 1 for i in df['cholesterol']]
df['gluc'] = [0 if z == 1 else 1 for z in df['gluc']]

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # 7
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")


    # 8
    fig = graph.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(16, 9))

    # 15
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")


    # 16
    fig.savefig('heatmap.png')
    return fig
