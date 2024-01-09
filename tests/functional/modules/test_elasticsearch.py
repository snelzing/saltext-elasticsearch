import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("elasticsearch.example_function"),
]


@pytest.fixture
def elasticsearch(modules):
    return modules.elasticsearch


def test_replace_this_this_with_something_meaningful(elasticsearch):
    echo_str = "Echoed!"
    res = elasticsearch.example_function(echo_str)
    assert res == echo_str
