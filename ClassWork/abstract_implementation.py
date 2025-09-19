'''
from abc import ABC, abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        None
class demo(AbstractDemo):
    def display(self):
        print("Abstract Method")
obj = AbstractDemo()

#TypeError: Can't instantiate abstract class AbstractDemo without an implementation for abstract method 'display'
'''
'''
from abc import ABC, abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        None
class demo(AbstractDemo):
    def display(self):
        print("Abstract Method")
obj = demo()
#object is instiated there is no error obj is created for only concrete classes.
'''
'''
from abc import ABC, abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        None
class demo(AbstractDemo):
    def display(self):
        print("Abstract Method")
obj = demo()
obj.display()

'''
'''
from abc import ABC, abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        None
    
    @abstractmethod
    def show(self):
        None
class demo(AbstractDemo):
    def display(self):
        print("Abstract Method")


obj = demo()
obj.display()

#TypeError: Can't instantiate abstract class demo without an implementation for abstract method 'show'
'''
#to overcome

from abc import ABC, abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        None
    
    @abstractmethod
    def show(self):
        None
class demo(AbstractDemo):
    def display(self):
        print("Abstract Method")
    def show(self):
        print("Show Method")


obj = demo()
obj.display()
obj.show()

