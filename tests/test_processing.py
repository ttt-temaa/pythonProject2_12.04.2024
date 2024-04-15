import pytest

from src.processing import filter_by_state, sort_dicts_by_date


@pytest.fixture
def input_data() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(input_data: list) -> None:
    filtered_data_executed = filter_by_state(input_data)
    assert filtered_data_executed == input_data[:2]

    filtered_data_canceled = filter_by_state(input_data, "CANCELED")
    assert filtered_data_canceled == input_data[2:]


def test_sort_dicts_by_date(input_data: list) -> None:
    sorted_descending = sort_dicts_by_date(input_data, True)
    assert sorted_descending == sorted(input_data, key=lambda x: (x["date"], "%Y-%m-%dT%H:%M:%S.%f"))[::-1]

    sorted_ascending = sort_dicts_by_date(input_data, False)
    assert sorted_ascending == sorted(input_data, key=lambda x: (x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
