from diagrams import Diagram, Cluster
from diagrams.onprem.analytics import Flink
from diagrams.aws.storage import S3
from diagrams.saas.analytics import Snowflake
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.aws.analytics import Glue
from diagrams.custom import Custom

with Diagram("Streaming ETL", show=False, direction="LR"):

    # Origem de dados em tempo real
    with Cluster("Streaming Source"):
        stream_input = Custom("Data Stream\n(Kafka)", "./icons/stream.png")

    # Processamento com Flink + Checagem de qualidade
    with Cluster("Data Processing"):
        flink_job = Flink("Apache Flink\n(streaming ETL)")
        dq_check = Custom("Real-time\nData Quality", "./icons/data_quality.png")
        flink_job >> dq_check

    # Armazenamento + catálogo
    with Cluster("Storage & Catalog"):
        s3_landing = S3("S3 Bucket\n(raw + processed)")
        catalog = Glue("Data Catalog")

    # Observabilidade
    monitoring = [Prometheus("Prometheus\n(metrics)"), Grafana("Grafana\n(dashboards)")]

    # Armazém de dados e visualização
    with Cluster("Data Warehouse"):
        snowflake = Snowflake("Snowflake\n(auto-scale DW + Snowsight)")
        looker = Custom("Looker\n(advanced BI)", "./icons/kafka.png")

    # Fluxo principal
    stream_input >> flink_job
    dq_check >> s3_landing
    s3_landing >> snowflake
    s3_landing >> catalog
    snowflake >> looker

    # Monitoramento
    flink_job >> monitoring
    dq_check >> monitoring
