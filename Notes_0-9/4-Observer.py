
#******************************************************************************************************************#

# 4-Observer.py

#******************************************************************************************************************#

# 2021-01-04 05:43:06

# This is the code used in '2-Understanding_Design_Patterns.txt'

class Observer():
    
    # This is the function called whenever the subject updates.
    def update(self, subject):
        print("Observer: My subject just updated and told me about it.")
        print("Observer: It's states is now - " + str(subject._state))
    
class Subject():
    
    _state = 0
    _observers = []         # this list will contain all the observer objects
    
    # Add observer to the list
    def attach(self, observer):
        self._observers.append(observer)
    
    # Remove observer from the list.
    def detach(self, observer):
        self._observers.remove(observer)
    
    # goes thru the list and update
    def notify(self):
        
        print("Subject: I'm notifying my observers ...")
        
        for observer in self._observers:
            observer.update(self)
    
    # Updates state, which changes the _state to variable n.
    # This also calls the notify() function.
    def updateState(self, n):
        
        print("Subject: I have received a state update!")
        self._state = n
        
        self.notify()
        

# Creating the objects

s = Subject()

obj1 = Observer()
obj2 = Observer()
obj3 = Observer()

# Attach the observer objects to the single Subject object.
s.attach(obj1)
s.attach(obj2)
s.attach(obj3)

s.updateState(5)
