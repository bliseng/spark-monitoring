"""
A python library to interact with the Spark History server.
"""

def client(server, port=18080, is_https=False, api_version=1):
    """
    Method to return a client to make calls to the spark history server with.

    :param server: Hostname or IP pointing to the spark history server
    :type server: basestring
    :param port: Port which the spark history server is exposed on
    :param is_https:
    :param api_version:
    :return sparkmonitoring.api.ClientV1:
    """
    from sparkmonitoring.api import ClientV1
    return ClientV1(server, port, is_https)


def df(server, port=18080, is_https=False, api_version=1):
    from sparkmonitoring.dataframes import PandasClient
    return PandasClient(server, port, is_https, api_version)
