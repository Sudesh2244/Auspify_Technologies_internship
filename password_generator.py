import random
import string

def generate_password(length):
    """Generates a secure password based on provided length."""
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random choices and join into a string
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("--- Secure Password Generator ---")
    
    while True:
        try:
            # Step 1: Take password length as input
            length = int(input("\nEnter desired password length: "))
            
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            
            # Step 2, 3, & 4: Generate and display password
            password = generate_password(length)
            print(f"Generated Password: {password}")
            
            # Step 5: Allow users to generate multiple passwords
            again = input("\nGenerate another password? (y/n): ").lower()
            if again != 'y':
                print("Exiting. Happy coding!")
                break
                
        except ValueError:
            print("Invalid input! Please enter a numeric value for the length.")

if __name__ == "__main__":
    main()