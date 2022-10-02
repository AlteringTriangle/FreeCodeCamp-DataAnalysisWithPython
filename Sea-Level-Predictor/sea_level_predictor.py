import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(y='CSIRO Adjusted Sea Level', x='Year', data=df)


    # Create first line of best fit
    slope, intercept = scipy.stats.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[0:2]
    x = np.linspace(df.iloc[0, 0], 2050, 171)
    y = x*slope + intercept
    plt.plot(x, y)

    # Create second line of best fit
    slope, intercept = scipy.stats.linregress(df['Year'].iloc[120:], df['CSIRO Adjusted Sea Level'].iloc[120:])[0:2]
    x = np.linspace(2000, 2050, 51)
    y = x * slope + intercept
    plt.plot(x, y, 'g')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
