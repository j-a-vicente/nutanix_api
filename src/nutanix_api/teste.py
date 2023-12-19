from nutanix_api import NutanixApiClient, NutanixVM, NutanixCluster
import requests

client = NutanixApiClient("admin-abelardo", "Drv962324", 9440, "https://10.0.17.42")
requests.packages.urllib3.disable_warnings()
# Virtual Machine
vm = NutanixVM.get(client, "7a190fbc-138c-471a-a8b7-18109b07bdc5")
print(vm.name)
#vm.turn_off()  # Turn VM off 
#vm.turn_on()  # Turn VM on

# Cluster
#cluster = NutanixCluster.get(client, "7a190fbc-138c-471a-a8b7-18109b07bdc5")
#print(cluster.name)
