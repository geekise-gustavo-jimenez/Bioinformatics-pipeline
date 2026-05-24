import json
import pandas as pd
import matplotlib.pyplot as plt
import requests


def get_posts():
    url = "https://sabiork.h-its.org/export-api/sabio/kinlaw-entry/json/1"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
    
def main():
    posts = get_posts()

    if posts:
        # print(json.dumps(posts, indent=4))
        km_value = None
        kcat_value = None
        Et = 1.0

        for i in posts['kineticlaw']['parameter']:
            if i['name'] == 'Km':
                km_value = i['start_value']

            elif i['name'] == 'kcat':
                kcat_value = i['start_value']
        
        print(f"Success! Captured Km: {km_value} and kcat: {kcat_value}")
        vmax_value = kcat_value * Et
        print(f"Calculated Vmax: {vmax_value}")

        s_values = [i * 0.5 for i in range(21)]
        df = pd.DataFrame({'Substrate_Concentration': s_values})

        df['Velocity'] = (vmax_value * df['Substrate_Concentration']) / (km_value + df['Substrate_Concentration'])

        print(df.head())

        plt.figure(figsize=(8, 5))
        plt.plot(df['Substrate_Concentration'], df['Velocity'], marker='o', color='blue')

        plt.title('Enzyme Saturation Curve (SABIO-RK Data)')
        plt.xlabel('Substrate Concentration [S]')
        plt.ylabel('Reaction Velocity (v)')
        plt.grid(True)

        plt.show()

    else:
        print('Failed to fetch posts from API.')
    
    

if __name__ == '__main__':
    main()