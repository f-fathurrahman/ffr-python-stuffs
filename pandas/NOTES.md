Data structures:
- Series
- DataFrame

Structured data -> stored in tables
CSV files, spreadsheets, database tables.

Unstructured data: free form text, images, sound, video

Single column of a DataFrame is returned as a Series.

`Index` object

index label: individual members of index
column name: individual members of columns

index and columns are collectively known as the axes

NaN (not a number): represent missing values

Several methods:

df.head()
df.head(10)

df.tail()
df.tail(10)

Column names:
df.columns

Index: (usually RangeIndex instance)
df.index

Accessing a column:
```python
df["column name"] # or
df.column_name
```

Accessing data:
```python
df.loc[:3,"col name"] # first four rows of column with column name `col name`
df.iloc[:3,1] # first four rows, 2nd column (idx=1)
```

df.head()["label name"]

Convert to numpy array:
dfnp = df.to_numpy()

```python
columns = df.columns
index = df.index
```


```python
type(columns)
type(index)
```

```python
print(columns.__class__)
```

df["column name"].value_counts()


data types:

df.dtypes
df.info()



Several Series methods and attributes:

.dtype
.size
.sample()
.value_counts()
.count()  # number of non-missing values
.mean()
.median()
.max()
.min()
.std()
.describe()
.quantile()
.isna()
.fillna()
.dropna()
.hasnans
.notna()