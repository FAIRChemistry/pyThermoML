import pandas as pd

# Prepare data
data={'Name':['Dhanashri', 'Smita', 'Rutuja',
              'Sunita', 'Poonam', 'Srushti'],
      'Age':[ 20, 18, 27, 50, 12, 15]}
  
# Load data into DataFrame
df = pd.DataFrame(data = data);
print(df)