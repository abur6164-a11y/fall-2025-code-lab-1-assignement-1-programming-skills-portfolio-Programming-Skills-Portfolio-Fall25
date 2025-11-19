# declearing variable name, hometown, and age
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# declearing age input to ensure it's an integer
while True:
	ageinput = input("Enter your age: ")
	try:
		age = int(ageinput)
		break
	except ValueError:
		print("Please enter your age as an integer.")

# Display the collected information
print(f"Name: {name}")
print(f"Hometown: {hometown}")
print(f"Age: {age}")
