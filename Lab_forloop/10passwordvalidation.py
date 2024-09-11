import re

# Function to check password validity
def is_valid_password(password):

    """Check if the password meets the basic criteria."""
    
    # Check all criteria in one line only
    if (len(password) < 8 or  # Password must be at least 8 characters long
        not re.search(r'[A-Z]', password) or  # Must contain at least one uppercase letter
        not re.search(r'[a-z]', password)):  # Must contain at least one lowercase letter
        return "Password must be at least 8 characters long and contain both uppercase and lowercase letters."
    
    return "Password is valid."

# Main function to get user input and validate password
def main():
    
    """Prompt user for password and check its validity."""

    #We have to feed password from our end to check validity

    password = input("Enter your password: ")
    

    # Print the result of password as validity check

    print(is_valid_password(password))

if __name__ == "__main__":
    main()
    
