# `computed_property`: Decorator com dependências reativas em Python

 Na Goldman Sachs, os chamados “strats” contam com um banco de dados orientado a
 objetos, o Securities Database (ou SecDB), em que as relações de dependência entre as
 entidades são modeladas em um grafo. Isso permite que o valor armazenado em um certo nó
 seja considerado válido enquanto suas dependências não sofrerem alteração, o que evita
 recômputos desnecessários. Por outro lado, ao modificar-se qualquer uma de suas
 dependências, o nó fica invalidado, e deverá ser recomputado na próxima consulta.
 O objetivo é recriar esse mecanismo para objetos Python, em memória. Para isso, escreva um
 decorator chamado 
computed_property, análogo ao 
property. O decorator
 computed_property deve aceitar múltiplos atributos dos quais ele depende, e cachear o valor
 da property enquanto o valor desses atributos permanecer inalterado.

## Exemplo de uso

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

### Testando:

```python
>>> v = Vector(9, 2, 6)
>>> v.magnitude
computing magnitude
11.0

>>> v.color = 'red'
>>> v.magnitude  # Não recalcula, pois 'color' não é dependência
11.0

>>> v.y = 18
>>> v.magnitude  # Recalcula, pois 'y' é uma dependência
computing magnitude
21.0
```

---
Seu decorator deve ainda contemplar os métodos 
ocorre com 
property.

```python
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius', 'area')
    def diameter(self):
        return self.radius * 2

>>> circle = Circle()
>>> circle.diameter
2  # Funciona mesmo que 'area' ainda não exista
```

---

Seu decorator também deve tratar corretamente docstrings, da mesma forma como é feito por
 property.

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

### Testando:

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

---

## Docstrings preservadas

O decorator também deve preservar a **docstring original**, como acontece com `property`.

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
...
|  diameter
|      Circle diameter from radius
```

