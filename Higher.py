import logging
from datetime import datetime
logging.basicConfig(filename="logs.log",level=logging.DEBUG)
database = {
    "user1": {"email": "fairozahmadsheikh@gmail.com", "password": "123@mtech"},
    "user2": {"email": "ahmadsheikh@gmail.com", "password": "121@mtech"},
    "user3": {"email": "sheikhabid@gmail.com", "password": "129@mtech"},
    "user4": {"email": "sheikh@gmail.com", "password": "103@mtech"},
}
email = input("Enter Email: ")
password = input("Enter Password: ")
authenticated = False
for user_data in database.values():
    if user_data["email"] == email and user_data["password"] == password:  
        authenticated = True
        break  
if authenticated:
    logging.warning(f"Login Success for : {email} {datetime.now()}")
    is_admin=input("Are You Admin (Y/N) : ").lower()
    if is_admin in['y','1','yes']:
        username=input("Enter Admin Username : ")
        password=input("Enter Admin Password : ")
        if username =="Root" and password=="Kingx@123":
            logging.critical(f"Admin logged in through  {email} at {datetime.now()}")
            print(database)
        else:
            print("Invalid Crediantials ")
else:
    logging.warning(f"Someone Tried Login at {datetime.now()}")
    print("Invalid Credentials")
