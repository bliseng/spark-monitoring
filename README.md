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

## Proxies

If your Spark history server is behind a proxy, you can connect using the `http_proxy` and 
`https_proxy` environment variables. 

## GCP

To connect to dataproc History Server, create an SSH tunnel using a local port as 
described in [Cluster web interfaces](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces) documentation
and then use the environment variables as above. 

**Note**: Use the IP for the cluster master node, as the google short names will not resolve
through the socks proxy.

### Example

```bash
gcloud compute ssh my-cluster-m \
  --project=my-project \
  --zone=us-east4-a -- -D 1080 -N

http_proxy="socks5://localhost:1080" \
    https_proxy="socks5://localhost:1080" \
    python my_spark_history_script.py
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

 - [`sparkmonitoring.api.ClientV1`](#sparkmonitoringapiclientv1)
 
#### Examples
_Basic Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.client('my.history.server')
```

_Custom Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.client('my.history.server', port=8080, is_https=True)
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

 - [`sparkmonitoring.dataframes.PandasClient`](#sparkmonitoringdataframespandasclient)

#### Examples
_Basic Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.df('my.history.server')
```

_Custom Endpoint_
```python
import sparkmonitoring as sparkmon
client = sparkmon.df('my.history.server', port=8080, is_https=True)

```

### sparkmonitoring.api.ClientV1

A client to interact with the Spark History Server.
Generally this class is not instantiated directly, and is accessed via
[`sparkmonitoring.client(...)`](#sparkmonitoringclient).

#### Arguments

| Name | Type | Description | Default |
|------|------|-------------|---------|
| `server` | `string` | Hostname or IP pointing to the spark history server | |
| `port` | `int` | Port which the spark history server is exposed on | |
| `is_https` | `bool` |  Whether or not to use https to communicate with the spark server | | 
| `api_version` | `int` | API Version to interact with. Currently only `1` is supported | |

#### Methods

 - [`list_applications(...)`](#sparkmonitoringdataframespandasclientlist_applications)
 - `get_application(...)`
 - `list_jobs(...)`
 - `get_job(...)`
 - `list_stages(...)`
 - `list_stage_attempts(...)`
 - `get_stage_attempt(...)`
 - `get_stage_attempt_summary(...)`
 - `get_stage_attempt_tasks(...)`
 - `list_active_executors(...)`
 - `list_executor_threads(...)`
 - `list_all_executors(...)`

### sparkmonitoring.dataframes.PandasClient.list_applications

A list of all applications.

#### Arguments

| Name | Type | Description | Default |
|------|------|-------------|---------|
| `status` | `enum{'completed','running'}` | Type of applications to return |
| `minDate` | `string{ISO8601}` | Earliest Application |
| `maxDate` | `string{ISO8601}` | Latest Application |
| `limit` | `int` | Number of results to return |

### sparkmonitoring.dataframes.PandasClient

A client to interact with the Spark History Server, returning pandas
DataFrames.
Generally this class is not instantiated directly, and is accessed via
[`sparkmonitoring.df(...)`](#sparkmonitoringdf).

#### Arguments


| Name | Type | Description | Default |
|------|------|-------------|---------|
| `server` | `string` | Hostname or IP pointing to the spark history server | |
| `port` | `int` | Port which the spark history server is exposed on | `18080` |
| `is_https` | `bool` |  Whether or not to use https to communicate with the spark server | `False`
| `api_version` | `int` | API Version to interact with. Currently only `1` is supported | `1` |

#### Methods

 - `list_applications(...)`
 - `get_application(...)`
 - `list_jobs(...)`
 - `get_job(...)`
 - `list_stages(...)`
