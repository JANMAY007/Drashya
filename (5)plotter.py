import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf
import matplotlib.pyplot as plt

po.init_notebook_mode(connected=True)
cf.go_offline()


def createdata(data):
    global df1
    if (data == 1):
        x = np.random.rand(100, 5)
        df1 = pd.DataFrame(x, columns=['A', 'B', 'C', 'D', 'E'])

    elif (data == 2):
        x = [0, 0, 0, 0, 0]
        r1 = [0, 0, 0, 0, 0]
        r2 = [0, 0, 0, 0, 0]
        r3 = [0, 0, 0, 0, 0]
        r4 = [0, 0, 0, 0, 0]
        print('Enter the values for columns')
        for i in [0, 1, 2, 3, 4]:
            x[i] = input()
        print('Enter the values for first row')
        for i in [0, 1, 2, 3, 4]:
            r1[i] = int(input())
        print('Enter the values for second row')
        for i in [0, 1, 2, 3, 4]:
            r2[i] = int(input())
        print('Enter the values for third row')
        for i in [0, 1, 2, 3, 4]:
            r3[i] = int(input())
        print('Enter the values for fourth row')
        for i in [0, 1, 2, 3, 4]:
            r4[i] = int(input())
        df1 = pd.DataFrame([r1, r2, r3, r4], columns=x)

    elif (data == 3):
        file = input('Enter the file name')
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)

    else:
        print('DataFrame creation failed please enter in between 1 to 3 and try again')

    return df1


def plotter1(plot):
    if (plot == 1):
        df1.iplot(kind='scatter')
        plt.show()

    elif (plot == 2):
        df1.iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
        plt.show()

    elif (plot == 3):
        df1.iplot(kind='bar')
        plt.show()

    elif (plot == 4):
        df1.iplot(kind='hist')
        plt.show()

    elif (plot == 5):
        df1.iplot(kind='box')
        plt.show()

    elif (plot == 6):
        df1.iplot(kind='surface')
        plt.show()

    else:
        print('Select only between 1 to 7')


def plotter2(plot):
    global finalplot
    col = input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3')
    col = int(col)

    if (col == 1):
        colm = input('Enter the column you want to plot by selecting any column from dataframe head')

        if (plot == 1):
            finalplot = df1[colm].iplot(kind='scatter')
            plt.show()

        elif (plot == 2):
            finalplot = df1[colm].iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
            plt.show()

        elif (plot == 3):
            finalplot = df1[colm].iplot(kind='bar')
            plt.show()

        elif (plot == 4):
            finalplot = df1[colm].iplot(kind='hist')
            plt.show()

        elif (plot == 5):
            finalplot = df1[colm].iplot(kind='box')
            plt.show()

        elif (plot == 6 or plot == 7):
            finalplot = print('Bubble plot and surface plot require more than one column arguments')

        else:
            finalplot = print('Select only between 1 to 7')

    elif (col == 2):
        print('Enter the columns you want to plot by selecting from dataframe head')
        x = input('First column')
        y = input('Second column')

        if (plot == 1):
            finalplot = df1[[x, y]].iplot(kind='scatter')
            plt.show()

        elif (plot == 2):
            finalplot = df1[[x, y]].iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
            plt.show()

        elif (plot == 3):
            finalplot = df1[[x, y]].iplot(kind='bar')
            plt.show()

        elif (plot == 4):
            finalplot = df1[[x, y]].iplot(kind='hist')
            plt.show()

        elif (plot == 5):
            finalplot = df1[[x, y]].iplot(kind='box')
            plt.show()

        elif (plot == 6):
            finalplot = df1[[x, y]].iplot(kind='surface')
            plt.show()

        elif (plot == 7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble', x=x, y=y, size=size)
            plt.show()

        else:
            finalplot = print('Select only between 1 to 7')

    elif (col == 3):
        print('Enter the columns you want to plot')
        x = input('First column')
        y = input('Second column')
        z = input('Third column')

        if (plot == 1):
            finalplot = df1[[x, y, z]].iplot(kind='scatter')
            plt.show()

        elif (plot == 2):
            finalplot = df1[[x, y, z]].iplot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
            plt.show()

        elif (plot == 3):
            finalplot = df1[[x, y, z]].iplot(kind='bar')
            plt.show()

        elif (plot == 4):
            finalplot = df1[[x, y, z]].iplot(kind='hist')
            plt.show()

        elif (plot == 5):
            finalplot = df1[[x, y, z]].iplot(kind='box')
            plt.show()

        elif (plot == 6):
            finalplot = df1[[x, y, z]].iplot(kind='surface')
            plt.show()

        elif (plot == 7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble', x=x, y=y, z=z, size=size)
            plt.show()

        else:
            print('Select only between 1 to 7')

    else:
        print('Please enter only 1 , 2 or 3')

    return finalplot


def main(cat):
    if (cat == 1):
        print('Select the type of plot you need to plot by writing 1 to 6')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        plot = int(input())
        plotter1(plot)

    elif (cat == 2):
        print('Select the type of plot you need to plot by writing 1 to 7')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot')
        plot = int(input())
        plotter2(plot)

    else:
        print('Please enter 1 or 2 and try again')


if __name__ == "__main__":
    print('Select the type of data you need to plot(By writing 1,2 or 3)')
    print('1.Random data with 100 rows and 5 columns')
    print('2.Customize dataframe with 5 columns and. 4 rows')
    print('3.Upload csv/json/txt file')
    data = int(input())
    df1 = createdata(data)
    print('Your DataFrame head is given below check the columns to plot using cufflinks')
    df1.head()
    print('What kind of plot you need , the complete data plot or columns plot')
    cat = input('Press 1 for plotting all columns or press 2 for specifying columns to plot')
    cat = int(cat)
    main(cat)
