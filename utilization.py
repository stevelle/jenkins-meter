import requests
import argparse

PATH = '%s/computer/%s/api/json?depth=3'


def main(args):
    r = requests.get(PATH % (args.host_url, args.node))
    r.raise_for_status()

    body = r.json()
    busy_history = body['loadStatistics']['busyExecutors']['hour']['history']
    total_history = body['loadStatistics']['totalExecutors']['hour']['history']

    utilization = []
    for (busy, total) in zip(busy_history, total_history):
        if total == 0:
            break

        utilization.append(busy / total)

    print utilization

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Jenkins executor utilization checker')
    parser.add_argument('host_url', help='url of the Jenkins server, e.g. \
            http://builds.example.org')
    parser.add_argument('node', help='name of computer or "node" to check')
    args = parser.parse_args()
    main(args)
