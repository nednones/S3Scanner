import boto3
from boto.sts import STSConnection

def assumed_role(debug,OTP,mfa_serial,sts_duration,roleArn,SessionName):

    try:
        sts_connection = STSConnection()

        # Use the appropriate device ID (serial number for hardware device or ARN for virtual device).
        # Replace ACCOUNT-NUMBER-WITHOUT-HYPHENS and MFA-DEVICE-ID with appropriate values.
        #OTP = input("Enter OTP: ")
        #debug is used if you want assume-role print credentials

        tempCredentials = sts_connection.get_session_token(
            duration=sts_duration,
            mfa_serial_number=mfa_serial,#"arn:aws:iam::101549811061:mfa/SecurityAuditUser",
            mfa_token=OTP
        )

        STSsession = boto3.client('sts',
                                  aws_access_key_id=tempCredentials.access_key,
                                  aws_secret_access_key=tempCredentials.secret_key,
                                  aws_session_token=tempCredentials.session_token)

        assumed_role_object = STSsession.assume_role(
            RoleArn=roleArn,#"arn:aws:iam::072979390894:role/read",
            RoleSessionName=SessionName#"SecurityAuditSession"
        )

        credentials = assumed_role_object['Credentials']
    except (ValueError, IOError) as e:
        raise("Error Processing your information for Assuming a role")
        credentials = ""

    if(debug):
        print(credentials['AccessKeyId'])
        print(credentials['SecretAccessKey'])
        print(credentials['SessionToken'])

    return credentials

    #s3_resource=boto3.resource(
    #    's3',
    #    aws_access_key_id=credentials['AccessKeyId'],
    #    aws_secret_access_key=credentials['SecretAccessKey'],
    #    aws_session_token=credentials['SessionToken'],
    #)

    # Use the Amazon S3 resource object that is now configured with the
    # credentials to access your S3 buckets.
    #for bucket in s3_resource.buckets.all():
    #    print(bucket.name)