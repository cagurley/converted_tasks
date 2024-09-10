"""
Fetcher main
"""

import datetime as dt
import os
import act
import sat
from support import log, plog
import toefl


def main():
    try:
        plog(f'Fetcher booted from disk at {dt.datetime.now().astimezone()}')
        current = dt.datetime.now().astimezone()
        act.fetch()
        sat.fetch(current)
        with open('toefl.dat') as f:
            last = dt.datetime.strptime(f.read().strip(), '%Y-%m-%d').date()
            if current.date() > last:
                toefl.fetch(last, current.date())
        current = dt.datetime.now().astimezone()
        plog(f'Cycle ended at {current}')
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
