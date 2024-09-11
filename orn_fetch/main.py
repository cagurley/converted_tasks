"""
Fetcher main
"""

import comevo
import datetime as dt
import os
from support import log, plog


def main():
    try:
        plog(f'Fetcher booted from disk at {dt.datetime.now().astimezone()}')
        with open('last.dat') as file:
            last = file.readline().strip()
        current = dt.datetime.now().astimezone()
        plog(f'Cycle begun at {current}')
        downloads = comevo.fetch(current, last)
        if downloads:
            db_hooks = comevo.init(current)
            if db_hooks:
                comevo.replace(downloads, db_hooks[1])
                comevo.end(*db_hooks)
        with open('last.dat', 'w') as file:
            file.write(dt.datetime.strftime(current, '%Y-%m-%dT%H:%M:%S%z') + '\n')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except KeyboardInterrupt:
        plog(f'Fetcher terminated via keyboard interrupt at {dt.datetime.now().astimezone()}')
    finally:
        return None


if __name__ == '__main__':
    main()
