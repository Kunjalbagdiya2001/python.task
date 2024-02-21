d={876:"kunjal",890:"mansi",765:"Humza",564:"parthiv",456:"Rahul"}


print(d)
print(d[564])
print(d.get(456))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(890))
print(d)
d1={333:"mans",444:"Taksh"}
d.update(d1)
print(d)
d.popitem()
print(d)

for i in d:
    print(i,":",d[i])
