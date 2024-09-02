import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_s3_notifications as s3_notifications,
)
from constructs import Construct


class AwsCdkTutorialStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwsCdkTutorialQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # L1 and L2 construct of an S3 Bucket
        level1_s3_bucket = s3.CfnBucket(
            scope=self,
            id="MyFirstLevel1ContructBucket",
            bucket_name="my-first-level1-construct-bucket-amit",    # must be unique and lowercase name
            versioning_configuration={"status": "Enabled"}, # 'E' must be capital in "Enabled"
        )
        
        level2_s3_bucket = s3.Bucket(
            scope=self,
            id="MyFirstLevel2ContructBucket",
            versioned=True,
            bucket_name="my-first-level2-construct-bucket-amit", # must be unique and lowercase name
            # removal_policy=cdk.RemovalPolicy.DESTROY,
        )
        
        # Setting up S3 bucket notification using SQS
        queue = sqs.Queue(
            scope=self,
            id="MyQueueForS3Bucket",
            queue_name="my-queue-for-s3-bucket-amit",
        )
        
        # # Add S3 event notification for PUT events
        level2_s3_bucket.add_event_notification(
            event=s3.EventType.OBJECT_CREATED_PUT,
            dest=s3_notifications.SqsDestination(queue),
        )
        level2_s3_bucket.add_event_notification(
            event=s3.EventType.OBJECT_CREATED_COPY,
            dest=s3_notifications.SqsDestination(queue),
        )
