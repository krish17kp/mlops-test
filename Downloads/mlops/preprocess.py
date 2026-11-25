import pandas as pd;
from sklearn.preprocessing import MinMaxScaler, StandardScaler;
df=pd.read_csv('data.csv'); 
df=df.dropna();
X=df.select_dtypes(include='number');
print('Original Data:\n',X.head()); 
print('\nMin-Max Scaling:\n',MinMaxScaler().fit_transform(X)); 
print('\nStandardization:\n',StandardScaler().fit_transform(X))"