"""
Fetcher main
"""

import csv
import datetime as dt
import os
import func


def main():
    try:
        # Startup
        cwd = os.getcwd()
        root = os.path.join(cwd, '.vars')
        with open(os.path.join(root, 'args.dat')) as file:
            fm_args = file.read().strip()
        logfile = os.path.join(cwd, 'log.txt')
        if not os.path.exists(logfile):
            with open(logfile, 'w'):
                pass
        cyclefile = os.path.join(cwd, 'last.dat')
        if not os.path.exists(cyclefile):
            with open(cyclefile, 'w') as f:
                pass

        # Main loop
        func.plog(logfile, f"Modifier booted from disk at {func.get_now_str()}")
        with open('last.dat') as file:
            last = file.readline().strip()
        last = dt.datetime.strptime(last, "%c")
        current = func.get_now()
        func.plog(logfile, f"Cycle begun at {current.strftime('%c')}")
        for item in os.scandir(fm_args):
            if item.is_file() and dt.datetime.fromtimestamp(item.stat().st_mtime) > last and item.name.endswith(".txt"):
                with open(item, newline = "") as f:
                    r = csv.reader(f)
                    with open(f"{item.path.rstrip('.txt')}_MOD.csv", "w", newline="") as nf:
                        w = csv.writer(nf)
                        for row in r:
                            w.writerow([*row[:15], row[14], row[14], row[14], *row[15:]])
                func.plog(logfile, f"Successfully modified file at {item.path}")
        with open('last.dat', 'w') as file:
            file.write(func.get_now_str())
        func.clear()
    except KeyboardInterrupt:
        func.plog(logfile, f"Fetcher terminated via keyboard interrupt at {func.get_now_str()}")


if __name__ == '__main__':
    main()
