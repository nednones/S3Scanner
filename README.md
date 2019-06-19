# S3Scanner
Used in the same manner as TruffleHog whereby this tool can be used against internal private S3 buckets to scan for secrets or identify yummy findings.

Tool is still in development and will be built with the following in due course:
1.) Normal API Authorisation to execute AWS APIs
2.) Use STS Token Authorisation to execute AWS APIs
3.) Use Assume-Role to Authorise and execute AWS APIs
4.) Retrieve List of all S3 Buckets
5.) Pull directories from within each S3 Bucket
6.) Specify depth to scan objects within directory mapping of S3 Bucket
7.) Perform Entropy of objects in identified buckets

# How to use:
