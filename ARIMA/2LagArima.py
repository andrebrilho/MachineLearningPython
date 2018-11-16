from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.tools.plotting import autocorrelation_plot


def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('teste2.csv', header=0, nrows=36, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
autocorrelation_plot(series)
pyplot.show()