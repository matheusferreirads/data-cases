# Asset Manager


Clientes: 
Entidade que guarda informações básicas sobre os clientes da asset manager (nome, CPF/CNPJ, contato). Relaciona-se com Portfolios em 1:N (um cliente possui vários portfolios).

Portfolios: 
Representa carteiras individuais de investimentos dos clientes. Está ligada diretamente ao Cliente (N:1) e às Transações (1:N). Também conecta-se a Portfolio_Ativos (1:N), indicando a composição de ativos da carteira.

Ativos:
Tabela que registra ativos financeiros individuais (ações, bonds, fundos imobiliários), incluindo preço atual e tipo. Está relacionada com Transações (1:N), Rendimentos (1:N) e com Portfolio_Ativos (1:N), onde cada ativo pode estar em diversos registros da tabela Portfolio_Ativos.

Transacoes:
Guarda informações detalhadas das operações financeiras realizadas (compras e vendas). Relaciona-se diretamente com Portfolio (N:1) e com Ativos (N:1).

Portfolio_Ativos:
Define explicitamente a composição de cada carteira, armazenando o peso percentual de cada ativo no portfólio. Cada registro pertence exclusivamente a um Portfólio (N:1) e a um Ativo (N:1).

Rendimentos:
Registra os rendimentos periódicos pagos pelos ativos financeiros, como dividendos ou cupons. Tem relacionamento direto com Ativos (N:1), indicando o ativo que gerou o rendimento.
