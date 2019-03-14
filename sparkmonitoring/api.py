import requests

from sparkmonitoring.responsetype import ResponseType


class BaseClient(object):
    def __init__(self, server, port, is_https, api_version):
        self._server = server
        self._port = port
        self._is_https = is_https
        self._api_version = api_version

    @property
    def _base_url(self):
        protocol = 'https' if self._is_https else 'http'

        return "{protocol}://{server}:{port}/api/v{version}/".format(
            protocol=protocol,
            server=self._server,
            port=self._port,
            version=self._api_version
        )

    def _do_request(self, path, params=None, response_type=ResponseType.JSON):
        url = self._base_url + path
        r = requests.get(url, params)

        if r.status_code != requests.codes.ok:
            r.raise_for_status()

        if response_type == ResponseType.JSON:
            return r.json()
        else:
            return r.content


class ClientV1(BaseClient):
    """
    Interact with
    """

    def __init__(self, server, port, is_https):
        super().__init__(server, port, is_https, 1)

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
        A list of attempts for a given stage

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

    def get_stage_attempt(self, app_id, stage_id, attempt_id):
        """
        A single attempt for a given stage

        :param app_id: ID of the application for stages we wish to retrieve
        :param stage_id: ID of the stage to list attempts for
        :param attempt_id: ID of the stage attempt to get
        :return:
        """
        return self._do_request(
            'applications/{app_id}/stages/{stage_id}/{attempt_id}'.format(
                app_id=app_id, stage_id=stage_id, attempt_id=attempt_id
            )
        )

    def get_stage_attempt_summary(self, app_id, stage_id, attempt_id):
        """
        Summary metrics for a single attempt for a given stage

        :param app_id: ID of the application for stages we wish to retrieve
        :param stage_id: ID of the stage to list attempts for
        :param attempt_id: ID of the stage attempt to get
        :return:
        """
        return self._do_request(
            'applications/{app_id}/stages/{stage_id}/{attempt_id}/taskSummary'.format(
                app_id=app_id, stage_id=stage_id, attempt_id=attempt_id
            )
        )

    def get_stage_attempt_tasks(self, app_id, stage_id, attempt_id,
                                offset=None, length=None, sortBy=None):
        """
        A list of all tasks for a stage attempt

        :param app_id: ID of the application for stages we wish to retrieve
        :param stage_id: ID of the stage to list attempts for
        :param attempt_id: ID of the stage attempt to get
        :param offset: Offset for tasks to return
        :param length: Number of tasks to return as an integer
        :param sortBy: Must be one of {runtime, -runtime}.
        :return:
        """
        args = {}
        if offset or length:
            args['offset'] = offset
            args['length'] = int(length)
        if sortBy is not None:
            args['sortBy'] = sortBy
        return self._do_request(
            'applications/{app_id}/stages/{stage_id}/{attempt_id}/taskList'.format(
                app_id=app_id, stage_id=stage_id, attempt_id=attempt_id
            ),
            args
        )

    def list_active_executors(self, app_id):
        """
        Get a list of all active executors for a given application

        :param app_id: ID of the application for stages we wish to retrieve
        :return:
        """
        return self._do_request(
            'applications/{app_id}/executors'.format(
                app_id=app_id
            )
        )

    def list_executor_threads(self, app_id, executor_id):
        """
        Get a list of threads for an executor for a given application

        :param app_id: ID of the application for executors we wish to retrieve
        :return:
        """
        return self._do_request(
            'applications/{app_id}/executors/{executor_id}/threads'.format(
                app_id=app_id, executor_id=executor_id
            )
        )

    def list_all_executors(self, app_id):
        """
        Get a list of all active and dead executors

        :param app_id: ID of the application for executors we wish to retrieve
        :return:
        """
        return self._do_request(
            'applications/{app_id}/allexecutors'.format(
                app_id=app_id
            )
        )

    def get_logs(self, app_id):
        """
        Get a zipped file containing all the logs of the application.

        :param app_id: ID of the application for logs we wish to retrieve
        """
        return self._do_request(
            'applications/{app_id}/logs'.format(
                app_id=app_id
            ),
            response_type=ResponseType.RAW
        )
