from datetime import datetime

from src.decorators import log


@log("logging.txt")
def prog(x: int, y: int) -> int:
    return x + y


@log()
def g(x: int, y: int) -> int:
    return x + y


def test_log_file_correct() -> None:
    prog(1, 3)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logging.txt", "r", encoding="utf8") as f:
        assert f.readlines()[-1].strip() == f"{date} prog ok"


def test_log_file_error() -> None:
    prog("1", 4)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logging.txt", "r", encoding="utf8") as f:
        assert (
            f.readlines()[-1].strip()
            == f"{date} prog error: can only concatenate str (not \"int\") to str. Inputs: ('1', 4), {{}}"
        )


def test_correct() -> None:
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert g(1, 2) == (3, f"{date} g ok")


def test_error() -> None:
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert g("1", 4) == f"{date} g error: can only concatenate str (not \"int\") to str. Inputs: ('1', 4), {{}}"
