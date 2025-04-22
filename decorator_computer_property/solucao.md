# Resolução
Criação de um decorator para cachear dados, simulando a funcionalidade de um graph database, onde a entidade nó é única no grafo (considerando seus atributos).
Existem alguns decorator do python (lib functools) que servem para cachear dados, porém eles têm algumas desvantagens se fossem utilizados aqui.
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




