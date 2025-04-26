# Asset Manager

- [Cenário](#cenário)
    - [Requisitos Específicos](#requisitos-específicos)
    - [Tarefa](#tarefa)
    -[Entregáveis](#entregáveis)

- [Solução]
    - [Modelo ER](#modelo-er)
    - [Descrição](#descrição)



## Cenário

Uma asset manager está expandindo sua operação de gestão de investimentos e precisa de um sistema robusto para gerenciar seus ativos, clientes, portfólios e transações. O sistema deve ser capaz de armazenar informações detalhadas sobre os ativos sob gestão, incluindo diferentes tipos de investimentos como ações, títulos de dívida (bonds) e fundos imobiliários. Além disso, deve gerenciar as contas dos clientes, os portfólios atribuídos a cada cliente e todas as transações realizadas.


### Requisitos Específicos

- **Clientes**: O sistema deve armazenar informações básicas de cadastro dos clientes.  
- **Ativos**: Os ativos devem incluir as informações do ativo como nome, preço atual e moeda.  
- **Portfólios**: Cada cliente pode ter um ou mais portfólios. Um portfólio pode incluir diversos ativos. É necessário registrar o peso ou a porcentagem de cada ativo no portfólio.  
- **Transações**: Todas as compras e vendas de ativos devem ser registradas.  
- **Rendimentos**: O sistema deve ser capaz de registrar os rendimentos dos ativos, como dividendos para ações e fundos imobiliários, ou pagamento de cupons para bonds.  


### Tarefa

Baseando-se nos requisitos acima, crie um **modelo Entidade-Relacionamento (ER)** detalhado para o sistema de gestão de investimentos da asset manager. Seu modelo deve incluir todas as entidades mencionadas, seus atributos específicos e os relacionamentos entre elas. Considere as **melhores práticas de normalização** para evitar redundâncias e garantir a integridade dos dados.


### Entregáveis

- **Um diagrama do modelo ER**, mostrando entidades, atributos e relacionamentos  
- **Uma breve descrição de cada entidade e relacionamento** no seu modelo

---

## Solução

### Modelo ER

![Modelo ER](2_asset_manager\diagrama_ER_asset.png)

### Descrição

Clientes: 
Entidade que guarda informações básicas sobre os clientes da asset manager (nome, CPF/CNPJ, contato). Relaciona-se com Carteiras em 1:N.

Carteiras: 
Representa portfolios individuais de investimentos dos clientes. Está ligada diretamente ao Cliente (N:1). Também conecta-se a Portfolio_Ativos (1:N), indicando a composição de ativos de cada portfolio.

Ativos:
Tabela que registra ativos financeiros individuais (ações, bonds, fundos imobiliários), incluindo preço atual e tipo. Está relacionada com Transações (1:N), Rendimentos (1:N) e com Portfolio_Ativos (1:N), onde cada ativo pode estar em diversos registros da tabela Portfolio_Ativos.

Transacoes:
Guarda informações detalhadas das operações financeiras realizadas (compras e vendas). Relaciona-se diretamente com Ativos (N:1).

Portfolio_Ativos:
Define explicitamente a composição de cada carteira, armazenando o peso percentual de cada ativo no portfólio. Cada registro pertence exclusivamente a um Portfólio (N:1) e a um Ativo (N:1).

Rendimentos:
Registra os rendimentos periódicos pagos pelos ativos financeiros, como dividendos ou cupons. Tem relacionamento direto com Ativos (N:1), indicando o ativo que gerou o rendimento.
