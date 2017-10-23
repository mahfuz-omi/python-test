import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#s = pd.Series(data, index=index)
s = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

# a    0.045506
# b    0.971440
# c    0.484570
# d    0.128503
# e    0.679532
# dtype: float64


d = {'a' : 0., 'b' : 1., 'c' : 2.}
pd.Series(d)
print(d)

# {'a': 0.0, 'b': 1.0, 'c': 2.0}


print(pd.Series(d, index=['b', 'c', 'd', 'a']))

# b    1.0
# c    2.0
# d    NaN
# a    0.0
# dtype: float64

print(pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))

# a    5.0
# b    5.0
# c    5.0
# d    5.0
# e    5.0
# dtype: float64

print(s[0])

# 0.0455060470941

print(s['c'])

# 0.484570

print('e' in s)
# True

print('f' in s)
# False

print(s.get('g'))

# None

print(s+s)

print(2*s)

print(np.exp(s))

s = pd.Series(np.random.randn(5), name='something')
print(s)

# 0    1.846990
# 1   -0.130234
# 2    0.044144
# 3   -1.417306
# 4    0.304393
# Name: something, dtype: float64

print(s.name)

# something

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
   'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

print(df)

# one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0

print(pd.DataFrame(d, index=['d', 'b', 'a']))

# one  two
# d  NaN  4.0
# b  2.0  2.0
# a  1.0  1.0

print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))

# two three
# d  4.0   NaN
# b  2.0   NaN
# a  1.0   NaN

print(df.index)
# Index(['a', 'b', 'c', 'd'], dtype='object')

print(df.columns)

# Index(['one', 'two'], dtype='object')

d = {'one' : [1., 2., 3., 4.],
'two' : [4., 3., 2., 1.]}

df = pd.DataFrame(d)
print(df)

# one  two
# 0  1.0  4.0
# 1  2.0  3.0
# 2  3.0  2.0
# 3  4.0  1.0

print(df['one'])

# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0

print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))

# one  two
# a  1.0  4.0
# b  2.0  3.0
# c  3.0  2.0
# d  4.0  1.0

df['three'] = df['one'] * df['two']

print(df)

# one  two  three
# 0  1.0  4.0    4.0
# 1  2.0  3.0    6.0
# 2  3.0  2.0    6.0
# 3  4.0  1.0    4.0

del df['two']
print(df)

# one  three
# 0  1.0    4.0
# 1  2.0    6.0
# 2  3.0    6.0
# 3  4.0    4.0

df['foo'] = 'bar'

print(df)

# one  three  foo
# 0  1.0    4.0  bar
# 1  2.0    6.0  bar
# 2  3.0    6.0  bar
# 3  4.0    4.0  bar

df['one_trunc'] = df['one'][:2]
print(df)

# one  three  foo  one_trunc
# 0  1.0    4.0  bar        1.0
# 1  2.0    6.0  bar        2.0
# 2  3.0    6.0  bar        NaN
# 3  4.0    4.0  bar        NaN

df.insert(1, 'bar', df['one'])
print(df)

# one  bar  three  foo  one_trunc
# 0  1.0  1.0    4.0  bar        1.0
# 1  2.0  2.0    6.0  bar        2.0
# 2  3.0  3.0    6.0  bar        NaN
# 3  4.0  4.0    4.0  bar        NaN

df = pd.read_csv('data.csv')
print(df)

#  Title1    Title2    Title3
# 0       one       two     three
# 1  example1  example2  example3