import os

def main():
    counter = 0
	while counter <=3:
		print("hello")
	counter = counter+1
	
	for i in range(0,counter):
		print("world!")
		
	printTest()
	print_another_test();
	
def printTest():
	print("test")
	

def print_another_test():
	print("another test")
	

if __name__=="__main__":
    main()