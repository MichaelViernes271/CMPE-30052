# author: Viernes, Michael E.
# yr/lvl: BSCOE 2-1
# objective: create a address book in which it can create, edit, delete, search, view and exit the program
    
    
# init lists
fname = []
lname = []
address = []
contact = []

def menu():
    print("ADDRESS BOOK".center(80, "="))
    menudisplay = \
    """\
What would you like to do?
1. Add Contact
2. Edit Contact
3. Delete Contact
4. View Contacts
5. Search Address Book
6. Exit
    """
    print(menudisplay)

def create(): # asks for user entries

    try:
        usr_fname = input("First name: ")
        usr_lname = input("Surname: ")
        usr_address = input("Address: ")
        usr_contact = int(input("Contact: "))
        
        fname.append(usr_fname)
        lname.append(usr_lname)
        address.append(usr_address)
        contact.append(usr_contact)
    except ValueError as e:
        print("Invalid Contact. Try again.\n")
    except Exception as e:
        print("Unexpected entry. Try again.")
    print("Added Successfully!\n")
    
def edit():
    idx = int(input("Select entry number to change: "))
    
    result = f"""
{idx:00}\t\t{fname[idx]}\t\t{lname[idx]}\t\t{contact[idx]}\t\t{address[idx]}
        """
    print("*"*80, "BEFORE CHANGE\n",result)
    
    try:
        usr_fname = input("First name: ")
        usr_lname = input("Surname: ")
        usr_address = input("Address: ")
        usr_contact = int(input("Contact: "))
        
        fname[idx] = usr_fname
        lname[idx] = usr_lname
        address[idx] = usr_address
        contact[idx] = usr_contact
    except ValueError as e:
        print("Invalid Contact. Try again.\n")
    except Exception as e:
        print("Unexpected entry. Try again.")
    
    result = f"""
{idx:00}\t\t{fname[idx]}\t\t{lname[idx]}\t\t{contact[idx]}\t\t{address[idx]}
        """
    print("*"*80, "\nAFTER CHANGE\n",result)
    print("Changed Successfully!\n")

def delete(idx): # delete by index
    if type(idx) is int:
        print(fname[idx],  lname[idx], contact[idx], address[idx],
        "\nDeleted Successfully.", "\n"*2)
        del fname[idx],  lname[idx], contact[idx], address[idx]
    else:
        print("There is no such entry. Try again.")
        
def view(): # display in table-like format
    print("No. First Name\tLast Name\tContact \tAddress\n", "*"*80)
    for idx in range(0, len(fname)):
        result = f"""\
{idx:2} {fname[idx]}\t\t{lname[idx]}\t\t{contact[idx]}\t\t{address[idx]}
        """
        print(result)

def search():
    print("""\
Options:
1. First Name
2. Last Name
3. Contact
4. Address
    """)
    idx = int(input("\nSelect Number: ")) 
    field = fname if idx == 1\
    else lname if idx== 2\
    else contact if idx == 3\
    else address if idx == 4 else 5
    
    searchfor = input("\nSearch for:")
    if searchfor in field:
        # change "idx" variable from options selection above into field index
        idx = field.index(searchfor)
        usr_fname = fname[idx]
        usr_lname= lname[idx]
        usr_contact = contact[idx]
        usr_address = address[idx]
        
        # print formatted results
        print("RESULT".center(80, "*"))
        result = "Name: {0} {1}\n\tPhone No.: {2}\n\tAddress: {3}"
        result = result.format(usr_fname, usr_lname, usr_contact, usr_address)
        print(result,"\n"*2)
    elif idx == 5: return "Invalid Option."

def main():

    while True:
        menu() # display actions for address book
        
        idx = (input("Choose action by number: "))
        
        if(idx == "1"): # create
            create()
        elif(idx == "2"): # edit
            edit()
        elif(idx == "3"): # delete
            usr_input = int(input("Delete by index: "))
            delete(usr_input)
        elif(idx == "4"): # view
            view()
        elif(idx == "5"): # search
            if not (len(lname) == 0):
                search()
            else:
                print("The book is empty. :(\n")
        elif(idx == "6"): # exit
            print("Closing...")
            exit()
        else:
            print("Select correct index.\n")

if __name__ == "__main__":
    main()