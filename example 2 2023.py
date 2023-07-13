import os
import pandas as pd
from metalpriceapi.client import Client


api_key = ''
client = Client(api_key)

result = client.timeframe(start_date='2023-05-05', end_date='2023-06-06', base='USD', currencies=['XAU'])   

new_row = pd.DataFrame(result['rates'])

result = new_row

result = result.transpose()

result = 1 / result

result.rename(columns={'XAU': 'GOLD'}, inplace=True)

# Format the prices with a dollar sign and two decimal places
result = result.applymap(lambda x: f'${x:.2f}')

# Save the DataFrame to a file if it's the first time running
if not os.path.isfile('metal_prices2023.csv'):
    result.to_csv('metal_prices2023.csv')
else:
    result.to_csv('metal_prices2023.csv', mode='a', header=False)
print(result)

