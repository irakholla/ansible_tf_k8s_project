import os

ansible_playbook_path = "/Users/Ilia_Rakholla/tf_k8s_project/ansible/ansible_tf_k8s_project"

os.chdir(ansible_playbook_path)
os.system("/Users/Ilia_Rakholla/Library/Python/3.9/bin/ansible-playbook test_playbook.yml")