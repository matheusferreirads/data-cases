# Last Lines

- [Cenário](#cenário)
    - [Exemplo de Uso](#exemplo-de-uso)

- [Solução](#solução)
    - [Código](#código)



Escreva uma função chamada `last_lines` que devolve as linhas de um arquivo de texto em ordem inversa. Caso esteja familiarizado com a linha de comando Unix, essa função deve ter o mesmo comportamento do comando `tac`.

### Exemplo de arquivo: `my_file.txt`
```
This is a file
This is line 2
And this is line 3
```

### Exemplo de uso:
```python
>>> for line in last_lines('my_file.txt'):
...     print(line, end='')
...
And this is line 3
This is line 2
This is a file
```

 Note que a função `last_lines` deve incluir o caractere terminador de linha (suponha \n) para cada linha.


```python
>>> lines = last_lines('my_file.txt')
>>> next(lines)
'And this is line 3\n'
>>> next(lines)
'This is line 2\n'
>>> next(lines)
'This is a file\n'
```



 Sua função deve ler o arquivo fornecido em pedaços não maiores que o tamanho dado por um argumento da função, cujo valor padrão deve ser `io.DEFAULT_BUFFER_SIZE`. Dito de outro
 modo,  `last_lines` não deve ler mais do que um certo número de bytes (número esse dado por um argumento facultativo) de cada vez. Suponha ainda que o arquivo fornecido possa 
 estar codificado em UTF-8, de modo a conter qualquer caractere Unicode válido. Isso significa que, ao ler e decodificar texto do arquivo, deve se certificar de não decodificar 
 um trecho que contenha um caractere pela metade.

---

## Solução

### Código

- [Código .py](last_lines.py)
- [Código .ipynb](last_lines.ipynb)

``` python

import io
import os

def last_lines(file_path, bufsize=io.DEFAULT_BUFFER_SIZE):
    try:
        with open(file_path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            pos = f.tell()
            buffer = b''
            first_pass = True

            while pos > 0:

                read_size = min(bufsize, pos)
                pos -= read_size
                f.seek(pos)
                chunk = f.read(read_size)


                buffer = chunk + buffer


                parts = buffer.split(b'\n')

                if first_pass and pos == 0 and parts and parts[-1] == b'':
                    parts = parts[:-1]

                first_pass = False


                buffer = parts[0]

                for segment in reversed(parts[1:]):

                    cleaned = segment.rstrip(b'\r')
                    yield cleaned.decode('utf-8') + '\n'

            if buffer:
                cleaned = buffer.rstrip(b'\r')
                yield cleaned.decode('utf-8') + '\n'
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo '{file_path}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
```

``` python

# cria o arquivo de teste
with open('my_file.txt', 'w', encoding='utf-8') as f:
    f.write("This is a file\n")
    f.write("This is line 2\n")
    f.write("And this is line 3\n")

```

``` python

for line in last_lines('my_file.txt'):
    print(line, end='')

```
```
And this is line 3
This is line 2
This is a file

```

```python
lines = last_lines('my_file.txt')
next(lines)
```
```
'And this is line 3\n'
```
```python
next(lines)
```
```
'This is line 2\n'
```
```python
next(lines)
```
```
'This is a file\n'
```