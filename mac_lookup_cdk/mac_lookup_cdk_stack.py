import os
from aws_cdk import Stack, aws_lambda, aws_apigateway
from constructs import Construct


class MacLookupCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lookup_lmbda = aws_lambda.Function(
            self,
            "MacLookupLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.from_asset("lambda"),
            handler="lookup.handler",
        )

        apigw = aws_apigateway.LambdaRestApi(self, "Endpoint", handler=lookup_lmbda)

        api = apigw.root.add_resource("api")
        v1 = api.add_resource("v1")

        items = v1.add_resource("macs")
        items.add_method("GET")

        item = items.add_resource("{mac}")
        item.add_method("GET")
