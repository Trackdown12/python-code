a={"e":2,"f":2,"c":3,4:45}
print(a,type(a))
print(a["e"])
print(a.items())#this provides the list of the key:value pair within a tuple
print(a.keys())
print(a.values())
a.update({"e":45,"A":454})#update the value of the key in argument & can add a new item
print(a)
print(a.get("e"))#returns the value of given key & return none if key doesn't exist