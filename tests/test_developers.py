from developers import (
    add_developer, find_developer,
    calculate_developer_capacity)


def test_add_developer():
    devs = []
    add_developer(devs, "Дамир", "Backend", 64.0)
    assert len(devs) == 1
    assert devs[0]["name"] == "Дамир"
    assert devs[0]["id"] == 1


def test_find_developer():
    devs = [
        {"id": 1, "name": "Дамир", "role": "Backend", "max_capacity": 64.0}
    ]
    res = find_developer(devs, "дам")
    assert len(res) == 1
    assert res[0]["name"] == "Дамир"


def test_calculate_capacity():
    cap = calculate_developer_capacity(10, 8, 0.2)
    assert cap == 64.0
