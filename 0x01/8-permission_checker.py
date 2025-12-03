#!/usr/bin/python

def check_permission(user_permission, required_permission):
    if user_permission & required_permission:
        return  "Access granted"
    else:
        return "Access denied"
    

if __name__ == "__main__":
    user_perm = int(input("Enter user permission value: "))
    required_perm = int(input("Enter required permssion value: "))

    print(check_permission(user_perm,required_perm))


