import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            messagebox.showinfo("List Books", "No books found.")
        else:
            book_list = "\n".join(books)
            messagebox.showinfo("List Books", book_list)

    def add_book(self):
        book_title = simpledialog.askstring("Add Book", "Enter book title:")
        book_author = simpledialog.askstring("Add Book", "Enter book author:")
        release_year = simpledialog.askstring("Add Book", "Enter first release year:")
        num_pages = simpledialog.askstring("Add Book", "Enter number of pages:")

        if book_title and book_author and release_year and num_pages:
            book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
            self.file.write(book_info)
            messagebox.showinfo("Add Book", "Book added successfully.")
        else:
            messagebox.showerror("Add Book", "Please fill in all fields.")

    def remove_book(self):
        title_to_remove = simpledialog.askstring("Remove Book", "Enter the title of the book to remove:")
        self.file.seek(0)
        books = self.file.read().splitlines()

        updated_books = [book for book in books if title_to_remove not in book]

        self.file.seek(0)
        self.file.truncate()

        for book in updated_books:
            self.file.write(book + '\n')

        messagebox.showinfo("Remove Book", f"Book '{title_to_remove}' removed successfully.")

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.library = Library()

        # Adding a background image
        background_image = Image.open("background.png")
        [imageSizeWidth, imageSizeHeight] = background_image.size
        n = 0.25
        newImageSizeWidth = int(imageSizeWidth * n)
        newImageSizeHeight = int(imageSizeHeight * n)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)
        img = ImageTk.PhotoImage(background_image)
        canvas = tk.Canvas(root)
        canvas.create_image(300, 340, image=img)
        canvas.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
        canvas.pack(expand=True, fill=tk.BOTH)

        heading_frame = tk.Frame(root, bg="#120aab", bd=5)
        heading_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        heading_label = tk.Label(heading_frame, text="Library Management System", bg='black', fg='white', font=('Courier', 24))
        heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.list_button = tk.Button(root, text="List Books", command=self.library.list_books)
        self.list_button.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

        self.add_button = tk.Button(root, text="Add Book", command=self.library.add_book)
        self.add_button.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

        self.remove_button = tk.Button(root, text="Remove Book", command=self.library.remove_book)
        self.remove_button.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

        self.exit_button = tk.Button(root, text="Exit", command=self.root.destroy)
        self.exit_button.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

# Create the main window
root = tk.Tk()
app = LibraryGUI(root)
root.mainloop()
