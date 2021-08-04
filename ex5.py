my_name = 'Wenjingyi'
my_age = 26  # not a lie
my_height = 160  # cm
my_weight_kg = 80  # kg
my_weight_pound = 0.4536 * my_weight_kg
my_weight_pound = round(my_weight_pound)
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'brown'


print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight_kg} kg heavy.")
print(f"He's {my_weight_pound} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes } eyes and {my_hair} hair.")
print(f"He's teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight_pound
print(f"If I add {my_age}, {my_height}, and {my_weight_pound} I get {total}.")


