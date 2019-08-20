import pytest

from influxdb_pytest_plugin.influxdb_components import Influxdb_Components
from influxdb_pytest_plugin.test_result_DTO import TestResultDTO

test_result_dto_dict = dict()


@pytest.fixture()
def get_influxdb(db_host, db_port, db_name, db_user, db_password):
    influxdb_components = Influxdb_Components(db_host, db_port, db_user, db_password, db_name)
    return influxdb_components


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    report = __multicall__.execute()
    setattr(item, "rep_" + report.when, report)
    return report


@pytest.fixture(scope='function', autouse=True)
def test_result(request, run_id, pytestconfig, db_measurement_name, get_influxdb):
    if pytestconfig.getoption('--influxdb-pytest'):
        test_name = request.node.nodeid
        test_result_dto_dict.update({test_name: TestResultDTO()})
        test_result_dto = test_result_dto_dict.get(test_name)
        test_result_dto.set_test(test_name)

        def fin():
            report_outcome = request.node.rep_call
            test_result_dto.set_run(run_id)
            test_result_dto.set_duration_sec(report_outcome.duration)
            test_result_dto.set_status(report_outcome.outcome)
            influxdb_components = get_influxdb
            test_json = influxdb_components.get_json(db_measurement_name, test_result_dto)
            influxdb_components.get_client().write_points(test_json)
            print(influxdb_components.get_client().query(
                'SELECT * from ' + db_measurement_name))

        request.addfinalizer(fin)


def pytest_exception_interact(node, call, report):
    if report.failed:
        test_name = node.nodeid
        test_result_dto = test_result_dto_dict.get(test_name)
        if test_result_dto is not None:
            stack_trace = node.repr_failure(call.excinfo)
            test_result_dto.set_exception(stack_trace)


def pytest_addoption(parser):
    group = parser.getgroup('influxdb-pytest')
    group.addoption("--influxdb-pytest", action="store_true",
                    help="influxdb-pytest: enable influxdb data collection")
    parser.addoption(
        "--run_id", action="store", default=None, help="my option: run_id"
    )
    parser.addoption(
        "--db_host", action="store", default=None, help="my option: db_host"
    )
    parser.addoption(
        "--db_port", action="store", default=None, help="my option: db_port"
    )
    parser.addoption(
        "--db_user", action="store", default=None, help="my option: db_username"
    )
    parser.addoption(
        "--db_password", action="store", default=None, help="my option: db_password"
    )
    parser.addoption(
        "--db_name", action="store", default=None, help="my option: db_name"
    )
    parser.addoption(
        "--db_measurement_name", action="store", default=None, help="my option: db_measurement_name"
    )


@pytest.fixture
def run_id(request):
    return request.config.getoption("--run_id")


@pytest.fixture
def db_host(request):
    return request.config.getoption("--db_host")


@pytest.fixture
def db_port(request):
    return request.config.getoption("--db_port")


@pytest.fixture
def db_user(request):
    return request.config.getoption("--db_user")


@pytest.fixture
def db_password(request):
    return request.config.getoption("--db_password")


@pytest.fixture
def db_name(request):
    return request.config.getoption("--db_name")


@pytest.fixture
def db_measurement_name(request):
    return request.config.getoption("--db_measurement_name")
