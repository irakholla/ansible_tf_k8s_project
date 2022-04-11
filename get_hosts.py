import boto3
import os
import pycurl
from io import BytesIO


number_of_slaves = 3
number_of_masters = 1
terraform_path = "/Users/Ilia_Rakholla/tf_k8s_project/terraform/terraform_tf_k8s_project"
ansible_path = "/Users/Ilia_Rakholla/tf_k8s_project/ansible/ansible_tf_k8s_project"
url = 'http://icanhazip.com'

def dns_names(type, number):
    session = boto3.Session(region_name=region_name)
    client = session.client('ec2')
    for n in range(1, number+1):
        response = client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': [
                        f'main_test_{type}-{n}'
                    ]
                },
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running'
                    ]
                }
            ]
        )
        f.write(f"{response['Reservations'][0]['Instances'][0]['PublicDnsName']}\n")

# Get IP

b_obj = BytesIO()
crl = pycurl.Curl()
# Set URL value
crl.setopt(crl.URL, url)
# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)
# Perform a file transfer
crl.perform()
# End curl session
crl.close()
# Get the content stored in the BytesIO object (in byte characters)

# Terraform apply

os.chdir(terraform_path)
os.system(f"terraform apply -auto-approve -var=\"ingress_cidr_block_ssh={b_obj.getvalue().rstrip().decode('utf8')}/32\" -var=\"number_of_slaves={number_of_slaves}\" -var=\"number_of_masters={number_of_masters}\"")

# Get DNS names and re-write hosts file

os.chdir(ansible_path)
region_name = "us-west-2"
f = open("hosts", "w")
f.write("[masters]\n")
dns_names("master", number_of_masters)
f.write("\n[slaves]\n")
dns_names("slave", number_of_slaves)
f.write("\n[all_groups:children]\nmasters\nslaves")
f.close