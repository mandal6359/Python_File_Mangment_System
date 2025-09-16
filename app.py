import os      




def create_file(filename):  
    try:   
        with open(filename,"x") as f: 
            print(f"File name {filename} create suscefully..") 
    except FileExistsError:     
        print("Alerady file created ")
    except Exception as e:
        print("something is wrong.. ")



def view_all_files():
    files = os.listdir()
    if not files:
        print("Not file in this system..")
    else:
        print("Files in directory..")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted..")
    except FileNotFoundError:
        print("file dosent exits..")
    except Exception as e:
        print ("Something Error !!")


def read_file(filename):
    try:
        with open("sample.txt","r") as f:
            content = f.read()
            print(f"Content of '{filename}' : \n{content}")
    except FileNotFoundError:
        print("File Not Foundd..")
    except Exception as e:
        print("Something Error Found!!")

def edit_file(filename):
    try:
        with open("sample.txt","a") as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f"File added {filename} Sucessfully ..")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Something error ..!")



def main():
    while True:
        print("FILE MANAGMENT APP")
        print("1: Create a file")
        print("2: View all file")
        print("3: Delete a file")
        print("4: Read a file")
        print("5: Edit a file")
        print("6: EXIT")

        choice =input("Enter your choice (1-6) = ")
        if choice == "1":
            filename = input("Enter the file-name to create = ")
            create_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            filename = input("Enter the file-name to delete = ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter the file-name to read = ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the file-name to edit = ")
            edit_file(filename)
        elif choice == "6":
            print("Closing the App...")
            break
        else:
            print ("Invalid input !!")
if __name__ == "__main__":
    main()

