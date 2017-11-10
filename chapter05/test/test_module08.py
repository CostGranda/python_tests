import pytest

@pytest.fixture()
def fixture01(request):
    print("\nIn fixture01()...")
    print("Fixture Scope: "+ str(request.scope))
    print("Function Name: "+ str(request.function.__name__))
    print("Class Name: "+ str(request.cls))
    print("Module Name: "+ str(request.cls))
    print("File Path: "+ str(request.fspath))

@pytest.mark.usefixtures('fixture01')
def test_case01(fixture01):
    print("\nIn test_case01()...")
