# %%
import pandas as pd
import re
from collections import Counter

# %%
df = pd.read_csv('input.txt', sep=" ", header=None)
    
# %%
df.columns = ["original"]


# %%
df[["letter", "number", "nothing"]] = df.apply(lambda s: re.split(r'(\d+)', s["original"]), axis=1, result_type="expand")

# %%
df.drop(columns=["nothing"], inplace=True)

# %%
dial_ticks = list(range(0,100))

# %%
class BidirectionalIterator:
    def __init__(self, collection, start):
        self.collection = collection
        self.index = start
        self.length = len(collection)
        self.current_value = collection[start]

    def right(self, amount):
        self.index += amount
        if self.index >= self.length:
            self.index = self.index - self.length
        self.current_value = self.collection[self.index]
        return self.current_value

    def left(self, amount):
        self.index -= amount
        if self.index < -self.length:
            self.index = self.index + self.length
        self.current_value = self.collection[self.index]
        return self.current_value

    def current(self):
        return self.current_value

    def __iter__(self):
        return self
    
# %%
dial = BidirectionalIterator(dial_ticks, 50)

# %%
dial.current()

# %%
dial.right(50)

# %%
dial.left(24)

# %%
