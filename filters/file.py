import argparse
import fnmatch
import json
import os
import sys


def filter(args):
    debug = bool(os.getenv("DEBUG", default=False))
    eventFile = os.getenv("GITHUB_EVENT_PATH")
    try:
        with open(eventFile, mode="r", encoding="utf-8") as file:
            filechanges = []
            event = json.load(file)
            for commit in event["commits"]:
                filechanges = [
                    *filechanges,
                    *commit["added"],
                    *commit["modified"],
                    *commit["removed"],
                ]
            for filechange in filechanges:
                for pattern in args.patterns:
                    if debug:
                        print(f"Comparing {filechange} to {pattern}")
                    if fnmatch.fnmatch(filechange, pattern):
                        if debug:
                            print(
                                f"Found match: {filechange} <-> {pattern}\nReturning...")
                        return 0
            if debug:
                print("No match")
            return 78
    except IOError:
        print(eventFile, "not found")
        return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("patterns", metavar="P", type=str,
                        nargs="+", help="patterns to match")
    return filter(parser.parse_args())


if __name__ == "__main__":
    sys.exit(main())
