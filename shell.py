import os

def shell():
	while True:
		command = input("Enter a command: ")
		if command == "exit":
			break
		os.system(command)

if __name__ == "__main__":
	shell()