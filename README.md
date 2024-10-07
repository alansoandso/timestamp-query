# Plutus helper tool - Timestamp Query
Convert timestamps to human readable
### Example:

```
usage: tq [<time in seconds or milliseconds since epoch>]

        Use clipboard or supplied parameter
```

## Dependencies

- Python3
- Poetry
- zsh complete

## Installing

**Development Installation**

    poetry install
    poetry update

    # Add globally
    pipx install -e .

    # If you want to synchronize your environment – and ensure it matches the lock file – use the --sync option.
    poetry install --sync

**Testing**

    poetry shell
    pytest -v 

**Uninstalling**

    pipx uninstall timestamp-query

