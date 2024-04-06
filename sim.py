from roller import roller
from roller2 import roller2
from roller3 import roller3
import pandas as pd
import math

pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", 100)

dice = [4, 6, 8, 10, 12, 20]
sides = [4, 6, 8, 10, 12, 20]
# rolls = 10**6
# rolls = 1

trials = []

for die in dice:
    for side in sides:
        rolls = math.floor(10 ** ((((die * side) - 16) / 384) * 3 + 5))
        # trials = []
        print("Rolling {2} sets of {0}d{1}".format(die, side, rolls))
        Roll = roller2(die, side, rolls)
        Roll.roll_sim()
        trials.append(["{0}d{1}".format(die, side), Roll.hands])

flattened_data = [
    (dice_set, hand, count) for dice_set, hands in trials for hand, count in hands
]

df = pd.DataFrame(flattened_data, columns=["Dice Set", "Hand", "Count"])
df = df.pivot(columns="Dice Set", index="Hand", values="Count")
df = df.fillna(0)

# df = df[["6d6", "6d8", "6d12", "8d6", "8d8", "8d12"]]
df = df.sort_values(df.columns[0], axis=0, ascending=False)
# df = df.reindex(["High", "2", "22", "3", "Straight", "32", "4", "5"])
# df = (df.div(df.sum(axis=0), axis=1) * 100).round(2)

# df.loc[:, "Percentage"] = (df.div(df.sum(axis=0), axis=1) * 100).round(2)

print(df)
df.to_csv("{2}_{0}d{1}.csv".format(dice[-1], sides[-1], rolls))
