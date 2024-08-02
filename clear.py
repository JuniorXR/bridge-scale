#!venv/bin/python
import os

for i in os.listdir():
	if i.endswith(".txt") or i.endswith(".pdf"):
		print("deleting:",i)
		os.remove(i)
print("program finished successfully!")
os.system("clear")
