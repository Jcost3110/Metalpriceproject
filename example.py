import os
import pandas as pd
from metalpriceapi.client import Client



api_key = ''
client = Client(api_key)

result = client.fetchLive(base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
    
new_row = pd.DataFrame(result['rates'], index=[0])

result = new_row

result = 1 / result

result = result.rename(columns={'XAU': 'Gold', 'XAG': 'Silver', 'XPD': 'Palladium', 'XPT': 'Platinum'})

# Format the prices with a dollar sign and two decimal places
result = result.applymap(lambda x: f'${x:.2f}')

# Save the DataFrame to a file if it's the first time running
if not os.path.isfile('metal_prices.csv'):
    result.to_csv('metal_prices.csv')
else:
    result.to_csv('metal_prices.csv', mode='a', header=False)
print(result)

