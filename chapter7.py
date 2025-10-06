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

f=open("sample.txt","r+")  # Overwrite from begining.
f.write("abcde....z")      # also truncate previous.
f.close()