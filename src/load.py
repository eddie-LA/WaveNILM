import pickle
import numpy as np

filename = r'D:\WaveNILM\data\comparison\2020_12_08_1204\Loss_history.dat'

infile = open(filename,'rb')
data = pickle.load(infile)
infile.close()

'''
python def pretty(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            print('  ' * indent + str(key))
            pretty(value, indent+1)
        else:
            print('  ' * (indent+1) + f"{key}: {value}")
'''
i = 1
for dict in data:
    print(f"--------- RECORD {i} ---------")
    for key in dict:
        print(key.ljust(35), '->', np.around(dict[key], decimals=4))
    i+=1