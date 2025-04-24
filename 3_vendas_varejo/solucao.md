# Star Schema:
- **Tabela Fato (tb_fato_vendas)**:  
Tabela central contendo métricas quantitativas das vendas realizadas. Inclui informações essenciais para análise como ID da venda, quantidade vendida, valor total, além de chaves estrangeiras para dimensões relacionadas (produto, cliente, funcionário, loja e tempo).

- **Dimensões**:
  - **tb_dim_produtos**: Armazena informações detalhadas dos produtos, como nome, categoria e preço unitário. Ajuda a compreender quais itens geram mais vendas.
  - **tb_dim_clientes**: Registra informações dos clientes (nome, CPF/CNPJ, e-mail, telefone), permitindo análises sobre o comportamento de consumo dos clientes.
  - **tb_dim_funcionarios**: Guarda informações dos funcionários (nome, cargo, loja vinculada), permitindo análise da performance de vendas por funcionário.
  - **tb_dim_lojas**: Contém informações sobre cada loja (nome, localização, gerente), permitindo avaliar desempenho por unidade.
  - **tb_dim_data**: Fornece contexto temporal detalhado das vendas (data completa, ano, mês e dia), permitindo análises temporais detalhadas.

---

## Explicação da Transformação ER em Star Schema:

Para transformar o modelo ER original em um Star Schema, eu reorganizei as tabelas originais considerando um modelo dimensional, ideal para consultas analíticas rápidas e eficientes:

- **Seleção da Tabela Fato**:  
  Escolhi a tabela de **Vendas** para ser a tabela central (**Fato**) por conter as medidas quantitativas (quantidade, valor das vendas) essenciais para análises.

- **Criação das Dimensões**:  
  As tabelas que fornecem contexto qualitativo (Clientes, Produtos, Funcionários, Lojas) tornaram-se dimensões. Cada dimensão passou a ter um ID único, referenciado diretamente pela tabela de fatos, simplificando consultas analíticas e melhorando a performance.

- **Dimensão Tempo (Data)**:  
  Uma dimensão de tempo dedicada (**tb_dim_data**) foi criada para possibilitar análises granulares e consistentes ao longo do tempo (por ano, mês, dia), melhorando significativamente as capacidades analíticas.

- **Simplificação das Relações**:  
  Relações complexas do modelo ER original foram simplificadas para um modelo estrela, onde as dimensões têm relação direta e simples com a tabela fato, reduzindo a necessidade de junções complexas em consultas analíticas.