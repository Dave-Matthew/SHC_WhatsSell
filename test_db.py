import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('shc_ws.db')

# Create a cursor object
cursor = connection.cursor()

# # Insert dummy data into Users table
# cursor.execute("INSERT INTO Users (phone_number) VALUES ('123-456-7890')")
# cursor.execute("INSERT INTO Users (phone_number) VALUES ('098-765-4321')")
# cursor.execute("INSERT INTO Users (phone_number) VALUES ('555-555-5555')")

# # Insert dummy data into Items table
# cursor.execute("INSERT INTO Items (user_id, name, price, condition, short_description, description, status) VALUES (1, 'Product A', 10.0, 'new', 'Short description A', 'Description A', 'open')")
# cursor.execute("INSERT INTO Items (user_id, name, price, condition, short_description, description, status) VALUES (2, 'Product B', 20.0, 'used', 'Short description B', 'Description B', 'open')")
# cursor.execute("INSERT INTO Items (user_id, name, price, condition, short_description, description, status) VALUES (3, 'Product C', 30.0, 'refurbished', 'Short description C', 'Description C', 'open')")

# # Insert dummy data into Item_Images table
# cursor.execute("INSERT INTO Item_Images (item_id, image_url) VALUES (1, 'http://example.com/image1.jpg')")
# cursor.execute("INSERT INTO Item_Images (item_id, image_url) VALUES (2, 'http://example.com/image2.jpg')")
# cursor.execute("INSERT INTO Item_Images (item_id, image_url) VALUES (3, 'http://example.com/image3.jpg')")

# # Insert dummy data into Orders table
# cursor.execute("INSERT INTO Orders (item_id, buyer_id, quantity, total_price) VALUES (1, 1, 2, 20.0)")
# cursor.execute("INSERT INTO Orders (item_id, buyer_id, quantity, total_price) VALUES (2, 2, 1, 20.0)")
# cursor.execute("INSERT INTO Orders (item_id, buyer_id, quantity, total_price) VALUES (3, 3, 5, 150.0)")



# Commit the changes
connection.commit()

# Execute a SQL query to select all rows from the Orders table
cursor.execute("SELECT * FROM Items")

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Iterate through the rows and print them
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()

# -- Create Users Table
# CREATE TABLE Users (
#     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     phone_number TEXT NOT NULL UNIQUE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Create Items Table
# CREATE TABLE Items (
#     item_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     name TEXT NOT NULL,
#     price REAL NOT NULL,
#     condition TEXT NOT NULL CHECK (condition IN ('new', 'used', 'refurbished')),
#     short_description TEXT NOT NULL CHECK (length(short_description) <= 100),
#     description TEXT,
#     status TEXT NOT NULL CHECK (status IN ('open', 'modified', 'sold')),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
# );

# -- Create Item_Images Table
# CREATE TABLE Item_Images (
#     image_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     item_id INTEGER NOT NULL,
#     image_url TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (item_id) REFERENCES Items(item_id) ON DELETE CASCADE
# );

# -- Create Orders Table
# CREATE TABLE Orders (
#     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     item_id INTEGER NOT NULL,
#     buyer_id INTEGER NOT NULL,
#     purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     quantity INTEGER NOT NULL DEFAULT 1,
#     total_price REAL NOT NULL,
#     FOREIGN KEY (item_id) REFERENCES Items(item_id),
#     FOREIGN KEY (buyer_id) REFERENCES Users(user_id)
# );