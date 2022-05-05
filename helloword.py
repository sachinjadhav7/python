#!/usr/bin/env python3


f=open("mainpage.md","w")
f.write("hello world")
f.close()

#read

f=open("mainpage.md","r")
print(f.read())
