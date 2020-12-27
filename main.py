import pandas as pd
import numpy as np

from functions.transformations import *

df = pd.read_excel("Data.xlsx").fillna("")

# Begin transformations
df['FullName'] = df.apply (lambda row: create_fullName(row['FirstName'], row['LastName'], row['MiddleName']), axis=1)
df['Age'] = df.apply (lambda row: calculate_age(row['DateOfBirth']), axis=1)
