import argparse
import itertools
import json

from dcctools.config import Configuration

c = Configuration("config.json")

parser = argparse.ArgumentParser(
    description="Tool for counting the number of perfect matches (exactly identical hashes) \
                 for one project across sites."
)
parser.add_argument(
    "-p", "--project", default="name-sex-dob-zip",
    help="Select a project to review perfect matches across sites. \
          Default: name-sex-dob-zip",
)
args = parser.parse_args()

project = args.project

print(f"COUNTING PERFECT MATCHES FOR {project}")

clks = {}
for system in c.systems:
    raw_clks = c.get_clks_raw(system, project)
    clk_json = json.loads(raw_clks)
    clks[system] = set(clk_json['clks'])
    print(f"Size of {system}: {len(clks[system])}")

total_perfect_matches = set()

for pair in itertools.combinations(c.systems, 2):
    pairwise_matches = clks[pair[0]].intersection(clks[pair[1]])
    print(f"Total perfect matches between {pair[0]} and {pair[1]}: {len(pairwise_matches)}")

    total_perfect_matches.update(pairwise_matches)  # update means add to set

print()
print(f"Total perfect matches for {project}: {len(total_perfect_matches)}")
