#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mac_lookup_cdk.mac_lookup_cdk_stack import MacLookupCdkStack


app = cdk.App()
MacLookupCdkStack(app, "MacLookupCdkStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
    region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
