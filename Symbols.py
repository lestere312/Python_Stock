import glob
import json

gl = glob.glob('*_data.txt')
print(len(gl))
for i in range(0, len(gl)):
    f = open(gl[i], "r")
#     print(f.readline())
    string1 = f.read()
    print(json.loads(string1))
