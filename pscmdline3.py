"""cli tools"""

import optparse
import os


def main():
    p = optparse.OptionParser()

    p.add_option('--file', '-f', action='store_true', default=False, help="a sample option", )
    p.add_option('--sample', '-s', action='store_true', default=False, help="a sample option")

    options, arguments = p.parse_args()

    print(options, arguments)


if __name__ == '__main__':
    main()
