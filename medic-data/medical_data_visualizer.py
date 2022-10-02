import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight'] / (pow(df['height'] / 100, 2))
df['overweight'] = bmi

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.
old_df = df.copy()
bmi = (bmi > 25) * 1
df['overweight'] = bmi
df['cholesterol'] = (df['cholesterol'] > 1) * 1
df['gluc'] = (df['gluc'] > 1) * 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco',
    # 'active', and 'overweight'.
    df_cat = pd.melt(frame=df, id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.

    df_cat['var2'] = df_cat['variable']
    df_cat = df_cat.groupby(['cardio', 'value', 'variable']).count()
    df_cat = pd.DataFrame(np.append(df_cat.index[:].to_frame().values, df_cat.values, axis=1),
                          columns=['cardio', 'value', 'variable', 'total'])

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')

    # Get the figure for the output
    fig = plt.gcf()

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.copy()
    df_heat.loc[df_heat['ap_lo'] > df_heat['ap_hi'], 'ap_lo'] = np.nan
    df_heat.loc[df_heat['height'] < df_heat['height'].quantile(0.025), 'height'] = np.nan
    df_heat.loc[df_heat['height'] > df_heat['height'].quantile(0.975), 'height'] = np.nan
    df_heat.loc[df_heat['weight'] < df_heat['weight'].quantile(0.025), 'weight'] = np.nan
    df_heat.loc[df_heat['weight'] > df_heat['weight'].quantile(0.975), 'weight'] = np.nan
    df_heat.dropna(inplace=True)
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    triangle_indices = np.triu_indices_from(mask)
    mask[triangle_indices] = True
    # Set up the matplotlib figure
    fig, ax = plt.subplots(dpi=300)

    # Draw the heatmap with 'sns.heatmap()'
    sns.color_palette("rocket")
    sns.heatmap(corr, mask=mask, annot=True, annot_kws={'size': 6},
                linewidths=.5, vmax=.3, center=0, fmt='.1f')
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
