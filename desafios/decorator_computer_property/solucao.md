# Computed Property

- [Cenário](#cenário)
    - [Exemplo de Uso](#exemplo-de-uso)

- [Solução](#solução)
    - [Código](#código)

## Cenário

 Na Goldman Sachs, os chamados “strats” contam com um banco de dados orientado a
 objetos, o Securities Database (ou SecDB), em que as relações de dependência entre as
 entidades são modeladas em um grafo. Isso permite que o valor armazenado em um certo nó
 seja considerado válido enquanto suas dependências não sofrerem alteração, o que evita
 recômputos desnecessários. Por outro lado, ao modificar-se qualquer uma de suas
 dependências, o nó fica invalidado, e deverá ser recomputado na próxima consulta.
 O objetivo é recriar esse mecanismo para objetos Python, em memória. Para isso, escreva um
 decorator chamado computed_property, análogo ao `property`. O decorator
 computed_property deve aceitar múltiplos atributos dos quais ele depende, e cachear o valor
 da `property` enquanto o valor desses atributos permanecer inalterado.

### Exemplo de uso

```python
from math import sqrt

class Vector:
    def __init__(self, x, y, z, color=None):
        self.x, self.y, self.z = x, y, z
        self.color = color

    @computed_property('x', 'y', 'z')
    def magnitude(self):
        print('computing magnitude')
        return sqrt(self.x**2 + self.y**2 + self.z**2)
```


```python
>>> v = Vector(9, 2, 6)
>>> v.magnitude
computing magnitude
11.0

>>> v.color = 'red'
>>> v.magnitude 
11.0

>>> v.y = 18
>>> v.magnitude  
computing magnitude
21.0
```

Seu decorator deve aceitar como dependêcias atributos que não existam no objeto em questão. Tais atributos devem ser ignorados. 
Em outras palavras, enquanto um atributo estiver faltando, ele deve ser tratado como inalterado.

```python
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius', 'area')
    def diameter(self):
        return self.radius * 2

>>> circle = Circle()
>>> circle.diameter
2  
```


Seu decorator deve ainda contemplar os métodos `setter` e `deleter`, a exemplo do que ocorre com `property`.

```python
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius')
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @diameter.deleter
    def diameter(self):
        self.radius = 0
```


```python
>>> circle = Circle()
>>> circle.diameter
2

>>> circle.diameter = 3
>>> circle.radius
1.5

>>> del circle.diameter
>>> circle.radius
0
```


Seu decorator também deve tratar corretamente docstrings, da mesma forma como é feito por `property`.

```python
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius')
    def diameter(self):
        """Circle diameter from radius"""
        print('computing diameter')
        return self.radius * 2
```

```python
 >>> help(Circle)
 Help on class Circle in module __main__:
 class Circle(builtins.object)
 |  Circle(radius=1)
 |
 |  Methods defined here:
 |
 |  __init__(self, radius=1)
 |      
Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __weakref__
 |      
|
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      
dictionary for instance variables (if defined)
 list of weak references to the object (if defined)
 |
 |  diameter
 |      
Circle diameter from radius
```



## Solução

Criação de um decorator para cachear dados, simulando a funcionalidade de um graph database, onde a entidade nó é única no grafo (considerando seus atributos).
Existem alguns decorators do python (lib functools) que servem para cachear dados, porém eles têm algumas desvantagens se fossem utilizados aqui.
Abaixo segue uma tabela de comparativo, para entender o porque foi feito dessa forma mais "caseira", que foi a melhor forma que encontrei de resolver o problema,  ao invés de utilizar algum dos decorators já existentes

Na classe Vector, como sugestão, inseri a função abaixo

```python
def __repr__(self):
    return f'Vector({self.x!r}, {self.y!r}, {self.z!r})'
```
Esse método especial facilita a depuração.
A utilização do WeakKeyDictionary permite que o cache da classe Vector seja limpo assim que não tiver mais nada referenciando aquele valor cacheado a uma função existente.
Dessa forma evita sobrecarga de memória no decorator.

Comparativo com Outros Decorators de Cache


| Característica                  | `lru_cache` | `cache` | `cached_property` | `computed_property` |
|--------------------------------|-------------|--------- |--------------------|----------------------|
| Cache por instância            | ❌          | ❌      | ✅                 | ✅                  |
| Invalidação automática         | ❌          | ❌      | ❌                 | ✅                  |
| Dependências explícitas        | ❌          | ❌      | ❌                 | ✅                  |
| Suporte a `setter`/`deleter`   | ❌          | ❌      | ❌                 | ✅                  |
| Complexidade                   | Baixa       | Baixa    | Baixa               | Alta                  |


### Código

- [Código .py](decorator_computer_property.py)
- [Código .ipynb](decorator_computer_property.ipynb)


#### Decorator Class

``` python
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
```            

```python
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
```


```python
v = Vector(9, 2, 6)
print(v.magnitude) 

v.color = 'red'
print(v.magnitude)  

v.y = 18
print(v.magnitude) 
```

```
computing magnitude
11.0
11.0
computing magnitude
21.0
```

```python
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
```

```python
circle = Circle()

print(circle.diameter)  
circle.diameter = 3
print(circle.radius)  

del circle.diameter
print(circle.radius) 

help(Circle)
```

```
2
1.5
0
Help on class Circle in module __main__:

class Circle(builtins.object)
 |  Circle(radius=1)
 |
 |  Methods defined here:
 |
 |  __init__(self, radius=1)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  diameter
 |      Circle diameter from radius

```
