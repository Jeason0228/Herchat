import pandas as pd

def parse_excel(file):
    df = pd.read_excel(file, dtype=str)
    person_list = []
    for index, row in df.iterrows():
        # print(row)
        person_list.append(row.to_dict())
    return person_list, df