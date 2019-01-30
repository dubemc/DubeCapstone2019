
import pandas as pd
#reads csv of January 2018 data
data = pd.read_csv("JanuaryData.csv")

#default n=5, so it will only print 5 rows of data
data.head()


"""Cites:
  -https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
  """
