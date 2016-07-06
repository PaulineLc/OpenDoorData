from models import *

user = User.get(User.username == "donovan")

print(user)
print(user.password)