class Users:
    def __init__(self, username, user,email) -> None:
        self.username = username
        self.user = user
        self.email = email
    def __repr__(self) -> str:
        return f"Users({self.username},{self.user},{self.email})"     
    
    def __str__(self) -> str:
        return self.__repr__()
    


class Userdb:
    def __init__(self) -> None:
        self.Users =[]

    def insert(self,Users):
        i = 0 
        while i < len(self.Users):
            if self.Users.username[i]> Users.Username:
                break
        self.Users.insert(i,Users)
            

    def find(self, username):
        pass

    def update(self, username):
        pass

    def listall(self):
        return self.Users
    



    



a = Users('ab','abcd','ab@cd.com')
print(repr(a))
print(a)
b = Userdb.listall(None)
print(b)
