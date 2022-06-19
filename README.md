# ECR Vulnerable Image Tagger
This solution will automatically tag Docker images which contain a `CRITICAL` vulnerability with a "vulnerable" prefix.

### Deployment
```
sam build
sam deploy --capabilities CAPABILITY_NAMED_IAM  
```

### Local testing
Image should be available in ECR. Don't forget to update the account IDs in the `event.json`.
```
sam build
sam local invoke LambdaFunction --event event.json
```