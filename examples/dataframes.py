import sparkmonitoring as sparkmon

monitoring = sparkmon.df('10.91.62.6')

apps = monitoring.list_applications()

apps['function'] = apps.name.str.split('(').str.get(0)

print(apps.head().stack())

# plt.figure()
# apps['duration'].hist(by=apps['function'], figsize=(40, 20))
# plt.show()


jobs = monitoring.list_jobs(apps.iloc[0].id)

print(jobs.head().stack())
