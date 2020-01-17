import pytest


@pytest.fixture(scope="class")
def setup():
    print("Before test case")
    yield
    print("After test case")


@pytest.fixture()
def dataLoad():
    print("user data is being loaded")
    return ["Aruna", "Kumara S", "as3@conversantmedia.com"]


@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param

@pytest.fixture(params=[("chrome","Aruna"),("firefox","Kumara"),("IE","Srinivasa")])
def crossBrowserParam(request):
    return request.param