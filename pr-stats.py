import argparse
import requests
import json
from datetime import datetime
from user import User


def is_pull_younger(created_date: datetime, pull: json.dump) -> bool:
    open_date = datetime.strptime(pull['created_at'].split('T')[0], '%Y-%m-%d')

    return open_date < created_date


def read_token() -> str:
    """Read password/token from a file"""
    with open('credential.json') as file:
        data = json.load(file)

    return data['password']


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version',
                    help='show the script version',
                    action='version',
                    version='%(prog)s - version 1.0')

parser.add_argument('-a', '--all',
                    help='show all pull requests',
                    action='store_true')

parser.add_argument('--rate',
                    help='show merged/closed statistics',
                    action='store_true')

parser.add_argument('-p', '--pull',
                    help='Set specific pull number')

parser.add_argument('--open',
                    help='Show who opened pull request (required -p/--pull)',
                    action='store_true')

parser.add_argument('-d', '--date', type=str,
                    help='Set special date for --after/--before (format: YYYY-M(M)-D(D)')

parser.add_argument('--after',
                    help='Show pull requests after special date (requierd -d/--date)',
                    action='store_true')

parser.add_argument('--before',
                    help='Show pull requests before special date (requierd -d/--date)',
                    action='store_true')

parser.add_argument('--comments',
                    help='Show the number of comments for pull request (required -p/--pull)',
                    action='store_true')

parser.add_argument('user', type=str,
                    help='An owner of repository')

parser.add_argument('-r', '--repository', type=str,
                    help='A GitHub repository')


args = parser.parse_args()

user = User(args.user, read_token())
repo = args.repository

session = requests.Session()
session.auth = (user.name, user.token)

if args.all:
    url = f'https://api.github.com/repos/{user.name}/{repo}/pulls'
    params = {
        'state': 'all',
        'per_page': 100
    }
    pulls = session.get(url, params=params).json()
    amount = pulls[0]['number']

    if amount <= 100:
        print('You have pulls:')
        print('\n'.join(f"Pull {pull['number']} - {pull['title']}" for pull in pulls))
    else:
        print('You have pulls:')
        for number in range(1, amount + 1):
            pull = session.get(url + f'/{number}').json()
            print(f'Pull {pull["number"]} - {pull["title"]}')

if args.rate:
    url = f'https://api.github.com/repos/{user.name}/{repo}/pulls'
    params = {
        'state': 'all',
        'per_page': 100
    }
    pulls = session.get(url, params=params).json()
    amount = pulls[0]['number']

    merged = 0
    closed = 0
    if amount <= 100:
        for pull in pulls:
            if pull['merged_at']:
                merged += 1
            if pull['closed_at']:
                closed += 1

        print(f'Merged pull: {merged}, all pull: {amount}. Merged rate = {merged / amount}',
              f'Closed pull: {closed}, all pull: {amount}. Closed rate = {closed / amount}',
              sep='\n')
    else:
        for number in range(amount):
            pull = session.get(url + f'/number').json()

            if pull['merged_at']:
                merged += 1
            if pull['closed_at']:
                closed += 1

        print(f'Merged pull: {merged}, all pull: {amount}. Merged rate = {merged / amount}',
              f'Closed pull: {closed}, all pull: {amount}. Closed rate = {closed / amount}',
              sep='\n')

if args.pull and args.open:
    try:
        url = f'https://api.github.com/repos/{user.name}/{repo}/pulls/{args.pull}'
        pull = session.get(url).json()
        print(f'{pull["user"]["login"]} opened pull {args.pull}')
    except KeyError:
        print("Wrong pull number!")

if args.pull and args.comments:
    try:
        url = f'https://api.github.com/repos/{user.name}/{repo}/pulls/{args.pull}/comments'
        print(f'The pull has {len(session.get(url).json())} comment(s)')
    except KeyError:
        print("Wrong pull number!")

if args.date and args.after and not args.before:
    date = datetime.strptime(args.date, '%Y-%m-%d')

    url = f'https://api.github.com/repos/{user.name}/{repo}/pulls'
    params = {
        'state': 'all',
        'per_page': 100
    }
    pulls = session.get(url, params=params).json()
    amount = pulls[0]['number']

    if amount <= 100:
        for pull in pulls:
            if not is_pull_younger(date, pull):
                print(f'Pull {pull["number"]} - {pull["title"]} - {pull["created_at"]}')
    else:
        for number in range(1, amount + 1):
            pull = session.get(url + f'/{number}').json()

            if not is_pull_younger(date, pull):
                print(f'Pull {pull["number"]} - {pull["title"]} - {pull["created_at"]}')

if args.date and args.before and not args.after:
    date = datetime.strptime(args.date, '%Y-%m-%d')

    url = f'https://api.github.com/repos/{user.name}/{repo}/pulls'
    params = {
        'state': 'all',
        'per_page': 100
    }
    pulls = session.get(url, params=params).json()
    amount = pulls[0]['number']

    if amount <= 100:
        for pull in pulls:
            if is_pull_younger(date, pull):
                print(f'Pull {pull["number"]} - {pull["title"]} - {pull["created_at"]}')
    else:
        for number in range(1, amount + 1):
            pull = session.get(url + f'/{number}').json()

            if is_pull_younger(date, pull):
                print(f'Pull {pull["number"]} - {pull["title"]} - {pull["created_at"]}')
