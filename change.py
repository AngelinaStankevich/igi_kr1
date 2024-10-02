from collections import ChainMap

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

combined_dict = dict(ChainMap(dic1, dic2, dic3))

print(combined_dict,)
