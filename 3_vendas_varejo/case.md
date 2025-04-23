## Cenário

Você é um analista de dados que foi encarregado de otimizar o **armazenamento de dados** para análises de vendas de uma grande rede de varejo. A empresa possui um sistema de **banco de dados relacional tradicional**, com um modelo **Entidade-Relacionamento (ER)** que inclui as seguintes entidades principais:

- **Produtos**: Armazena informações sobre os produtos vendidos, incluindo ID do Produto, Nome, Categoria, Preço Unitário e Estoque.
- **Vendas**: Registra cada venda, incluindo ID da Venda, ID do Produto, ID do Cliente, ID do Funcionário, ID da Loja, Data da Venda, Quantidade e Valor Total.
- **Clientes**: Contém dados dos clientes, como ID do Cliente, Nome, E-mail e Telefone.
- **Funcionários**: Mantém informações sobre os funcionários, incluindo ID do Funcionário, Nome, Cargo e ID da Loja em que trabalham.
- **Lojas**: Detalha as lojas da rede, com ID da Loja, Nome, Localização e Gerente.

---

## Tarefa

A partir do modelo ER fornecido, desenvolva um **Star Schema** para otimizar as análises de vendas da empresa.

---

## Entregáveis

- **Um diagrama do Star Schema**, identificando claramente a **tabela de fatos** e as **dimensões**
- **Uma breve descrição de cada tabela**
- **Explique brevemente** como você transformou o modelo ER em um Star Schema, destacando as **decisões de design mais importantes**

---