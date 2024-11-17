# Import library
from argparse import ArgumentParser

# Import function from Pipeline
from . import .




# Define parser
def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--per_lang', help='If true, conduct experiment language-wise')

    return parser.parse_args()


##### 구분선 #####


def main():

    return None


##### 구분선 #####
if __name__ == '__main__':
    args = parse_args()
    main(args)