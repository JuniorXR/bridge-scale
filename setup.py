def cloneGitRepo():
	try:
		from os import system
		
		system("git clone https://github.com/JuniorXR/junior")
		del system
	except Exception as e:
		print(e)

if __name__ =='__main__':
	cloneGitRepo()