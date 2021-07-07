---
title: Inheritance
tags: [object, class, inheritance, child, parent, object_oriented_programming, python]
keywords: object, class, inheritance, child, parent, object_oriented_programming, python
summary: "In brief, inheritance in Object-Oriented-Programming is the ability to define a new **child class** that inherits all properties and methods of another **parent class**."
#permalink: /notes/object-oriented-programming/inheritance/index.html

last_updated: July 9, 2019
---

## Single inheritance  

Consider the example Dog class that we already created in the previous notes. We know that dog is a sub-category, or **sub-class**, or a **child class** of another **super-class** or **parent class**, for example, the super-class of animals. Therefore, in a broader context, it makes sense to create an animal class which contains and defines the basic properties and methods of the class Animal, and then inherit all the shared properties and methods of the Dog class directly from the Animal class, instead of redefining them from scratch for the Dog class specifically.  

Initially, this may seem redundant and useless, but consider the case where you need to develop multiple (sub-)classes, for example, Cat, Cow, Goat, ..., all of which share many properties and methods. In such scenarios, it is highly advantageous to have a super-class that contains all the shared methods and properties, and then define child-classes that inherit all the shared properties and methods directly from the parent classes.  

The general syntax for sub-class definition is as simple as the following
```python
class childName(parrentName):
    # Here goes the list of all new, sub-class-specific properties and methods,
    # including the subclass constructor.
    # ...
```

Here is an example Animal super-class, which has proeprties and methods that are shared among all animal sub-classes, for example, age, weight, alive/dead attributes and, eating, sleeping, ... methods,

```python
class Animal:

    # Animal constructor
    def __init__(self, age = 0, weight = 0, animal_is_alive = True):
        # instance attributes
        self.age = age
        self.weight = weight
        self.animal_is_alive = animal_is_alive

    # eating method
    def eat(self,food=None):
        if food==None:
            print('\nThere is nothing to eat :-{{ \n'.format(food))
        else:
            print('\nEating {}...yum yum yum...\n'.format(food))

    # sleeping method
    def sleep(self):
        print('\nSleeping...ZzZzZz....\n')
```

Now, We could instantiate a dog from this `Animal` class,

```python
Coco = Animal(3,10,True)
Coco.sleep()
Coco.eat()
```
    
    Sleeping...ZzZzZz...
    
    
    There is nothing to eat :-{
    

However, a dog can do a lot more than what the generic `Animal` that we have defined above can do, for example, barking. Therefore, it makes more sense to define a child class `Dog` that is specifically for dogs,

```python
class Dog(Animal):
    def bark(self,thisManyTimes=3):
        print('\n')
        for i in range(thisManyTimes):
            print('hop', end=' ')
        print('\n')
```

No, we can redefine `Coco` as an instance of `Dog` rather than `Animal`,

```python
Coco = Dog(3,10,True)
Coco.bark()
```
    
    hop hop hop
    
Notice in the above example that we did not define the constructor method for the new child class `Dog`. The constructor was automatically inherited from the parent class. It is, however, a good practice to define unique constructors for all classes separately, as the following example.

```python
class Dog(Animal):

    # Dog constructor
    def __init__( self, age = 0, weight = 0, animal_is_alive = True, bark_sound = "hop" ):
        self.bark_sound = bark_sound
        Animal.__init__(self, age, weight, animal_is_alive)

    # barking method
    def bark(self,thisManyTimes=3):
        print('\n')
        for i in range(thisManyTimes):
            print('{}'.format(self.bark_sound), end=' ')
        print('\n')
```

```python
Coco = Dog(3,10,True,"ruf")
Coco.bark()
```
    Ruf Ruf Ruf

Notice in the above example that, the parent class's constructor function `__init__` was called from inside of the child's constructor method. Also, note the extra new attribute that was added in the child's constructor method `bark_sound` and how the rest of the old parameters are passed to the parent's constructor.  

## Multiple-inheritance  

It is also possible for a child class to inherit from multiple classes, just as in the real world where offsprings can have one or more parents. The syntax for multiple-inheritance is as simple as the following,  

```python
class childClassName ( parent1, parent2, ... )
    # Here goes all the new methods and attributes...
```

Just as with the case of single inheritance, the child class inherits all attributes of all of its parents.  

### The Diamond Problem  

In the case of multiple inheritances, what if multiple parents have a method or attribute that has the same name? Which one should be inherited by the child class?  

This inheritance problem is known as the **diamond problem** in Python programming. By convention, the child class inherits the attributes and methods that shared by more than one parent, **only from the first parent from the left, that appears in the parent list in the child's class definition**. For example, consider `MotherDog` and `FatherDog` classes from which `ChildDog` inherits methods and properties,  

```python
class MotherDog(Animal):

    # MotherDog constructor
    def __init__( self, age = 0, weight = 0, animal_is_alive = True ):
        Animal.__init__(self, age, weight, animal_is_alive)

    # MotherDog barking method
    def bark(self,thisManyTimes=3):
        print('\n')
        for i in range(thisManyTimes):
            print('hop', end=' ')
        print('\n')

class FatherDog(Animal):

    # FatherDog constructor
    def __init__( self, age = 0, weight = 0, animal_is_alive = True, running_Speed = 10 ):
        self.running_Speed = running_Speed
        Animal.__init__(self, age, weight, animal_is_alive)

    # FatherDog barking method
    def bark(self,thisManyTimes=10):
        print('\n')
        for i in range(thisManyTimes):
            print('ruf', end=' ')
        print('\n')

class ChildDog(MotherDog,FatherDog):

    # ChildDog constructor
    def __init__( self, age = 0, weight = 0, animal_is_alive = True, running_Speed = 10 ):
        Animal.__init__(self, age, weight, animal_is_alive)
```

Note that the implementation of barking method `bark()` is different in the two parent classes `MotherDog` and `FatherDog`, and that **since `MotherDog` appears first in the argument list to `ChildDog`, this child class will inherit the `bark()` method from the `MotherDog`,  

```python
Coco = ChildDog()
Coco.bark()
```
    hop hop hop

If we redefined `ChildDog` as the following by swiching the position of `MotherDog` with `FatherDog` as the input to the class `ChildDog`,  

```python
class ChildDog(FatherDog,MotherDog):

    # ChildDog constructor
    def __init__( self, age = 0, weight = 0, animal_is_alive = True, running_Speed = 10 ):
        Animal.__init__(self, age, weight, animal_is_alive)
```

then, `Coco` will `bark` like `FatherDog`,  

```python
Coco = ChildDog()
Coco.bark()
```
    Ruf Ruf Ruf Ruf Ruf ruf Ruf Ruf Ruf Ruf

Also, note that despite having the input attribute `running_Speed` to the `ChildDog` constructor, since it is not used or defined therein, it will not exist in any instances of `ChildDog`,  

```python
Coco.running_Speed
```
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-85-a2c3b0a91050> in <module>
    ----> 1 Coco.running_Speed

    AttributeError: 'ChildDog' object has no attribute 'running_Speed'

Since `running_Speed` is only defined in the constructor method of `FatherDog`, you will need to explicitly call that constructor to define this property also for `ChildDog`,  

```python
class ChildDog(FatherDog,MotherDog):

    # ChildDog constructor
    def __init__( self, age = 0, weight = 0, animal_is_alive = True, running_Speed = 10 ):
        Animal.__init__(self, age, weight, animal_is_alive)

        # Calling the constructor for the default parent class (in this case, FatherDog) to initialize running_Speed
        super().__init__(age, weight, animal_is_alive, running_Speed)
```

```python
Coco = ChildDog()
Coco.running_Speed
```
    10

The above discussion so far is just a glimpse of inheritance in Python. More advanced topics go beyond the scope and goals of these notes at the moment.  
