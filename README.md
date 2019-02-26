# Amazon s3 zipping service(API)

## S3zipper API using Python

# S3zipper(API)
S3zipper is a managed zipping service for Amazon S3.  
It is a lightweight API but robust in its capabilities.
It can handle zipping many Gigabytes of data efficiently.

# Documentation
1. Zipping to Amazon S3 bucket:  
[Zip to S3 API](https://docs.s3zipper.com/#23fc2566-464e-bcf7-1e0d-614dd77290df)
2. Stream zipping while downloading:  
[Stream S3 Downloads API](https://docs.s3zipper.com/#1c290c02-8c67-14d7-6fee-3912dca4abbf)
3. EC2 AMI only (Only for AWS EC2)  
[EC2(AMI) S3ZIPPER API SERVER](https://docs.s3zipper.com/#bd260c71-5f11-4a05-a07b-6e489ca8cb7d)

# Website
- Main Website:  
[S3zipper](https://s3zipper.com/)

- AWS EC2 AMI :  
[Amazon EC2](https://aws.amazon.com/marketplace/pp/B0727QDVXV)

# USAGE

## 1. Register for Account
``` URL : https://s3zipper.com/registration/login ```

Register for a new account or login to start the process.  
[Registration](https://s3zipper.com/registration/login)

## 2. Get credentials
``` URL : https://s3zipper.com/auth/develop ```  

We will need these credentials to later get tokens.  
[Developer](https://s3zipper.com/auth/develop)

## 3. Generate token
```API : https://api.s3zipper.com/gentoken```  

We will need tokens to securely access the rest of the API. Please save this token in a cookie or a session depending on your use case.

- Tokens are generated using credentials from step 2 above.

- All tokens last for 24 hours.

```
# -*- coding: utf-8 -*-
import requests
url = "https://api.s3zipper.com/gentoken"
payload = {'userKey': 'xxxxxxxxx', 'userSecret': 'xxxxxxxxx'} 
r = requests.request("POST", url, data=payload)
print(r.json())
d = r.json()
#Extract only the token part
token = d['token']
# save token in cookie or session for zipstart, zipstate & zipresult.

```

## 4. Start zipping
The API currently supports two generally desired modes:  
### 4a). Zip to Amazon S3 bucket  
 ``` API : https://api.s3zipper.com/v1/zipstart  ```    

**zipstart:**  will zip files back into the same originating bucket and issue a download URL when done.

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
token = token # Get it from cookie or session
myurl = "https://api.s3zipper.com/v1/zipstart"
bearer = 'Bearer {}'.format(token)
headers={"Authorization": bearer }
payload = {'awsKey':    'xxxx',
           'awsSecret': 'xxxx',
           'awsBucket': 'my-bucket',
           'awsRegion': 'us-east-1',
           'filePaths': ['my-bucket/path/to/file/one', 'my-bucket/path/to/file/two', 'my-bucket/path/to/folder']} #backend expects a list/array
r = requests.request("POST", myurl, data=payload ,headers=headers)
#Get raw text and save it
zipstart_output = r.text
print(zipstart_output)
#save zipstart_output "as is" for zipstate & zipresult

```

### 4b). Stream download zip files on a browser
``` API :  https://api.s3zipper.com/v1/streamzip ```

 **streamzip:**  will generate a URL that can later be used to stream download files on a browser.

 ```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
token = token # Get it from cookie or session
myurl = "https://api.s3zipper.com/v1/streamzip"
bearer = 'Bearer {}'.format(token)
headers={"Authorization": bearer }
payload = {'awsKey':    'xxxx',
           'awsSecret': 'xxxx',
           'awsBucket': 'my-bucket',
           'awsRegion': 'us-east-1',
           'filePaths': ['my-bucket/path/to/file/one', 'my-bucket/path/to/file/two', 'my-bucket/path/to/folder']} #backend expects a list/array
r = requests.request("POST", myurl, data=payload ,headers=headers)
#Get raw text and save it
zipstart_output = r.text
print(zipstart_output)
#save zipstart_output "as is" for zipstate & zipresult

 ```

## 5. Check your progess.
``` API : https://api.s3zipper.com/v1/zipstate ```

Some jobs can take quite a bit, and you might want to know their progress.  With this API call, you will get to know if the process completed successfully or if it is still running.
- For this, we will need the result from step 4.

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
token = token # Get it from cookie or session
myurl = "https://api.s3zipper.com/v1/zipstate"
bearer = 'Bearer {}'.format(token)
headers={'Content-Type':'application/json; charset=UTF-8',
         "Authorization": bearer }
payload = zipstart_output # Get it from cookie or session
r = requests.request("POST", myurl, data=payload ,headers=headers)
zipstate_output = r.text
print(zipstate_output)

```

## 6. Get the results.  
``` API : https://api.s3zipper.com/v1/zipresult```  

The API provides a background task that just listens and waits for the result. When done, it returns the result.   
**NB:**  
- It only returns the last result. If you zipped and requested the results emailed to you ; you will get a result about the email being sent.
- This is good if you need to automate things a bit. A good example is if you need to wait and send customized emails containing the result.
- This also consumes the result from step 4.

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
token = token  # Get it from cookie or session
myurl = "https://api.s3zipper.com/v1/zipresult"
bearer = 'Bearer {}'.format(token)
headers={'Content-Type':'application/json; charset=UTF-8',
         "Authorization": bearer }
payload = zipstart_output # Get it from cookie or session
r = requests.request("POST", myurl, data=payload ,headers=headers)
zipstate_output = r.text
print(zipstate_output)

```

## Conlusion

There it is! This API is more than three years in development, and we are putting a lot of effort into it to make sure that it gets even better. Our hope is to make it a de facto zipping service for busy people.

For now, it is intended to be a simple and relatively cheap API that just works and makes things easy.

More examples with different programming languages are available in [Documentation](https://docs.s3zipper.com/)
