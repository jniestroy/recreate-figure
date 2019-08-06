import click
import json
import pandas as pd
import sys
import os
from io import StringIO



#@click.command()
#@click.argument('file')
def data_cleaning(file):
    file = file[1]
    data = pd.read_csv(file,engine='python')
    fig_df = data.iloc[:,[17,20,47,52]]
    s = StringIO()
    fig_df.to_csv(s)
    click.echo(s.getvalue())


if __name__ == '__main__':
    print(os.listdir())
    data_cleaning(sys.argv)
