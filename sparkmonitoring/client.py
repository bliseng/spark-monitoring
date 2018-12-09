import requests


class Client(object):
    def __init__(self, server, port=18080, is_https=False, api_version=1):
        self._server = server
        self._port = port
        self._is_https = is_https
        self._api_version = 1

    @property
    def _base_url(self):
        protocol = 'https' if self._is_https else 'http'

        return "{protocol}://{server}:{port}/api/v{version}/".format(
            protocol=protocol,
            server=self._server,
            port=self._port,
            version=self._api_version
        )

    def _do_request(self, path, params=None):
        url = self._base_url + path
        r = requests.get(url, params)

        if r.status_code != requests.codes.ok:
            r.raise_for_status()

        return r.json()

    def list_applications(self, status=None, minDate=None, maxDate=None, limit=None):
        """
        A list of all applications.

        :param status: Must be one of {'completed', 'running'}
        :param minDate: Filter earliest job with ISO-8601 format
        :param maxDate: Filter latest job with ISO-8601 format
        :param limit: Number of results to return
        :return:
        """
        return self._do_request(
            'applications',
            params={
                k: v for k, v in
                {
                    'status': status, 'minDate': minDate,
                    'maxDate': maxDate, 'limit': limit
                }.items()
                if v is not None
            }
        )

    def get_application(self, app_id):
        """
        A single application

        :param app_id: ID of the application for jobs we wish to retrieve
        :return:
        """
        return self._do_request(
            'applications/' + app_id
        )

    def list_jobs(self, app_id):
        """
        A list of all jobs for the given application.

        :param app_id: ID of the application for jobs we wish to retrieve
        :return:
        """
        return self._do_request(
            'applications/' + app_id + '/jobs'
        )

    def get_job(self, app_id, job_id):
        """
        Details for the given job.

        :param app_id: ID of the application for jobs we wish to retrieve
        :param job_id: ID of the job within the application
        :return:
        """
        return self._do_request(
            'applications/' + app_id + '/jobs/' + job_id
        )

    def list_stages(self, app_id, status=None):
        """
        A list of all stages for a given application.

        :param app_id: ID of the application for stages we wish to retrieve
        :param status:  Must be one of {'active', 'complete', 'pending', 'failed'}
        """
        return self._do_request(
            'applications/' + app_id + '/stages',
            params={} if status is None else {'status': status}
        )

    def list_stage_attempts(self, app_id, stage_id, status=None):
        """

        :param app_id: ID of the application for stages we wish to retrieve
        :param stage_id: ID of the stage to list attempts for
        :param status:  Must be one of {'active', 'complete', 'pending', 'failed'}
        :return:
        """
        return self._do_request(
            'applications/{app_id}/stages/{stage_id}'.format(
                app_id=app_id, stage_id=stage_id
            ),
            params={} if status is None else {'status': status}
        )
