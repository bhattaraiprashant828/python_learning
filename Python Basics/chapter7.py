# Chapter.7 File Input/Output(I/O) in Python.

# f=open("student.txt","r")
# data=f.read()
# print(data)
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)
# f.close()   


# f=open("student.txt","a")
# f.write("\nI will move to react.")
# f.write("\n After that I will move to node JS.")

# f.close()

# f=open("sample.txt","a")
# f.close()

# f=open("sample.txt","a+")  # Add from begining.
# f.write("abcde")           # No truncation.
# f.close()

# import os 

# os.remove("student.txt")  # Used to remove a file.

# f=open("practice.txt","r")
# data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)
# # f.write( '''Hi Everyone 
# # we are learning File I\O
# # using Java
# # I like programming in Java''')
# # with open("practice.txt","w") as f:
# #     f.write(new_data)
# word="learnings"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")
# f.close()