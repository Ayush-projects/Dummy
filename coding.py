# Really bad Python code with lots of issues



# Global variable (bad practice)
connection = None

def connect_to_db():
    global connection
    print("Connecting to database...")
    # Bad practice: hardcoding connection string with username and password in plaintext
    connection = f"Connected to DB with user: {USERNAME}, password: {PASSWORD}"
    print(connection)

def fetch_data(query):
    if not connection:
        connect_to_db()

    # Executing query without proper sanitization (SQL injection vulnerability)
    print(f"Running query: {query}")
    if query == "SELECT * FROM users":
        return [{"username": "admin", "password": "hashed_password"}]
    else:
        return []

def login(user_input):
    if user_input == USERNAME:
        print("Login successful!")  # Bad practice: No authentication handling
    else:
        print("Login failed!")  # Bad error message: doesn't specify what went wrong

# Function that doesn't return anything or handle errors
def main():
    query = "SELECT * FROM users"
    data = fetch_data(query)  # No proper error checking
    for row in data:
        print(f"Username: {row['username']}, Password: {row['password']}")  # Bad practice: Exposing sensitive data

# Hardcoded user input for login
user_input = "admin"

# Calling main function without checking if it's being imported as a module or script
login(user_input)
main()
