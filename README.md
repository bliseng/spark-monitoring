# spark-monitoring

A python library to interact with the Spark History server.

## Quickstart

### Basic

```shell
$ pip install spark-monitoring
```
```python
import sparkmonitoring as sparkmon

monitoring = sparkmon.client('my.history.server')
print(monitoring.list_applications())
```

### Pandas

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

## Reference

### sparkmonitoring.client

Method to return a client to make calls to the spark history server with.

#### Arguments

| Name | Type | Description | Default |
|------|------|-------------|---------|
| `server` | `string` | Hostname or IP pointing to the spark history server | |
| `port` | `int` | Port which the spark history server is exposed on | `18080` |
| `is_https` | `bool` |  Whether or not to use https to communicate with the spark server | `False`
| `api_version` | `int` | API Version to interact with. Currently only `1` is supported | `1` |

#### Response

 - `sparkmonitoring.api.ClientV1`
 
#### Examples
_Basic Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.client('10.0.0.10')
```

_Custom Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.client('my-server', port=8080, is_https=True)
```

### sparkmonitoring.df

Method to return a client to make calls to the spark history server with. This
client will return pandas dataframes, as opposed ot dictionaries in the
standard client. Can be used when the `spark-monitoring[pandas]` extra is 
installed.

#### Arguments

| Name | Type | Description | Default |
|------|------|-------------|---------|
| `server` | `string` | Hostname or IP pointing to the spark history server | |
| `port` | `int` | Port which the spark history server is exposed on | `18080` |
| `is_https` | `bool` |  Whether or not to use https to communicate with the spark server | `False`
| `api_version` | `int` | API Version to interact with. Currently only `1` is supported | `1` |

#### Response

 - `sparkmonitoring.dataframes.PandasClient`

#### Examples
_Basic Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.df('10.0.0.10')
```

_Custom Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.df('my-server', port=8080, is_https=True)

```

### sparkmonitoring.api.ClientV1.\_\_init\_\_

A client to interact with the Spark History Server

#### Arguments

| Name | Type | Description | Default |
|------|------|-------------|---------|
| `server` | `string` | Hostname or IP pointing to the spark history server | |
| `port` | `int` | Port which the spark history server is exposed on | |
| `is_https` | `bool` |  Whether or not to use https to communicate with the spark server | | 
| `api_version` | `int` | API Version to interact with. Currently only `1` is supported | |

### sparkmonitoring.dataframes.PandasClient.\_\_init\_\_

Method to return a client to make calls to the spark history server with,
returning pandas DataFrames.

#### Arguments


| Name | Type | Description | Default |
|------|------|-------------|---------|
| `server` | `string` | Hostname or IP pointing to the spark history server | |
| `port` | `int` | Port which the spark history server is exposed on | `18080` |
| `is_https` | `bool` |  Whether or not to use https to communicate with the spark server | `False`
| `api_version` | `int` | API Version to interact with. Currently only `1` is supported | `1` |
