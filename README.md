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

### 3. UserUtil Class (Static Methods)
UserUtil class that provides utility functions.
- Static Methods:
generate_user_id(): Generates unique new user_id with 9 digits. The first two digits are taken from the current year ("24" for 2024). The remaining digits are randomly generated.
generate_password(): Generates new password. Minimum 8 characters long. At least 1 uppercase, 1 lowercase, 1 digit, and 1 special character.
is_strong_password(password): checks if a given password is at least 8 characters long and includes uppercase and lowercase letters, numbers, and special characters.
generate_email(name, surname, domain): Generates an email address using the user’s name and surname in lowercase.
validate_email(email) – Checks if the given email is in a valid format (e.g., follows the pattern name.surname@domain.com).

### 4. Unit Testing
TestUser, TestUserService, TestUserUtil classes that includes test cases for methods.
