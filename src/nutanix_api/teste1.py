import requests

# Configurações
nutanix_url = "https://10.0.17.42/v3/clusters/7a190fbc-138c-471a-a8b7-18109b07bdc5/vms"
nutanix_username = "admin-abelardo"
nutanix_password = "Drv962324"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Autenticação
auth_data = {
    "username": nutanix_username,
    "password": nutanix_password
}
auth_response = requests.post("https://seu-cluster-nutanix/v3/clusters/SEU_CLUSTER_UUID/auth", json=auth_data, headers=headers)
auth_response.raise_for_status()

# Obter token de autenticação
auth_token = auth_response.json()["metadata"]["token"]

# Cabeçalhos com token de autenticação
headers_with_token = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {auth_token}"
}

# Obter lista de VMs
vm_response = requests.get(nutanix_url, headers=headers_with_token)
vm_response.raise_for_status()

# Imprimir informações das VMs
vms = vm_response.json()["entities"]
for vm in vms:
    print(f"Nome da VM: {vm['status']['name']}")
    print(f"ID da VM: {vm['metadata']['uuid']}")
    print(f"Estado da VM: {vm['status']['state']}")
    print("------")
