# json
import json

dictData = {'name':'tom','age':33,'score':['90','80','100']}
print(dictData)

str_val = json.dumps(dictData)
print(str_val,type(str_val))
print(str_val[0:10])
#print(str_val['name']) string type

json_val = json.loads(str_val)
print(json_val,type(json_val)) 
#print(json_val[0:10])    dict 타입 슬라이싱 x
print(json_val['name'])
print(json_val['score'])

print()
for k in json_val.keys():
    print(k) #key 찍기
    
for v in json_val.values():
    print(v) #value 찍기
    
name_data = json_val.get('name')
print(name_data)