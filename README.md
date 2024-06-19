# AWS-SDK-boto3
Reduce ClickOps by using python scripts to interact with AWS Cloud programatically

Boto3 is a Software Development Kit (SDK) for Python designed by AWS. This SDK contains the libraries,
modules and tools to write Python programs that interact with AWS services. The programs can retrieve
information, create and delete resources (CRUD verbs = create, read, update and delete).

AWS Boto3 (and AWS Command Line Interface too) interacts with a lower level software module which is
called the botocore. For example, the calls from boto3 are translated into API calls using the secure web
protocol HTTPS. These API calls are directed to the endpoints of the different AWS cloud services such as
Elastic Compute Cloud (EC2), networking services (VPC), databases (RDS), storage (S3), functions and
many more. The HTTPS protocol carries the answers back in the format of the XML language. Then
botocore translates the answers to the boto3 requester.
