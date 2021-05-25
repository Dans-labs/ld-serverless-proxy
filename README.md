# Linked Data Serverless Proxy
Serverless LD Proxy implemented as FastAPI framework deployed as Lambda function on Amazon AWS. Read more about [AWS Lambda](https://aws.amazon.com/lambda/) and how to setup [custom domain name](https://www.serverless.com/blog/serverless-api-gateway-domain) for the deployment.

# Installation
Install aws cli and run configuration setup

```aws configure```

Install the AWS Serverless Application Model (SAM)

```pip install aws-sam-cli```

Build LD Proxy image:

```sam build --use-container```

# Create new role for AWS Lambda

You have to set up a role that the AWS Lambda will assume within AWS account and grant required permissions. Go to the [IAM console](https://console.aws.amazon.com/iam/), select Roles and Create, and then choose Lambda as the service. Press next and it’ll take you to the Permissions tab, search for lambda and select the AWSLambdaBasicExecutionRole. Save new role with some name, for example, lambda-demo.

# Deployment on AWS 

Deploy on AWS following the instruction 

```sam deploy --guided```

Go to AWS console in the [APIs section](https://console.aws.amazon.com/apigateway/main/apis?region=us-east-1), find function called ld-proxy, to Prod stage and check the Invoke URL, for example, [https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod](https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod)

Check if LD Proxy is operational:

```curl https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod/ping```

OpenAPI specification should be available on /prod/docs path, try this:

```curl https://1nrrr3dhei.execute-api.us-east-1.amazonaws.com/prod/docs```

# How to test LD Proxy

You can host your API locally by running: 

```sam local start-api```

Check if API is up and running:

```curl http://127.0.0.1:3000/prod/ping```


Further instructions are coming...
