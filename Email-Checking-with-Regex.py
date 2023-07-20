import re
# ????@??.??
regex = r"\b[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
def check_email(email):
    if re.fullmatch(regex, email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is invalid.")
email1 = "shfidoid@gmail.com"
email2 = "myown.site@our-earth.org"
email3 = "hahah.com"
check_email(email1)
check_email(email2)
check_email(email3)
#%%
