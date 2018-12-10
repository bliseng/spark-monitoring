import sparkmonitoring as sparkmon

monitoring = sparkmon.client('10.91.62.6')

print(monitoring.list_applications())
