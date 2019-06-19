from AWSAssumeRole import assumed_role
import argparse
import json

def AWS_Auth():

    Creds = assumed_role()


def main():
    parser = argparse.ArgumentParser(description='Find secrets hidden in the depths of AWS S3''s.')
    parser.add_argument('--json', dest="output_json", action="store_true", help="Output in JSON")
    parser.add_argument("--regex", dest="do_regex", action="store_true", help="Enable high signal regex checks")
    parser.add_argument("--inspectobject", dest="do_inspect_obj", action="store_true", help="Examine Files regardless of filename")
    parser.add_argument("--max_depth", dest="max_depth", help="Sets level of Directories to examine in each bucket")
    parser.add_argument("--assume_role",dest="assume_role", help="If required to assume role provide mfa_serial,sts_duration,roleArn,SessionName, e.g. [arn:aws:iam::accountnumber:mfa/userrolename,3600,arn:aws:iam::accountnumber:role/roletoassume,MySession]")
    parser.add_argument("--user_role",dest="user_role",help="If not assuming role please parse your AWS Access ID and Secret Key")

    parser.set_defaults(regex=False)
    parser.set_defaults(inspectobject=False)
    parser.set_defaults(max_depth=1000)
    args = parser.parse_args()

    token = AWS_Auth(args)

if __name__ == "__main__":
    main()

    #Creds = assumed_role(True,579040,"arn:aws:iam::101549811061:mfa/SecurityAuditUser",0,"arn:aws:iam::072979390894:role/read","SecurityAuditSession")