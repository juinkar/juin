Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates=pd.date_range('20130101', periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> dates=pd.date_range('20180216', periods=6)
>>> dates
DatetimeIndex(['2018-02-16', '2018-02-17', '2018-02-18', '2018-02-19',
               '2018-02-20', '2018-02-21'],
              dtype='datetime64[ns]', freq='D')
>>> df2 = pd.DataFrame({ 'A' : 1.,
   ....:                      'B' : pd.Timestamp('20130102'),
   ....:                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
   ....:                      'D' : np.array([3] * 4,dtype='int32'),
   ....:                      'E' : pd.Categorical(["test","train","test","train"]),
   ....:                      'F' : 'foo' })
SyntaxError: invalid syntax
>>> df2 = pd.DataFrame({ 'A' : 1.,
			 'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df=pd.DataFrame('F' : pd.Timestamp('20130102'))
SyntaxError: invalid syntax
>>> df=pd.DataFrame('F' = pd.Timestamp('20130102'))
SyntaxError: keyword can't be an expression
>>> f = pd.Timestamp('20130102'))
SyntaxError: invalid syntax
>>> f = pd.Timestamp('20130102')
>>> f
Timestamp('2013-01-02 00:00:00')
>>> f = pd.Categorical("Male","Female")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f = pd.Categorical("Male","Female")
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\categorical.py", line 281, in __init__
    dtype = CategoricalDtype(categories, ordered)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\dtypes\dtypes.py", line 154, in __init__
    self._finalize(categories, ordered, fastpath=False)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\dtypes\dtypes.py", line 181, in _finalize
    fastpath=fastpath)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\dtypes\dtypes.py", line 319, in _validate_categories
    categories = Index(categories, tupleize_cols=False)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 355, in __new__
    cls._scalar_data_error(data)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 710, in _scalar_data_error
    repr(data)))
TypeError: Index(...) must be called with a collection of some kind, 'Female' was passed
>>> f = pd.Categorical(["Male","Female"])
>>> f
[Male, Female]
Categories (2, object): [Female, Male]
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> df2.head(10)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df2.tail(10)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df2.index
Int64Index([0, 1, 2, 3], dtype='int64')
>>> df2.columns
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
>>> df2.T
                     0                    1                    2  \
A                    1                    1                    1   
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2013-01-02 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo  
>>>  df2
SyntaxError: unexpected indent
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df
NameError: name 'df' is not defined
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2018-02-16  0.607138 -0.587719  1.396044 -0.195886
2018-02-17 -0.177573  0.619541  0.054487 -1.461878
2018-02-18 -1.380737 -0.311687 -0.805077  0.907089
2018-02-19 -1.144763 -0.196145  0.613379 -0.859489
2018-02-20  0.914202  0.204273 -0.183639  0.232705
2018-02-21 -0.970306 -1.152689  0.372199 -0.737376
>>> df.T
   2018-02-16  2018-02-17  2018-02-18  2018-02-19  2018-02-20  2018-02-21
A    0.607138   -0.177573   -1.380737   -1.144763    0.914202   -0.970306
B   -0.587719    0.619541   -0.311687   -0.196145    0.204273   -1.152689
C    1.396044    0.054487   -0.805077    0.613379   -0.183639    0.372199
D   -0.195886   -1.461878    0.907089   -0.859489    0.232705   -0.737376
>>> df.sort_index(axis=1, ascending=False)
                   D         C         B         A
2018-02-16 -0.195886  1.396044 -0.587719  0.607138
2018-02-17 -1.461878  0.054487  0.619541 -0.177573
2018-02-18  0.907089 -0.805077 -0.311687 -1.380737
2018-02-19 -0.859489  0.613379 -0.196145 -1.144763
2018-02-20  0.232705 -0.183639  0.204273  0.914202
2018-02-21 -0.737376  0.372199 -1.152689 -0.970306
>>> df3=df.T
>>> df3
   2018-02-16  2018-02-17  2018-02-18  2018-02-19  2018-02-20  2018-02-21
A    0.607138   -0.177573   -1.380737   -1.144763    0.914202   -0.970306
B   -0.587719    0.619541   -0.311687   -0.196145    0.204273   -1.152689
C    1.396044    0.054487   -0.805077    0.613379   -0.183639    0.372199
D   -0.195886   -1.461878    0.907089   -0.859489    0.232705   -0.737376
>>> df3.sort_index(axis=1,ascending=False)
   2018-02-21  2018-02-20  2018-02-19  2018-02-18  2018-02-17  2018-02-16
A   -0.970306    0.914202   -1.144763   -1.380737   -0.177573    0.607138
B   -1.152689    0.204273   -0.196145   -0.311687    0.619541   -0.587719
C    0.372199   -0.183639    0.613379   -0.805077    0.054487    1.396044
D   -0.737376    0.232705   -0.859489    0.907089   -1.461878   -0.195886
>>> df3.sort_values(by='B')
Traceback (most recent call last):
  File "pandas\_libs\index.pyx", line 457, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 811, in pandas._libs.hashtable.Int64HashTable.get_item
TypeError: an integer is required

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 2525, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 421, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\index.pyx", line 459, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\index.pyx", line 465, in pandas._libs.index.DatetimeEngine._date_check_type
KeyError: 'B'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "pandas\_libs\index.pyx", line 457, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 811, in pandas._libs.hashtable.Int64HashTable.get_item
TypeError: an integer is required

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\datetimes.py", line 1435, in get_loc
    return Index.get_loc(self, key, method, tolerance)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 2527, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 421, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\index.pyx", line 459, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\index.pyx", line 465, in pandas._libs.index.DatetimeEngine._date_check_type
KeyError: 'B'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "pandas\_libs\tslib.pyx", line 1702, in pandas._libs.tslib.convert_str_to_tsobject
  File "pandas/_libs/src\datetime.pxd", line 119, in datetime._string_to_dts
ValueError: Error parsing datetime string "B" at position 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "pandas\_libs\tslib.pyx", line 1732, in pandas._libs.tslib.convert_str_to_tsobject
  File "pandas\_libs\tslibs\parsing.pyx", line 99, in pandas._libs.tslibs.parsing.parse_datetime_string
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\dateutil\parser.py", line 1182, in parse
    return DEFAULTPARSER.parse(timestr, **kwargs)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\dateutil\parser.py", line 559, in parse
    raise ValueError("Unknown string format")
ValueError: Unknown string format

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\datetimes.py", line 1443, in get_loc
    stamp = Timestamp(key, tz=self.tz)
  File "pandas\_libs\tslib.pyx", line 390, in pandas._libs.tslib.Timestamp.__new__
  File "pandas\_libs\tslib.pyx", line 1549, in pandas._libs.tslib.convert_to_tsobject
  File "pandas\_libs\tslib.pyx", line 1735, in pandas._libs.tslib.convert_str_to_tsobject
ValueError: could not convert string to Timestamp

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    df3.sort_values(by='B')
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 3619, in sort_values
    k = self.xs(by, axis=other_axis).values
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 2335, in xs
    return self[key]
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 2139, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 2146, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 1842, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3843, in get
    loc = self.items.get_loc(item)
  File "C:\Users\JUIN\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\datetimes.py", line 1451, in get_loc
    raise KeyError(key)
KeyError: 'B'
>>> df.sort_values(by='B')
                   A         B         C         D
2018-02-21 -0.970306 -1.152689  0.372199 -0.737376
2018-02-16  0.607138 -0.587719  1.396044 -0.195886
2018-02-18 -1.380737 -0.311687 -0.805077  0.907089
2018-02-19 -1.144763 -0.196145  0.613379 -0.859489
2018-02-20  0.914202  0.204273 -0.183639  0.232705
2018-02-17 -0.177573  0.619541  0.054487 -1.461878
>>> df3.sort_values(by='2018-02-18')
   2018-02-16  2018-02-17  2018-02-18  2018-02-19  2018-02-20  2018-02-21
A    0.607138   -0.177573   -1.380737   -1.144763    0.914202   -0.970306
C    1.396044    0.054487   -0.805077    0.613379   -0.183639    0.372199
B   -0.587719    0.619541   -0.311687   -0.196145    0.204273   -1.152689
D   -0.195886   -1.461878    0.907089   -0.859489    0.232705   -0.737376
>>> 
