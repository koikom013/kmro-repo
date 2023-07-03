#Test

import pandas as pd

#create test DF

df = pd.DataFrame(columns=['col a','col b'])

df.to_csv('data/test_db.csv',index=False)