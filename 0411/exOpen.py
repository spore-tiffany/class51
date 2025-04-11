

f = open("test.txt", 'w' )
f.write("test")
f.seek(0)
content = f.read()
print("content=",content)
f.close()