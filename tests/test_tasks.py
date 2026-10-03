from tasks import add_task, is_developer_available, cancel_task


def test_add_task():
    tasks = []
    add_task(tasks, 1, "Fix bug", 5.0)
    assert len(tasks) == 1
    assert tasks[0]["developer_id"] == 1


def test_is_developer_available():
    tasks = [{"id": 1, "developer_id": 1,
              "title": "A", "estimated_hours": 60.0}]
    # max capacity is 64. Adding 5 hours should fail.
    assert not is_developer_available(tasks, 1, 5.0, 64.0)
    # Adding 4 hours should pass.
    assert is_developer_available(tasks, 1, 4.0, 64.0)


def test_cancel_task():
    tasks = [{"id": 1, "developer_id": 1,
              "title": "A", "estimated_hours": 60.0}]
    assert cancel_task(tasks, 1) is True
    assert len(tasks) == 0
