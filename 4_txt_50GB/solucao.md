# txt 50GB

Consierando que o arquivo é armazenado no S3, é interessante uma abordagem utilizando a arquitetura AWS.
Para trigger do processo será utilizada uma lambda function que monitora o bucket para verificar quando um novo arquivo chega.
Como orquestrador de fluxo será utilizado o StepFunctions:
    Após o início do fluxo o arquivo é processado via Glue Job, lá será feito o processo de ETL do arquivo.
    O próximo passo é a aplicação de um processo de data quality 
    Antes de salvar os arquivos no banco é importante uma validação que contém guardrails evitando o deploy de uma tabela com dados incorretos
    Por final a tabela é criada no data warehouse (Redshift nesse exemplo)
Como ferramenta de BI seria interessante o quicksight pensando em integração, pois é possível plugar direto no Redshift e fica tudo na mesma arquitetura cloud. 

Obs:
    As queries podem ser realizadas no query editor do redshift, que aceita o padrão SQL.
    Escolhi o Glue pois acredito ser a melhor ferramenta para isso, além de ser pouco complexo de configurar e fácil de schedular.
    O redshift foi pensando no volume de dados e necessidade de ETL, então faz sentido ficar em um banco com persistência de dados, além de necessidade de queries e conexão com ferramentas de BI, como ele é dedicado, oferece baixa latência e um bom suporte pra alta concorrência.
    O Quicksight foi pensando em facilidade de integração e manter tudo num mesmo ecossistema (AWS)