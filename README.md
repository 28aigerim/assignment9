# User Class Methods 

### 1. User Class (Instance Variables and Methods
Class User that represents a user with the following attributes and methods:
- Instance Variables:
user_id (integer) – Unique identifier for the user.
name (string) – First name of the user.
surname (string) – Last name of the user.
email (string) – Email of the user.
password(string) – Password of the user.
birthday (datetime) – Birthday of the user.
- Methods:
__init__(self, user_id, name, surname, birthday): Initializes the user's details.
get_details(self): Returns a formatted string containing user details.
get_age(self): Computes and returns the user’s age.

##### Sample Input/Output
Code: user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
      print(user1.get_details())
Output: User Aibek Karypov with ID: 256895786.

Code: print(user1.get_age())
Output: User's age: 19


### 2. UserService Class (Class Methods & Class Attribute)
UserService class that manages users.
- Class Attribute:
users – A dictionary to store all User objects. key is the user_id, value is an User object.
- Class Methods:
add_user(cls, user): Adds a User object to users.
find_user(cls, user_id): Searches for a user by user_id and returns the user object if found.
delete_user(cls, user_id): Removes a user from users by user_id.
update_user(cls, user_id, user_update): Updates student attributes using user_update object arguments.
get_number(cls): Returns number of students in a users

##### Sample Input/Output
Code: print(UserService.add_user(user1))
Output: Successfully added new user.

Code: UserService.add_user(user1)
      print(UserService.find_user(user1.user_id))
Output: User: User Aibek Karypov with ID: 256895786.

Code: print(UserService.delete_user(user1.user_id))
Output: Successfully deleted the user.

Code: print(UserService.get_number())
Output: Number of students: 1.


### 3. UserUtil Class (Static Methods)
UserUtil class that provides utility functions.
- Static Methods:
generate_user_id(): Generates unique new user_id with 9 digits. The first two digits are taken from the current year ("24" for 2024). The remaining digits are randomly generated.
generate_password(): Generates new password. Minimum 8 characters long. At least 1 uppercase, 1 lowercase, 1 digit, and 1 special character.
is_strong_password(password): checks if a given password is at least 8 characters long and includes uppercase and lowercase letters, numbers, and special characters.
generate_email(name, surname, domain): Generates an email address using the user’s name and surname in lowercase.
validate_email(email) – Checks if the given email is in a valid format (e.g., follows the pattern name.surname@domain.com).

##### Sample Input/Output
(Only for sample check made the password public)
Code: user1.password = UserUtil.generate_password()
      print(user1.password)
Output: odz7AV[e

Code: print(UserUtil.is_strong_password('odz7AV[e'))
Output: The password is strong.

Code: user1.email = UserUtil.generate_email(user1.name, user1.surname, 'mail')
      print(user1.email)
Output: aibek.karypov@mail.kg

Code: print(UserUtil.validate_email('aibek.karypov@mail.kg'))
Output: The email is valid.


### 4. Unit Testing
TestUser, TestUserService, TestUserUtil classes that includes test cases for methods.
