#  Chapter.4 Dictonary and Set in Python

# Dictonary
# info={
#     "name" : "PrAsHaNt",
#     "name" : "Prashant",
#     "learning" :"12th",
#     "age" :22,
#     "subjects" : ["Math","Physis","Biology","English"],
#     "marks" : (99,94,85,"fail"),
# }
# nullinfo= {}
# print(info)
# print(info["name"])
# print(info["age"])
# print(info["marks"])
# print(nullinfo)

# Nested Dictonary
# student={
#     "name" : "Prashant",
#     "subjects" : {
#         "Math": 99,
#         "Physis":94,
#         "Biology":85,
#         "English":"fail",
#     }
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["Biology"])
# print(list(student.keys()))
# print(list(student.values()))
# print(student.items())
# print(student.get("name"))
# new_dict={"city":"Kapilvastu"}
# student.update(new_dict)
# print(list(student.keys()))
# print(list(student.values()))


# Set in Python
# collection={1,2,3,4,5,6,7,1.9999,"hello","world"}
# print(type(collection))
# print(collection)
# print(len(collection))

# # Set Methods 
# collection.add("Prashant")
# print(collection)
# collection.remove("hello")
# print(collection)
# collection.add(0)
# print(collection)
# collection.remove("world")
# print(collection)
# collection.pop()
# print(collection)
# collection.clear()
# print(collection)

# Union and Intersection of Set.
# set1={1,2,3,4,5}
# set2={2,3,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))

# Practice.
# Q.1.Store following word meanings in py dictonary.
# dict={
#     "table":["a piece of furniture","list of facts and figures"],
#     "cat":["a small animal"]
# }
# dict.update({"dog": ["a loyal animal"]})
# print(dict)
# dict['cat'].append('parent of tiger')
# print(dict)

# Q.2
# subjects={"python","java","C++","python","javascript","java",'python',"java","C++","C"}
# print(subjects)
# print(len(subjects))

# Q.3. 
# nulldict={}
# s1=input("Enter the First Subject:")
# p=float(input(f"Enter the marks in {s1}"))
# nulldict.update({s1:p})
# s2=input("Enter the Second Subject:")
# c=float(input(f"Enter the marks in {s2}"))
# nulldict.update({s2:c})
# s3=input("Enter the Third Subject:")
# m=float(input("Enter the marks in maths"))
# nulldict.update({s3:m})

# # print(nulldict)
# set1=set()
# set1=set()
# set1.add(('float',9.0))
# set1.add(('int',9))
# print(set1)


 