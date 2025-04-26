# PostgreeSQL

- [<span style="font-size:45px">Cenário</span>](#Cenário)
    - [Tarefa](#Tarefa)
- [Solução](#Solução)



## Cenário

A empresa quer disponibilizar um banco de dados PostgreSQL para uso em produção. Temos um time pequeno de dados e esse banco não pode ter downtime. 
Ele será utilizado por colaboradores em São Paulo, Nova York e Londres com alta frequência de leitura e gravação.



### Tarefa

Quais aspectos e configurações devem ser levadas em consideração na disponibilização desse banco de dados? Explique-os.


----

## Solução

Para o problema apresentado é fundamental pensar desde o início numa arquitetura de replicação e failover. Em vez de usar um único servidor “master”, configurar réplicas “standbys” em regiões diferentes e habilitar a réplica via streaming com confirmação síncrona: assim, cada gravação no servidor principal só é considerada concluida quando já estiver nos secundários, evitando perda de dados. Se o nó principal falhar, uma ferramenta como Patroni ou repmgr detecta o problema e promove automaticamente uma das réplicas, mantendo o serviço no ar sem intervenção manual.

Além disso, dividir o tráfego de leitura e escrita reduz a carga no master e melhora a latência. Direcionando consultas de leitura para réplicas instaladas geograficamente próximas aos usuários de Nova York e Londres, e concentrando as gravações no master em São Paulo. Para evitar que o banco fique sobrecarregado com muitas conexões simultâneas, vale usar um pooler leve como PgBouncer, que mantém poucas conexões abertas ao PostgreSQL e redistribui as requisições conforme necessário.  

Para o dimensionamento de memória e disco, reservar cerca de 25% da RAM para `shared_buffers` e ajustar o `work_mem` para evitar uso excessivo de disco em operações complexas, mantendo o autovacuum bem calibrado para não deixar tabelas inchadas. Fazer backups completos regulares, arquivar os logs de transação (WAL) e testes periódicos da restauração para ter recuperação ponto-a-ponto. Monitoramento via Prometheus/Grafana (latência de replicação, I/O, uso de CPU e disco) e alertas para qualquer atraso ou saturação. 
Definir o banco sempre em UTC e deixar a conversão de fuso por conta da aplicação, garantindo consistência nos horários de todos os colaboradores. Dessa forma, obtendo uma base sólida, resiliente e de fácil manutenção, sem exigir configurações superavançadas.