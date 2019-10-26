import optparse
# import click


def main():
    p = optparse.OptionParser()
    p.add_option('--line-no', '-n', action='store_true', default=False, help='print with line number')

    options, args = p.parse_args()

    # print(options, args)
    print(options.line_no)

    for file_name in args:
        line_number = 1

        for line in open(file_name):
            if options.line_no:
                line = f'{line_number}  {line}'
                line_number += 1

            print(line, end='')


if __name__ == '__main__':
    main()
