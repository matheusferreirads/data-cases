# Função `reconcile_accounts`

### Objetivo
Criar uma função `reconcile_accounts` que realiza a **conciliação (ou batimento)** entre dois grupos de transações financeiras.

### Assinatura da função
```python
def reconcile_accounts(transactions1: list[list[str]], transactions2: list[list[str]]) -> tuple[list[list[str]], list[list[str]]]:
```

### Entradas
A função deve receber **duas listas de listas**, onde cada sublista representa uma transação com os seguintes campos (todos como `strings`):

1. **Data** – no formato `YYYY-MM-DD`
2. **Departamento**
3. **Valor**
4. **Beneficiário**

### Saídas
Retorna duas novas listas de listas (cópias das originais), **cada uma com uma nova coluna à direita**:

- `"FOUND"` se a transação tiver correspondência na outra lista;
- `"MISSING"` caso contrário.

### Regras para Conciliação

- A **conciliação é baseada em todos os campos**, exceto pela **data**, que pode ser **um dia antes, o mesmo dia, ou um dia depois**.
- Cada transação pode ser **usada apenas uma vez** na conciliação.
- Se houver múltiplas possibilidades de correspondência, deve ser escolhida aquela com **data mais próxima e mais cedo**.
- Podem existir transações duplicadas nos arquivos.

---

### Exemplo

#### `transactions1.csv`
```csv
2020-12-04,Tecnologia,16.00,Bitbucket
2020-12-04,Jurídico,60.00,LinkSquares
2020-12-05,Tecnologia,50.00,AWS
```

#### `transactions2.csv`
```csv
2020-12-04,Tecnologia,16.00,Bitbucket
2020-12-05,Tecnologia,49.99,AWS
2020-12-04,Jurídico,60.00,LinkSquares
```

### Uso
```python
import csv
from pathlib import Path
from pprint import pprint

transactions1 = list(csv.reader(Path('transactions1.csv').open()))
transactions2 = list(csv.reader(Path('transactions2.csv').open()))
out1, out2 = reconcile_accounts(transactions1, transactions2)

pprint(out1)
# [['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket', 'FOUND'],
#  ['2020-12-04', 'Jurídico', '60.00', 'LinkSquares', 'FOUND'],
#  ['2020-12-05', 'Tecnologia', '50.00', 'AWS', 'MISSING']]

pprint(out2)
# [['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket', 'FOUND'],
#  ['2020-12-05', 'Tecnologia', '49.99', 'AWS', 'MISSING'],
#  ['2020-12-04', 'Jurídico', '60.00', 'LinkSquares', 'FOUND']]
```

--- 
