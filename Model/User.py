
class User:

    __firstName = ""
    __lastName = ""
    __username = ""
    __password = ""
    __email = ""
    __institution = ""

    def __init__(self, firstName,lastName,username,password,email,institution):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__username = username
        self.__password = password
        self.__email = email
        self.__institution = institution

    # getters
    def getFirstName(self):
        return self.__firstName

    def getlastName(self):
        return self.__lastName

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getEmail(self):
        return self.__email

    def getInstitution(self):
        return self.__institution

    # setters
    def setFirstName(self,firstName):
        self.__firstName = firstName

    def setlastName(self,lastName):
        self.__lastName = lastName

    def setUsername(self,username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setEmail(self,email):
        self.__email = email

    def setInstitution(self,institution):
        self.__institution = institution

    