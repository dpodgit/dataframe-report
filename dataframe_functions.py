import numpy as np
import pandas as pd

def report(df):
   feature_types = {df[df.columns[x]].dtypes.name for x in range(len(df.columns))}

   print('DATATYPES:\n{}\n\n'.format(df.dtypes))
   print('_'*50)

   print('ROWS, COLUMNS, NULLS')
   print(df.shape[0], "rows in dataframe.")
   print(df.shape[1], "rows in dataframe")
   print('{} nulls values in dataframe\n\n'.format(df.isnull().sum().sum()))

   print('_'*50)

   print('DUPLICATES') 
   duplicate_rows = df.duplicated(keep=False).sum() 
   duplicate_cols = df.index.T.duplicated(keep=False).sum()
   print("{} duplicate rows in dataframe.".format(duplicate_rows))
   print("{} duplicated columns in dataframe".format(duplicate_cols))

   if duplicate_rows > 0 or duplicate_cols > 0:
      print(df.loc[df.duplicated()])
   
   print('\n\n')
   print('_'*50)

   print('CONSTANT COLUMNS')

   numeric_cols = list(df.select_dtypes(include=[np.number]).columns.values)
   category_cols = list(df.select_dtypes('category').columns.values)

   standard_diffs = [df.describe().loc['std', x] for x in numeric_cols]

   constant_categ_col=False
   if 'category' in feature_types:
      for column in category_cols:
         if df[column].describe().index.unique == 1:
            constant_categ_col=True

   if (0 in standard_diffs):
      print('Constant numeric column(s): TRUE')
   else:
      print('Constant numeric column(s): FALSE ')

   if 'category' in feature_types:
      if constant_categ_col == True:
         print('Constant categorical column(s): TRUE')
      else:
         print('Constant categorical column(s): FALSE')
   else:
      print('No categorical columns')
   
   print('\n\n')
   print('_'*50)

   # stats

   print('NUMERIC DESCRIPTION')
   print(df.describe().T)
   print('\n\n')
   print('_'*50)

   # categorical stats

   if 'category' in feature_types:
      print('CATEGORICAL DESCRIPTION\n')
      print(df.select_dtypes(['category']).describe().T)
      print('\n\n')
      print('_'*50)

   # cardinalities

   col_names = list(df.columns.values)
   print('FEATURE CARDINALITIES\n')
   print('{0:45} {1}'.format("Feature", "Distinct Values"))
   print('{0:45} {1}'.format("-------", "---------------"))

   for c in col_names:
      print('{0:45} {1}'.format(c, str(len(df[c].unique()))))
   print('\n\n')
   print('*'*50)

   print('MEMORY')
   print('{}\n'.format(df.info(memory_usage='deep')))
   print('{}\n\n'.format(df.memory_usage(deep=True)))
   print('_'*50)

   # preview
   print('HEAD\n{}\n\n'.format(df.head(10)))
   print('TAIL\n{}'.format(df.tail(10)))




