import pandas as pd
from pandas.io.json import json_normalize

from sparkmonitoring.client import Client


class PandasClient(Client):
    def __init__(self, server, port=18080, is_https=False, api_version=1):
        super().__init__(server, port, is_https, api_version)

    def _melt_apps(self, app_df):
        df = json_normalize(
            app_df,
            'attempts',
            ['id', 'name']
        ).set_index('id', drop=False)
        df['sparkUser'] = df['sparkUser'].astype('category')
        df['duration'] = pd.to_timedelta(df['duration'], unit='ms')

        for col in ['startTime', 'endTime', 'lastUpdated']:
            df[col] = pd.to_datetime(df[col + 'Epoch'], unit='ms')
            df.drop(col + 'Epoch', inplace=True, axis=1)
        return df

    def list_applications(self, status=None, minDate=None, maxDate=None, limit=None):
        return self._melt_apps(
            super().list_applications(status, minDate, maxDate, limit)
        )

    def get_application(self, app_id):
        return self._melt_apps(
            super().get_application(app_id)
        )

    def _melt_jobs(self, jobs_df):
        df = json_normalize(
            jobs_df
        ).set_index('jobId', drop=False)
        df['status'] = df['status'].astype('category')
        for col in ['submissionTime', 'completionTime']:
            df[col] = pd.to_datetime(df[col])
        return df.sort_index()

    def list_jobs(self, app_id):
        return self._melt_jobs(
            super().list_jobs(app_id)
        )

    def get_job(self, app_id, job_id):
        return self._melt_jobs(
            super().get_job(app_id, job_id)
        )

    def list_stages(self, app_id, status=None):
        data = super().list_stages(app_id, status)
        return data
