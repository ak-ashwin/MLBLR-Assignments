import json
import random
import re

import pandas as pd

indices_set = []
values_set = []
source_data = ''
with open('data/mlblr2a.json') as f:
    data = json.load(f)
    cell_type_data = data['cells']

    for i, subset in enumerate(cell_type_data):
        if (subset['cell_type'] == "code"):
            source_data = subset['source']
            for i, s in enumerate(source_data):
                if ' = ' in s:
                    values_set.append(s)

            indices = [i for i, s in enumerate(source_data) if ' = ' in s]
            indices_set.append(indices)

df = pd.DataFrame({'col': values_set})
df['col'] = df['col'].str.split(' = ', expand=True)
df['col'] = df['col'].str.split('[', expand=True)
df['col'] = df['col'].str.strip()

unique_values = df['col'].unique().tolist()
# print(unique_values)

list_vars = ['eip', 'mlblr', 'eip_in', 'eip_out', 'mlblr_in', 'mlblr_out', 'eip_list', 'eip_dict']
unique_values = ['pivot', 'left', 'middle', 'right', 'x', 'y', 't', 'f', 'hello', 'world', 'hw', 'hw12', 's', 'xs',
                 'nums', 'animals', 'squares', 'even_squares', 'd', 'legs', 'even_num_to_square', 'self.name', 'g', 'a',
                 'b', 'c', 'e', 'row_r1', 'row_r2', 'col_r1', 'col_r2', 'bool_idx', 'v', 'w', 'vv', 'img', 'img_tinted',
                 'y_sin', 'y_cos']

print(df)
print(indices_set)






for val in unique_values:
    # newval = r'\b{0}\b'.format(val)
    newval = r"\b" + (val) + r"\b"
    # newval = r"\bpivot\b"
    print(newval)

    # Read in the file
    with open('data/new.json', 'r') as file:
        filedata = file.read()

    newdata = re.sub(newval, random.choice(list_vars), filedata)

    with open('data/new.json', 'w') as file:
        file.write(newdata)
