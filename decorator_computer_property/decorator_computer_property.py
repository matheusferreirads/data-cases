from functools import wraps
from weakref import WeakKeyDictionary

class computed_property:
    def __init__(self, *dependencies):
        self.dependencies = dependencies
        self.func = None
        self.cache = WeakKeyDictionary()
        self._setter = None
        self._deleter = None
        
    def __call__(self, func):
        self.func = wraps(func)(func)
        return self
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        if instance not in self.cache:
            self.cache[instance] = {
                'value': None,
                'depends': {}
            }
            
        cache_entry =  self.cache[instance]
        
        depends_changed = False
        for dep in self.dependencies:
            if hasattr(instance, dep):
                current_value =  getattr(instance, dep)
                if dep not in cache_entry['depends'] or cache_entry["depends"][dep] != current_value:
                    depends_changed = True
                    cache_entry['depends'][dep] = current_value
                    
                    
        if depends_changed or cache_entry['value'] is None:
            cache_entry['value'] = self.func(instance)
            
        return cache_entry['value']
    
    
    def __set__(self, instance, value):
        if self._setter is None:
            raise AttributeError("can't set attribute")
        self._setter(instance, value)
        self.cache.pop(instance, None)
        
    
    def __delete__(self, instance):
        if self._deleter is None:
            raise AttributeError("can't delete attribute")
        self._deleter(instance)
        self.cache.pop(instance, None)
    
    
        
    def setter(self, func):
        self._setter = func
        return self

    def deleter(self, func):
        self._deleter = func
        return self    
        
    @property
    def __doc__(self):
        return self.func.__doc__ if self.func else None
            

#-------------------------------------------------------------------------------------------------------------------------------
       
from math import sqrt
class Vector:
    def __init__(self, x, y, z, color=None):
        self.x, self.y, self.z = x, y, z
        self.color = color

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r}, {self.z!r})'

    @computed_property('x', 'y', 'z')
    def magnitude(self):
        """Magnitude of the vector"""
        print('computing magnitude')
        return sqrt(self.x**2 + self.y**2 + self.z**2) 
    
    
v = Vector(9, 2, 6)
print(v.magnitude) 

v.color = 'red'
print(v.magnitude)  

v.y = 18
print(v.magnitude) 



#--------------------------------------------------------------------------------------------------------------------------------------
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius')
    def diameter(self):
        """Circle diameter from radius"""
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @diameter.deleter
    def diameter(self):
        self.radius = 0


circle = Circle()


print(circle.diameter)  
circle.diameter = 3
print(circle.radius)  




del circle.diameter
print(circle.radius) 


help(Circle)