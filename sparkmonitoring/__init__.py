def client(server, port=18080, is_https=False, api_version=1):
    """

    :param server:
    :param port:
    :param is_https:
    :param api_version:
    :return:
    """
    from sparkmonitoring.api import ClientV1
    return ClientV1(server, port, is_https)


def df(server, port=18080, is_https=False, api_version=1):
    from sparkmonitoring.dataframes import PandasClient
    return PandasClient(server, port, is_https, api_version)
