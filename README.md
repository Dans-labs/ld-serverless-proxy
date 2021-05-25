# Linked Data Serverless Proxy
Serverless LD Proxy implementation as Lambda function created on Amazon AWS.

# Installation
Install aws cli and run configuration setup
```aws configure```

Install the AWS Serverless Application Model (SAM)
```pip install aws-sam-cli```

Build LD Proxy image:
```sam build --use-container```

Deploy on AWS following the instruction 
```sam deploy --guided```

Further instructions are coming...
