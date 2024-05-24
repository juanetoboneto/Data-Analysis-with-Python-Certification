import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], c='#e9c243')

    # Create first line of best fit
    pendiente_1880, intercepto_1880, pearson_1880, p_valor_1880, error_estandar_1880 = linregress(
        x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    abscisa_prediccion_1880 = pd.Series(range(1880, 2050))
    linea_1880 = abscisa_prediccion_1880 * pendiente_1880 + intercepto_1880
    plt.plot(abscisa_prediccion_1880, linea_1880, c='#C70039')

    # Create second line of best fit
    datos_2000 = df[df['Year'] >= 2000]
    pendiente_2000, intercepto_2000, pearson_2000, p_valor_2000, error_estandar_2000 = linregress(
        x=datos_2000['Year'], y=datos_2000['CSIRO Adjusted Sea Level'])
    abscisa_prediccion_2000 = pd.Series(range(2000, 2050))
    linea_2000 = abscisa_prediccion_2000 * pendiente_2000 + intercepto_2000
    plt.plot(abscisa_prediccion_2000, linea_2000, c='#023FF0')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
