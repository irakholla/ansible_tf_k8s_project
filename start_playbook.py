import os

ansible_app_path = "/Users/Ilia_Rakholla/Library/Python/3.9/bin/"
ansible_path = "/Users/Ilia_Rakholla/tf_k8s_project/ansible/ansible_tf_k8s_project"

os.system(f"export PATH=\"{ansible_app_path}:$PATH\"")
os.chdir(ansible_path)
os.system("ansible-playbook k8s.yml")