from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.aws.analytics import Glue
from diagrams.aws.database import Redshift
from diagrams.aws.analytics import Quicksight

with Diagram("ETL Pipeline on AWS with Step Functions", show=False, direction="LR"):
 
    with Cluster("Raw Data Storage"):
        raw_bucket = S3("S3 Raw Bucket\n50GB .txt @03h")


    trigger_fn = Lambda("Lambda Trigger\n(S3 PUT)")


    orchestrator = StepFunctions("Step Functions\n(State Machine)")


    with Cluster("Data Processing"):
        etl_job = Glue("Glue ETL Job\n(clean • enrich • load)")
        dq_job = Glue("Data Quality Job\n(validation • profiling)")
        guardrail_check = Glue("Guardrails Check\n(thresholds • alerts)")

    dw = Redshift("Redshift DW\n(OLAP Storage)")


    dashboard = Quicksight("Quicksight\n(Dashboards)")

    raw_bucket >> trigger_fn >> orchestrator
    orchestrator >> etl_job >> dq_job >> guardrail_check >> dw >> dashboard
