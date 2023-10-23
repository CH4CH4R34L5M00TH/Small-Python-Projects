import sqlite3

class DatabaseManagementTool:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.connection.commit()

    def insert_data(self, table_name, data):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(data))})", data)
        self.connection.commit()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.connection.close()

def get_user_input(prompt):
    return input(prompt).strip()

# Example Usage
db_name = get_user_input("Enter the database name: ")
table_name = get_user_input("Enter the table name: ")
columns = get_user_input("Enter the column names and types (e.g., 'name TEXT, surname TEXT, email TEXT'): ")

db_tool = DatabaseManagementTool(db_name)
db_tool.create_table(table_name, columns)

# Get data for insertion
data = tuple(get_user_input("Enter the data to insert (e.g., 'Max, Mueller, max@gmail.com'): ").split(", "))

db_tool.insert_data(table_name, data)

query = get_user_input("Enter SQL query to execute: ")
result = db_tool.execute_query(query)
print(result)

db_tool.close_connection()
