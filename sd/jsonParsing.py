import json

#
# courses ='{"name": "AbhishekSharma","languages": [ "Java","Python"]}'
#
# dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses)
# print(dict_courses['name'])
#
# list_language = dict_courses['languages']
# print(type(list_language))
# print(list_language[1])
#
#
# print(dict_courses['languages'][0])

#***********************parse content present in json file


with open('C:\\Users\Abhishek.sharma\Desktop\\appli\json.txt')as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])