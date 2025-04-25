## 1) Diferença entre `BEGIN/END` e `BEGIN` no `psql`

Explique, sucintamente, a diferença entre `BEGIN/END` dentro de um objeto de linguagem procedural PL/pgSQL e o `BEGIN` que se executa no cliente `psql` para execução de uma simples DML, como um `UPDATE`.

**Resposta**

    No PL/pgSQL, as palavras-chave `BEGIN` e `END` servem apenas para delimitar um bloco de código dentro de funções ou procedimentos.
    No cliente psql `BEGIN;`  está acionando o mecanismo de transação do PostgreSQL, tudo o que vier em seguida (UPDATE, INSERT, DELETE...) ficará
     
    “pendente” até que você confirme as alterações com um `COMMIT;` ou decida desfazê-las com um `ROLLBACK;`. Enquanto o `BEGIN…END` de PL/pgSQL não abre nem fecha transações, o `BEGIN` do psql é justamente o comando que inicia esse controle transacional.

---

## 2) Concatenação de strings no PostgreSQL

Assinale a alternativa que corretamente concatena as palavras ‘ABC’ e ‘def’ para formar ‘ABCdef’:

- A. `SELECT 'ABC' . 'def';`
- B. `SELECT cat('ABC', 'def') FROM pg_operator;`
- C. `SELECT 'ABC' + 'def' FROM duaL;`
- D. `SELECT 'ABC' + 'def' FROM dual;`
- E. `SELECT 'ABC' || 'def';`

**Resposta:**

    Alternativa correta: E

---

## 3) Índices no PostgreSQL

O PostgreSQL pode usar índices para acessar uma tabela. Assinale **duas alternativas erradas** sobre índices:

- A. Um índice é criado pelo `CREATE INDEX` e eliminado pelo `DROP INDEX`.
- B. Quando a query usa o índice, ela pode retornar as linhas de forma muito mais rápida.
- C. Os tipos de índices são B-TREE, Hash, R-TREE e GiST.
- D. Quando se cria um índice, a query que usa aquela coluna indexada fica sempre mais rápida.
- E. Criar um índice que não esteja sendo utilizado por nenhuma query não altera de forma alguma o desempenho do banco de dados.

**Resposta**

    Alternativas: D, E

---

## 4) `VIEWS` no PostgreSQL

Assinale **duas afirmações corretas** sobre `VIEWS` no PostgreSQL:

- A. Uma VIEW é criada pelo comando `DECLARE VIEW` e eliminada pelo comando `DROP VIEW`.
- B. Uma VIEW é uma tabela virtual que não existe no disco.
- C. Uma VIEW ajuda a simplificar queries complicadas.
- D. Uma VIEW pode ser criada com o mesmo nome de uma tabela no esquema em questão.
- E. Uma VIEW só existe enquanto o processo postmaster está rodando, sendo eliminada quando o servidor para.


**Resposta:**

    Alternativas: B, C
---

## 5) Query com subquery

Baseado na tabela `EMPREGADOS` abaixo, escreva uma query (usando subquery) que retorna o `ID`, o `FIRST_NAME`, o `MANAGER_ID` e o `SALARY` de todos os empregados que têm salário maior que o maior salário dos empregados com `MANAGER_ID` igual a 100. Ordene o resultado pelo salário.

```
+----+-------------+------------+------------+----------+----------------+------------+---------------+
| ID | FIRST_NAME  | LAST_NAME  | HIRE_DATE  | SALARY   | COMMISSION_PCT | MANAGER_ID | DEPARTMENT_ID |
+----+-------------+------------+------------+----------+----------------+------------+---------------+
|100 | Marcelo     | Goncalves  | 1997-04-17 | 20000.00 |       0.00     |     101    |       80      |
|101 | Carlos      |            |            | 17000.00 |       0.00     |     100    |       90      |
|102 | Renato      | Macaranduba| 1997-05-18 | 16000.00 |       0.00     |     100    |       90      |
|300 | Geraldo     | Silva      | 2001-10-01 |  8300.00 |       0.00     |     205    |      110      |
+----+-------------+------------+------------+----------+----------------+------------+---------------+
```
```sql
SELECT
  id,
  first_name,
  manager_id,
  salary
FROM empregados
WHERE salary > (
  SELECT MAX(salary)
  FROM empregados
  WHERE manager_id = 100
)
ORDER BY salary;
```


---

## 6) Verdadeiro (V) ou Falso (F)

Baseado na pergunta anterior, responda V para verdadeiro e F para falso nas afirmações abaixo:

- A. (**V**) Um índice composto nas colunas (`manager_id`, `salary`) é recomendado.
- B. (**F**) A query requisitada será sempre lenta, não importando como está indexada a tabela.
- C. (**F**) O PostgreSQL sempre fará a ordenação em disco, independente do índice usado.
- D. (**V**) Um índice de função (índice com expressão) deixaria a query mais rápida.
- E. (**V**) O PostgreSQL permite que se use tabelas temporárias para evitar o uso de subqueries.

---

## 7) Alternativa incorreta sobre PostgreSQL

Assinale a alternativa **incorreta** sobre PostgreSQL:

- A. O PostgreSQL possui recurso para permitir execução de queries em paralelo.
- B. O PostgreSQL possui recurso para permitir criação de índices de forma ONLINE, sem bloquear escrita.
- C. Na criação de um banco de dados é obrigatório definir o proprietário com a palavra chave `OWNER` do banco.
- D. Define-se o esquema que deseja trabalhar com `search_path` para evitar usar o nome do esquema nas tabelas o tempo todo.
- E. Os valores do `search_path` podem conter esquemas separados por vírgula.

**Resposta:** 

    Alternativa: C
---