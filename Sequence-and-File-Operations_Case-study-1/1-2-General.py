"""
1.What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4]) 
print(len(nums))
2.What will be the output?d ={"john":40, "peter":45}
print(list(d.keys()))
"""

nums =set([1,1,2,3,3,3,4,4]) 
print("1-The nums of list converting to set data type. Where set didn't have any duplicate values, so all repeted values \
      will be remove from the list. Then Final value will be set - (1,2,3,4) and lenght will be 4")

d ={"john":40, "peter":45}
print(d.keys())

print("2-The d is dictionry datatype, where it store the data in key values pairs. When we use key() method \
      for any dictionary it will return all associated keys in it. And output will be dict_keys(['john', 'peter']).")