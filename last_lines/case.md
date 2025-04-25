# Função `last_lines`

Escreva uma função chamada `last_lines` que **devolve as linhas de um arquivo de texto em ordem inversa**. Caso esteja familiarizado com a linha de comando Unix, essa função deve ter o mesmo comportamento do comando `tac`.

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

> **Observação:**  
> A função deve **manter o caractere de fim de linha** (`\n`) em cada linha retornada.

---

### A função deve devolver um **iterador**:
```python
>>> lines = last_lines('my_file.txt')
>>> next(lines)
'And this is line 3\n'
>>> next(lines)
'This is line 2\n'
>>> next(lines)
'This is a file\n'
```

---

### Requisitos técnicos:

- A função deve **ler o arquivo em blocos** com tamanho máximo dado por um argumento opcional.
- O valor padrão para esse tamanho deve ser `io.DEFAULT_BUFFER_SIZE`.
- A leitura deve considerar que o arquivo está codificado em **UTF-8**, o que significa que:
  - É necessário evitar a leitura ou decodificação de caracteres Unicode **parcialmente**.
  - Ou seja, a função deve garantir que caracteres multibyte não sejam quebrados entre leituras.

---