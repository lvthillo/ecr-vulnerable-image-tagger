# ECR Vulnerable Image Tagger
This solution will automatically tag Docker images which contain a `CRITICAL` vulnerability with a "vulnerable" prefix.

![image](https://user-images.githubusercontent.com/14105387/174495997-b6b27be3-4ec3-4540-8592-6882536856fb.png)


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
