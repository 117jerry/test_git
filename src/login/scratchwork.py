import hashlib


def hash_password(passw):
    return hashlib.sha3_256(str.encode(passw)).hexdigest()


password = ['katara', 'mai', 'sokka']

for p in password:
    print(hash_password(p))

Users = {'aang':'d962ea0b6ca55d646d0ae16b1eef07af5983628cf0aa1d34e563f909c888b356',
             'zuko':'c041ca4f77ac451b14bc8ae97a1c4e95bc01008e10b3d598bd438fd2c2468b38',
             'toph':'08a01a96bcde90b67c4ffeb5845c8f0771f33450a31d4d76d88940089cfaba50'}

# d962ea0b6ca55d646d0ae16b1eef07af5983628cf0aa1d34e563f909c888b356
# c041ca4f77ac451b14bc8ae97a1c4e95bc01008e10b3d598bd438fd2c2468b38
# 08a01a96bcde90b67c4ffeb5845c8f0771f33450a31d4d76d88940089cfaba50


# user = Login_System()
# username = input('Enter username:')
# password = input('Enter password:')
# user.login(username, password)


# user = 'pikachu'
# query = 'select password from "Users" ' \
#                     "where username='%s'" %user
# print(query)


# cur.execute('select password from "Users" '
#             "where username='zuko'")
#
# hash_pass = cur.fetchone()
# print(hash_pass[0])