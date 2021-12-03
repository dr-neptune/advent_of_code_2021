# quick and dirty, will update when I'm less busy
import pandas as pd

# IO
with open('input.txt') as f:
    diag = f.read().splitlines()

# part 1
# pandas version
diags = []
for d in diag:
    diags.append([c for c in d])

df = pd.DataFrame(diags)

vals = []
for col in df:
    vals.append(df[col].value_counts().index.tolist())

decimal_output = int("".join([i[0] for i in vals]), 2)
decimal_output2 = int("".join([i[1] for i in vals]), 2)

decimal_output * decimal_output2

# part 2
# Oxygen Generator Rating
df2 = df
for col in df2:
    mode = df2[col].mode().tolist()
    mode = mode[0] if len(mode) == 1 else "1"
    df2 = df2[df2[col] == mode]

decimal_output = int("".join(df2.values[0]), 2)

# CO2 Scrubber Rating
df2 = df

for col in df2:
    if len(df2) == 1:
        break
    match df2[col].mode().tolist():
        case ['1']:
            mode = "0"
        case['0']:
            mode = "1"
        case [a, b]:
            mode = "0"
    df2 = df2[df2[col] == mode]

decimal_output2 = int("".join(df2.values[0]), 2)

decimal_output * decimal_output2
