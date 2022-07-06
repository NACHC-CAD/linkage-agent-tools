#!/usr/bin/env python

import argparse
import csv
from pathlib import Path

from dcctools.config import Configuration


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="config.json",
        help='Configuration file (default "config.json")',
    )
    args = parser.parse_args()
    return args


def process_csv(csv_path, system_csv_path, system):
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        with open(system_csv_path, "w", newline="") as system_csvfile:
            writer = csv.DictWriter(system_csvfile, fieldnames=["LINK_ID", system])
            writer.writeheader()
            cnt = 0
            inc = 10000
            print("Counting by " + str(inc))
            for row in reader:
                cnt = cnt + 1
                if cnt % inc == 0:
                    print("Row " + str(cnt))
                if len(row[system]) > 0:
                    writer.writerow({"LINK_ID": row["LINK_ID"], system: row[system]})
            print("Done processing rows.")


def do_data_owner_ids(c):
    if c.household_match:
        csv_path = Path(c.matching_results_folder) / "household_link_ids.csv"
    else:
        csv_path = Path(c.matching_results_folder) / "link_ids.csv"

    cnt = 0
    print("CSV Path: " + str(csv_path))
    for system in c.systems:
        cnt = cnt + 1
        print("Processing system " + str(cnt) + " of " + str(len(c.systems)))
        if c.household_match:
            system_csv_path = Path(c.output_folder) / "{}_households.csv".format(system)
        else:
            system_csv_path = Path(c.output_folder) / "{}.csv".format(system)
        print("Creating: " + str(csv_path))
        process_csv(csv_path, system_csv_path, system)
        print(f"{system_csv_path} created")


if __name__ == "__main__":
    args = parse_args()
    config = Configuration(args.config)
    do_data_owner_ids(config)
