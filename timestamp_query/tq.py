import datetime
import re
import sys

from plutus import get_clipboard, set_clipboard


def ts_to_str(ts: str) -> str:
    """
    Format timestamp in seconds
    """
    ds = datetime.datetime.fromtimestamp(float(ts)).strftime("%a %d %b %Y %H:%M:%S")
    print(ds)
    return ds


def timestamp(date):
    ts = date.strftime("%s")
    return ts


def command_line_runner(argv=None):
    if argv is None:
        argv = sys.argv

    # Usage: tq [timestamp in seconds or milliseconds]
    # tq "exp_ms": "1600848628001+0000",  -> Wed 23 Sep 2020 09:10:28
    # tq 1600848628001+0000 -> Wed 23 Sep 2020 09:10:28
    # tq 1600848628001      -> Wed 23 Sep 2020 09:10:28
    # tq 1600848628         -> Wed 23 Sep 2020 09:10:28
    # tq --now
    # tq --today
    # tq --tomorrow

    if len(argv) == 1:
        ts = get_clipboard()
    elif len(argv) == 2:
        # Use argument
        ts = argv[1]
    else:
        # Use all arguments
        ts = " ".join(argv[1:])

    if ts == "--now":
        ts = timestamp(datetime.datetime.now())

    if ts == "--today":
        ts = timestamp(datetime.date.today())

    if ts == "--tomorrow":
        ts = timestamp(datetime.datetime.now() + datetime.timedelta(hours=24))

    try:
        # extract timestamp from string as 1st 10 digits found
        if matches := re.search(r"\d{10}", ts):
            seconds = matches[0]
            print(seconds)
        else:
            return 1

    except ValueError:
        # Probably not a timestamp
        return 1

    set_clipboard(ts_to_str(seconds))
    return 0


if __name__ == "__main__":
    sys.exit(command_line_runner(sys.argv))
