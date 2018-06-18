from __future__ import print_function

import numpy as np
import pandas as pd

# A Pandas `Series` is 1-D array of indexed data
# It can be created from a list or array
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

# access data just like in NumPy array:
print("data.values = ", data.values)
print(data[1])
print(data[1:3])

# also the index
print("data.index = ", data.index)

# Index can be values of any desired type
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])

print(data['b'])

print("data.index = ", data.index)

# Using noncontiguous or nonsequential indices
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])

print("data.index = ", data.index)
print(data[5])

# `pd.Series` can also be constructed directly from Python `dict`
population_dict = {"California" : 38332521,
                   "Texas" : 26448193,
                   "New York" : 19651127,
                   "Florida" : 19552860,
                   "Illinois" : 12882135}
population = pd.Series(population_dict)
print(population)

print(population.values)
print(population.index)

# `Series` supports array-style operations such as slicing
print(population["California":"Illinois"])

# Index can be explicitly set if a different result is preferred
print( pd.Series( {2:"a", 1:"b", 3:"c"}, index=[3,2]) )

#
# DataFrame
#

# Data frame is an analog of a two-dimensional array with both flexible row indices and
# flexible column names. We can think of a DataFrame as a sequence of aligned Series
# objects.

area_dict = {"California" : 423967, "Texas" : 695662, "New York" : 141297,
             "Florida" : 170312, "Illiois" : 149995}
area = pd.Series(area_dict)

states = pd.DataFrame( {"population" : population,
                        "area" : area} )
print(states)
print(states.index)
print(states.columns)

