import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    site_name = get_user_input("Enter the password name for the site: ")

    output_file = f"{site_name}.txt"  # Automatically appends .txt

    length = 12  # You can adjust the length of the generated password if needed
    password = generate_password(length)

    with open(output_file, 'w') as file:
        file.write(f"Site Name: {site_name}\n")
        file.write(f"Generated Password: {password}\n")

    print(f"Password for '{site_name}' generated and saved in '{output_file}'")

if __name__ == "__main__":
    main()
