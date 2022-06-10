import pandas as pd
import glob

df = pd.concat(map(pd.read_csv, glob.glob("data/*.csv")))
df.to_csv("data/compactData/data.csv")

f1 = pd.read_csv("data/compactData/data.csv", index_col= "product", converters={'price': lambda s: float(s.replace('$', ''))})

f1["sales ($)"] = f1["price"] * f1["quantity"]

f11 = f1.loc['pink morsel']

f11[['sales ($)', 'date', 'region']].to_csv("Task_2_pink_morsel_sales.csv", index=False)

solution = pd.read_csv('Task_2_pink_morsel_sales.csv') 

if __name__ == '__main__':

    print(f11)
    print(solution)

    pass
