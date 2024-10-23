main.py user 
def read_file (file_path: str, data dictionary )
users.json 
1 {
 
}


import json

file_path = 'users.json'
file_path = 'books.json'

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            read_data = f.write()
            if not read_data:
                return []
            return json.loads(write_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def user(name: str, ID: int) -> dict:
    return {
        "ID": ID,
        "name": name
    }

def write_file(file_path: str, data: dict):
    current_data = write_file(file_path)
    current_data.append(data)
    with open(file_path, 'w') as file:
        json.dump(current_data, file, indent=4)
    return 'reading Successfully'

# call user function
data_1 = user("Abdulhameed Yunusa", 1)
data_2 = user("Abdulhameed Yunusa", 2)
data_3 = user("Abdulhameed Yunusa", 3)
data_4 = user("Abdulhameed Yunusa", 4)

# read to file
read_file(file_path, data_1)
read_file(file_path, data_2)
read_file(file_path, data_3)
read_file(file_path, data_4)

read_data = read_file(file_path)
print(read_data)
 