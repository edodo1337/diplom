import pandas as pd



a = {
  '1': (2, 4, 8),
  '2': (4, 8, 16)
}

b = {
  '1': (3, 9, 27),
  '2': (6, 18, 54)
}



from itertools import chain


d_values = [i.values() for i in [a,b]]

x1 = [i[0] for i in chain(*d_values)]
x2 = [i[1] for i in chain(a.values(), b.values())]
x3 = [i[2] for i in chain(a.values(), b.values())]


data = {
  'first': x1,
  'second': x2,
  'third': x3,
}

df = pd.DataFrame(data)
print(df)