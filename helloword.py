#!/usr/bin/env python3

print('Hello World!')

f=open("sj.txt","w")
f.write("hello world")
f.close()

#read

f=open("sj.txt","r")
print(f.read())
