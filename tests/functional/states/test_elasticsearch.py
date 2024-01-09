import pytest

pytestmark = [
    pytest.mark.requires_salt_states("elasticsearch.exampled"),
]


@pytest.fixture
def elasticsearch(states):
    return states.elasticsearch


def test_replace_this_this_with_something_meaningful(elasticsearch):
    echo_str = "Echoed!"
    ret = elasticsearch.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
