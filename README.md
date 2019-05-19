# yieldmo_mergeContacts
I have put together here a Python code to merge a list of contacts by phone or email. Given a list of contacts, where each contact is of type class `contact` with propeties 'name', 'phone' and 'email'.  The code will merge the contacts by phone or email (similar to feature you have in phones).

  Given

  [{Name:'Mr. X', phone:'123-456-7890', email: 'x@yieldmo.com'},

  {Name:'Ms. Y', phone:'456-789-1234', email: 'y@yieldmo.com'},

  {Name:'Mr. X1', phone:'123-456-7890', email: 'x@gmail.com'},

  {Name:'Ms. Y1', phone:'456-789-9999', email: 'y@yieldmo.com'}]

  Return:

  [ [{Name:'Mr. X', phone:'123-456-7890', email: 'x@yieldmo.com'},{Name:'Mr. X1', phone:'123-456-7890', email: 'x@gmail.com'}],

  [{Name:'Ms. Y', phone:'456-789-1234', email: 'y@yieldmo.com'},{Name:'Ms. Y1', phone:'456-789-9999', email: 'y@yieldmo.com'}] ]

# Pre Requisites
You will need python 3.7 . You can download python from here
https://www.python.org/downloads/

You will also need Git Client. You can download it from here
https://git-scm.com/downloads

# Understand the code
To know more about how this code merges the contacts, please refer to the jupyter notebook [here](
https://github.com/harithatavarthy/yieldmo_mergeContacts/blob/master/mergeContacts.ipynb)


# How to run this code

a. Run the command `git clone https://github.com/harithatavarthy/yieldmo_mergeContacts.git`

b. Run the command `mkdir yieldmo_mergeContacts`

c. Run the command `python mergeContacts.py`

You will see the output at the terminal

