from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]            
        )
        return f'{self.__class__.__name__}({params})'


    def __repr__(self):
        return self.__str__()    





class User(StringReprMixin):
    def __init__(self):
        self.fristname = None
        self.lastname = None
        self.age = None 
        self.phone_numbers = None 
        self.addresses = []




class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):pass 


    @abstractmethod
    def add_fristname(self, fristname):pass


    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone_numbers(self, phone_numbers): pass

    @abstractmethod
    def add_addresses(self, addresses): pass


class UserBuilder(IUserBuilder):
 
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()
 
 
    @property  
    def result(self): 
        return_data = self._result
        self.reset()
        return return_data
    
    def add_fristname(self, fristname):
        self._result.fristname = fristname

   
    def add_lastname(self, lastname):
        self._result.lastname = lastname

    
    def add_age(self, age): 
        self._result.age = age 
    
    def add_phone_numbers(self, phone_numbers): 
        self._result.phone_numbers = phone_numbers
 
    def add_addresses(self, addresses): 
        self._result.addresses = addresses



class UserDirector:
    def __init__(self, builder):
        self._builder: UserBuilder = builder


    def with_age(self, fristname, lastname, age):
        self._builder.add_fristname(fristname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result





if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Joao', 'Da Silva', 23)
    print(user1)

