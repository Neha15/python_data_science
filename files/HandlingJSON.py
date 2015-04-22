import json 

file_path = open('/home/prodapt/PythonExercise/jsonfile.json')   
data = json.load(file_path)
jsondata = json.dumps(data, sort_keys=True, indent=4)
print jsondata
print data['two']['list'][1]['item']