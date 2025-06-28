import boto3

s3 = boto3.client('s3')
bucket_name = 'sentimentibm'

# Upload files
s3.upload_file('input.txt', bucket_name, 'input.txt')
s3.upload_file('output.json', bucket_name, 'output.json')

print(f"Uploaded input and output to s3://{bucket_name}/")
