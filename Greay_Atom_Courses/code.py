# --------------
# Code starts here
#Intruction
# Create a 'class_1' list and pass the elements 'Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio'.
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
#Create a 'class_2' list and pass the elements 'Hilary Mason','Carla Gentry','Corinna Cortes'.
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
#Concatenate the 'class_1' and 'class_2' list. Store the values in a'new_class' variable.
new_class = class_1 + class_2
print(new_class)
#Add new element 'Peter Warden' in the 'new_class' list.
new_class.append('Peter Warden')
#Print 'new_class' to see the updated list.
print(new_class)
# Remove the 'Carla Gentry'element from the 'new_class' list.
new_class.remove('Carla Gentry')
#Print 'new_class' to see the updated list.
print(new_class)
# Code ends here


# --------------
# Code starts here
courses = {"Math": 65, "English": 70, "History": 80, "French": 70, "Science": 60}
total = courses["Math"] + courses["English"] + courses["History"] + courses["French"] + courses["Science"]
print(total)
addition = 500
percentage = total / addition *100
print(percentage)
print("percentage scored by Geoffrey Hinton is", percentage)
# Code ends here


# --------------
# Code starts here
mathematics  = {"Geoffrey Hinton": 78, "Andrew Ng": 95, "Sebastian Raschka": 65, "Yoshua Benjio": 50, "Hilary Mason": 70, "Corinna Cortes": 66, "Peter Warden": 75}
topper = max(mathematics, key = mathematics.get)
print(topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
first_name, last_name = topper.split()[0], topper.split()[1]
full_name = last_name + " " + first_name
certificate_name = full_name.upper()
print(certificate_name)
# Code starts here



# Code ends here


