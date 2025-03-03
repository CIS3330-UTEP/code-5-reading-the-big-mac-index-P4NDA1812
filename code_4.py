import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    
    country_code = country_code.upper()
    df['year'] = df['date'].str[:4]
    price = df[(df['year'] == str(year)) & (df['iso_a3'] == country_code)]['dollar_price'].mean()
    return round(price, 2)

def get_big_mac_price_by_country(country_code):
    
    country_code = country_code.upper()
    price = df[df['iso_a3'] == country_code]['dollar_price'].mean()
    return round(price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    
    df['year'] = df['date'].str[:4]
    
    year_data = df[df['year'] == str(year)]
    
    cheapest_row = year_data.loc[year_data['dollar_price'].idxmin()]
   
    country_name = cheapest_row['name']
    country_code = cheapest_row['iso_a3']
    dollar_price = cheapest_row['dollar_price']
    
    result = f"{country_name}({country_code}): ${dollar_price:.1f}"
    return result

def get_the_most_expensive_big_mac_price_by_year(year):
    
    df['year'] = df['date'].str[:4]
    
    year_data = df[df['year'] == str(year)]
    
    most_expensive_row = year_data.loc[year_data['dollar_price'].idxmax()]
    
    country_name = most_expensive_row['name']
    country_code = most_expensive_row['iso_a3']
    dollar_price = most_expensive_row['dollar_price']
        
    result = f"{country_name}({country_code}): ${dollar_price:.1f}"
    return result

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2005,"usa"))
    print(get_big_mac_price_by_country("usa"))
    print(get_the_cheapest_big_mac_price_by_year(2005))
    print(get_the_most_expensive_big_mac_price_by_year(2005))