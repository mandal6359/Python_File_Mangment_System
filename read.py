file = open("sample.txt", "r")
container = file.read()
file.close()
print(f"container of 'sample.txt':{container}")