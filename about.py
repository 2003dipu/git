# a variable= is a reusable container for storing value
# a variable behaves as if it were the value it contains
Name = "Mike"
age = "23"
print("There once was a man named " + Name + ".")
print("He was " + age + " years old.")
name = "Steve"
age = "50"
print(f"He really liked the name {name}")
print(f"But he did not like being {age}")
print(f'His friends liked the name {name}')
teacher_name = "Bro Code"
print(f"His teacher {teacher_name} inspired him to learn to code.")
age = 21
print("You are " + str(age) + " years old.")
print("You are", age, "years old.")
# using f string to print something which is the most popular function now.
print(f"You are {age} years old")
# integers are whole numbers like 1,2,3 etc.
age = 20
players = 98456
quantity = 5
print(f"You are {age} years old")
print(f"There are {players} players online on the lichess app")
print(f"I'd like to buy {quantity} items.")


# float is a decimal number
GPA = 4.01
distance = 9.8
price = 84000
print(f"Your GPA is {GPA}")
print(f"I ride bycycle {distance} km each day to home-tutor")
print(f"Your price is ${price}")
# string
name = "Dipu"
food = "Jackfruit"
email = "hunabopa@gmail.com"
print(f"Your name is {name}")
print(f"You like  {food}")
print(f"Your email is {email}")

# boolean
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar

    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
zork = 0
print('Before',zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
