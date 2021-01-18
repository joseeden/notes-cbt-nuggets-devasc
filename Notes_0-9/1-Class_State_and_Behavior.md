
# 1 - Class State and Behavior #
____________________________________________________________

<!-- 2021-01-04 04:26:12 -->

## CLASS vs. OBJECTS ##

<p align=center>
    <img src="../Images/class-objects.png">
</p>

**CLASS** 
Your class definition is the blueprint itself - basically, the blueprint is not the house.

**OBJECTS**
You can instantiate the class into an object/s - these are the houses which you can build from the blueprint.

As an example, here's a code where we define three circles from the class circles

    class Circles:
        id = 0                                                      
        radius = 0
        color = ""
        display = True 

        def __init__(self, id, r, c, d):                                # This is the constructor
            self.id = id 
            self.radius = r 
            self.color = c 
            self.display = d 
        
        def circumference(self):                                        # This is a function which can be used
            return 3.14 * 2 * self.radius                                 by the instances


    # Creating the 3 different circles:

    circle1 =  Circle(1, 10, "Blue", True)
    circle2 =  Circle(2, 8, "Yellow", True)
    circle3 =  Circle(3, 17, "Red", False)


    # Printing the result

    print("Circle 1 has a circumference of " + circle1.circumference())
    print("Circle 2 has a circumference of " + circle2.circumference())
    print("Circle 3 has a circumference of " + circle3.circumference())
______________________________________________________________

## STATE and BEHAVIOR ##

Getting the sample class from above, we can define which is the **STATE** and which is the **BEHAVIOR** in a class

```python
class Circles:
    # STATE - represents the state, condition
    color = ""                                          # 
    id = 0                                                                                
    radius = 0                                          
    display = True 

    def __init__(self, id, r, c, d):                               
        # BEHAVIOR - functions
        self.id = id                                    
        self.radius = r                                            executed.
        self.color = c 
        self.display = d 
    
    def circumference(self):                                        
        return 3.14 * 2 * self.radius               
```