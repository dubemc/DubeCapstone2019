
import pandas as pd
#reads csv of January 2018 data

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)

data = pd.read_csv("DubeCapstone2019/JanuaryData.csv")

#default n=5, so it will only print 5 rows of data
print(data)


"""Cites:
  -https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
  --> For code 
  -https://stackoverflow.com/questions/36326544/python-shell-import-pandas
  --> Import error help for Pandas
  - https://www.youtube.com/watch?v=uIcime2nBjs
  --> printing all rows in data frame
  """
