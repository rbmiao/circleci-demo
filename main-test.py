# Import the Add function, 
# and assert that it works correctly

from main import Add

def TestAdd():
	assert Add(2,3) == 5
	assert Add(5,6) == 11
	assert Add(10, 9) == 19
	print("Add function works correctly")

if __name__ == '__main__':
	TestAdd()