import pymongo

# Establishing connection with MongoDB
client = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
db = client["library"]
collection = db["books"]

# Function to add a book to the library
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    quantity = int(input("Enter the quantity of books: "))
    
    book = {"title": title, "author": author, "quantity": quantity}
    collection.insert_one(book)
    print("Book added successfully!")

# Function to display all books in the library
def display_books():
    books = collection.find()
    for book in books:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Quantity:", book["quantity"])
        print("----------")

# Function to update the quantity of a book
def update_book():
    title = input("Enter the title of the book: ")
    new_quantity = int(input("Enter the new quantity: "))
    
    collection.update_one({"title": title}, {"$set": {"quantity": new_quantity}})
    print("Book quantity updated successfully!")

# Function to delete a book from the library
def delete_book():
    title = input("Enter the title of the book: ")
    
    collection.delete_one({"title": title})
    print("Book deleted successfully!")

# Main menu
while True:
    print("\n----- Library Management System -----")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Update book quantity")
    print("4. Delete a book")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
