import logging

from timestamp_query.tq import command_line_runner, ts_to_str

logger = logging.getLogger(__name__)


def test_not_timestamp():
    assert command_line_runner("tq tq".split()) == 1


def test_now():
    assert command_line_runner("tq --now".split()) == 0


def test_today():
    assert command_line_runner("tq --today".split()) == 0


def test_tomorrow():
    assert command_line_runner("tq --tomorrow".split()) == 0


def test_with_offset():
    assert command_line_runner("tq 1600848628001+0000".split()) == 0
