#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string

def generate_password(length=12):
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)


# In[ ]:




