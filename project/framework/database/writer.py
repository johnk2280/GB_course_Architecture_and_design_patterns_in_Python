import csv
from pathlib import Path

from settings import PATH_TO_DATABASE


def write_to_csv(
        data: dict,
        path: Path = PATH_TO_DATABASE,
        file_name: str = 'user_appeal',

) -> None:
    try:
        with open(path.joinpath(f'{file_name}.csv'), 'a', encoding='utf-8') as f:
            order = ['theme', 'first_name', 'last_name', 'email', 'text']
            writer = csv.DictWriter(f, fieldnames=order)
            writer.writerow({
                'theme': data['theme'][0],
                'first_name': data['first_name'][0],
                'last_name': data['last_name'][0],
                'email': data['email'][0],
                'text': data['text'][0],
            })
    except KeyError:
        pass


if __name__ == '__main__':
    obj = {'theme': ['2'], 'first_name': ['AEFBCG'],
            'last_name': ['zdfdzf'], 'email': ['vasia@g.com'],
            'text': ['Sd vsdSdacdaумаыымыак']}

    write_to_csv(obj)
