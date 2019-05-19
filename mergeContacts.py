#!/usr/bin/env python
# coding: utf-8

# ## Merge a list of contacts by phone or email (similar to feature you have in phones)
# 
# ###  Given
# 
# [{Name:'Mr. X', phone:'123-456-7890', email: 'x@yieldmo.com'},
# 
# {Name:'Ms. Y', phone:'456-789-1234', email: 'y@yieldmo.com'},
# 
# {Name:'Mr. X1', phone:'123-456-7890', email: 'x@gmail.com'},
# 
# {Name:'Ms. Y1', phone:'456-789-9999', email: 'y@yieldmo.com'}]
# 
# ###  Return:
# 
# [
# [{Name:'Mr. X', phone:'123-456-7890', email: 'x@yieldmo.com'},{Name:'Mr. X1', phone:'123-456-7890', email: 'x@gmail.com'}],
# 
# [{Name:'Ms. Y', phone:'456-789-1234', email: 'y@yieldmo.com'},{Name:'Ms. Y1', phone:'456-789-9999', email: 'y@yieldmo.com'}]
# ]
# 
# ### Function Signature
# 
# class Contact(name: String, phone: String, email: String)
# 
# def mergeUsers(contacts: List[Contact]): List[List[Contact]]

# ---------------------------------------------------------------------------------------------------
# # Solution...
# 
# ### At first we will define a class by name `Contact`. This class basically represents the structure to hold user contact
# 
# `class Contact(name: String, phone: String, email: String)`



class Contact():
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


# ## Below we will define a function `mergeUser`. This function takes as input the list of contacts and merges together the contacts with same `phone` or `email` as a new list . It returns the list of list of contacts .
# 
# Function Signature:
# 
# `def mergeUsers(contacts: List[Contact]): List[List[Contact]]`



def mergeUsers(contacts):
    if isinstance(contacts, (list,)):
        
        dup_contacts = contacts.copy()

        merged_contacts_list = []

        for contact in contacts:

            contact_list = []
            contact_list.append(contact)

            for dup_contact  in dup_contacts:
                if (contact != dup_contact) and (contact.phone == dup_contact.phone or contact.email == dup_contact.email):
                    contacts.remove(dup_contact)
                    contact_list.append(dup_contact)
            merged_contacts_list.append(contact_list)
        
    return merged_contacts_list


# ### We will then create a list of contacts and call the function `mergeUsers` by passing this list of contacts as input. The function returns another list , which we will print to see if it indeed returned the list of lists. 
# 
# ### Given the list of lists contain objects of type `Contact`, we will print the variables that forms the object to visualize the output 



if __name__ == "__main__":
    contacts = [Contact("Mr. X", "123-456-7890", "x@yieldmo.com"),Contact('Mr. Y', '456-789-1234', 'y@yieldmo.com')
               ,Contact("Mr. X1", "123-456-7890", "x@gmail.com"),Contact('Mr. Y1', '456-789-9999', 'y@yieldmo.com')]


    merged_contacts_list  = mergeUsers(contacts)
    print("Printing list of list of objects...")
    print("--------------------------")
    print(merged_contacts_list)

    print("\n")

    print("\n")

    print("Visualizing the output....")
    print("--------------------------")
    print("[")
    for i in range(len(merged_contacts_list)):
        print("[")
        for j in range(len(merged_contacts_list[i])):
            print(merged_contacts_list[i][j])
        print("]")

    print("]")





