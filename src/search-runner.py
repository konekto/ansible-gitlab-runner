# needs sudo rights

import argparse
import toml
import os

parser = argparse.ArgumentParser(description='Search the Gitlab Runner config file for runner by description')
parser.add_argument('--config', metavar='config', required=True, type=str, help='the path of the Gitlab runner config')
parser.add_argument('--query', metavar='query', required=True, type=str, help='The query (description) of the runner')

args = parser.parse_args()

config_file = os.path.abspath(args.config)

does_config_file_exists = not os.path.exists(args.config)
if does_config_file_exists:
    print('No config file found. Exiting.')
    exit(1)

config_file_as_toml = toml.load(config_file)

for runner in config_file_as_toml['runners']:
    runner_name_matches_query = runner['name'] == args.query
    if runner_name_matches_query:
        print('True')
        exit(0)

