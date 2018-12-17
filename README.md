## spark-monitoring

A python library to interact with the Spark History server.

### Quickstart

#### Basic

```shell
$ pip install spark-monitoring
```
```python
import sparkmonitoring as sparkmon

monitoring = sparkmon.client('my.history.server')
print(monitoring.list_applications())
```

#### Pandas

```shell
$ pip install spark-monitoring[pandas]
```

```python
import sparkmonitoring as sparkmon
import matplotlib.pyplot as plt

monitoring = sparkmon.df('my.history.server')

apps = monitoring.list_applications()
apps['function'] = apps.name.str.split('(').str.get(0)
print(apps.head().stack())

plt.figure()
apps['duration'].hist(by=apps['function'], figsize=(40, 20))
plt.show()

jobs = monitoring.list_jobs(apps.iloc[0].id)

print(jobs.head().stack())
```
