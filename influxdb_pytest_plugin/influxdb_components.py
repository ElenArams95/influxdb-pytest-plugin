import configparser

from influxdb import InfluxDBClient


class Influxdb_Components():
    _client = None
    config = configparser.RawConfigParser()
    config.read('resources/configuration_file')

    def __init__(self, host, port, db_user, db_password, db_name):
        self._client = InfluxDBClient(host, port, db_user, db_password, db_name)

    def get_client(self):
        return self._client

    def get_json(self, measurement_name, test_result_dto):
        json_body = [
            {
                "measurement": measurement_name,
                "tags": {
                    "run": str(test_result_dto.get_run()),
                    "project": str(test_result_dto.get_project()),
                    "version": str(test_result_dto.get_version())
                },
                "fields": {
                    "test": str(test_result_dto.get_test()),
                    "status": str(test_result_dto.get_status()),
                    "screenshot": str(test_result_dto.get_screenshot()),
                    "duration_sec": int(test_result_dto.get_duration_sec()),
                    "exception": str(test_result_dto.get_exception())
                }
            }
        ]
        return json_body
