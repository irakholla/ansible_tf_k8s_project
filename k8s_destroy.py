import os

terraform_path = "/Users/Ilia_Rakholla/tf_k8s_project/terraform/terraform_tf_k8s_project"

# Terraform destroy

os.chdir(terraform_path)
os.system("terraform destroy -auto-approve")