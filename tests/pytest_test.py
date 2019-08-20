import pytest

class TestClass(object):

    @pytest.fixture(autouse=True)
    def resource(self):
        yield

    def test_any_test(self, request):
        name = request.node.name
        assert name == 'test_any_test'

    def test_any_test2(self, request):
        name = request.node.name
        assert name == 'test_any_test2'

    def test_any_test3(self, request):
        name = request.node.name
        assert name == 'test_any_test3'

    def test_any_test4(self, request):
        name = request.node.name
        assert name == 'test_any_test4'


    def test_any_test5(self, request):
        name = request.node.name
        assert name == 'test_any_test4'


    def test_any_test7(self, request):
        name = request.node.name
        assert name == 'test_any_test7'

    def test_any_test8(self, request):
        name = request.node.name
        assert name == 'test_any_test9'