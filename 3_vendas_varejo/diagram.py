#pip install diagrams

from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import Glue
from diagrams.aws.database import Redshift
from diagrams.aws.analytics import Quicksight

with Diagram("Daily ETL Pipeline on AWS", show=False, direction="LR"):
    with Cluster("Raw Data Storage"):
        raw_bucket = S3("S3 Raw Bucket\n50GB .txt @03h")

    with Cluster("Processing Trigger"):
        trigger_fn = Lambda("Lambda Trigger\n(S3 PUT)")

    with Cluster("ETL Jobs"):
        etl_job = Glue("Glue ETL Job\n(clean • enrich • load)")

    with Cluster("Data Warehouse"):
        dw = Redshift("Redshift DW\n(OLAP Storage)")

    with Cluster("BI & Visualization"):
        dashboard = Quicksight("Quicksight\n(Dashboards)")

    raw_bucket >> trigger_fn >> etl_job >> dw
    dw >> dashboard
