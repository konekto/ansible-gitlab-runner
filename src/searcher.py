# needs sudo rights

import argparse
import os
import toml


def search_runner(config_file, query):
    config_file_as_toml = toml.load(config_file)

    for runner in config_file_as_toml['runners']:
        runner_name_matches_query = runner['name'] == query
        if runner_name_matches_query:
            return True
    return False


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Search the Gitlab Runner config file for runner by description')
    parser.add_argument('--config', metavar='config', required=True, type=str,
                        help='the path of the Gitlab runner config')
    parser.add_argument('--query', metavar='query', required=True, type=str,
                        help='The query (description) of the runner')

    args = parser.parse_args()

    config_file = os.path.abspath(args.config)

    does_config_file_exists = not os.path.exists(args.config)
    if does_config_file_exists:
        print('No config file found. Exiting.')
        exit(1)

    print(search_runner(args.config, args.query))
    exit(0)
