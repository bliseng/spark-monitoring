from sparkmonitoring.client import Client

monitoring = Client('10.91.62.6')

print(monitoring.list_applications())
