import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = df.index.astype('datetime64[ns]')

# Clean data / top 2.5%, bottom 2.5%
bottom = df.quantile(0.025).value
top = df.quantile(0.975).value

df = df[(df < top) & (df > bottom)]
df.dropna(inplace=True)


def draw_line_plot():
    # Draw line plot

    fig = plt.figure()
    lp = sns.lineplot(y=df.value, x=df.index)
    plt.xticks(df.index[::len(df.index) // 7])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['data'] = df_bar.index.astype('period[M]')

    df_bar = df_bar.groupby('data').mean()

    # Draw bar plot

    fig = plt.figure()
    df_bar.index = df_bar.index.astype('datetime64[ns]')
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['monthsort'] = df_bar.index.month
    df_bar.sort_values(by='monthsort', inplace=True)
    sns.barplot(x='Year', y='value', data=df_bar, hue='Month', palette='Set2')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)
    months = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3,
              'May': 4, 'Jun': 5, 'Jul': 6, 'Aug': 7,
              'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}

    df_box['monthsort'] = [months[d] for d in df_box.Month]
    df_box.sort_values(by='monthsort', inplace=True)

    fig, ax = plt.subplots(1, 2)
    ax[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(ax=ax[0], x='Year',y='value', data=df_box)
    ax[0].set_ylabel('Page Views')

    sns.boxplot(ax=ax[1], x='Month', y='value', data=df_box)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig