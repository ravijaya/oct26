def get_user_list(data_file):
    try:
        user_list = []

        for line in open(data_file):
            login = line.split(':')[0]
            user_list.append(login)

        line_no = 1
        fw = open('passwd.dat', 'w')

        for user in sorted(user_list):
            content = f'{line_no}, {user}'  # formatted string
            print(content)
            fw.write(content + '\n')
            line_no += 1

        fw.close()
    except (FileNotFoundError, IOError) as error:
        print(error)


if __name__ == '__main__':
    get_user_list('passwd.txt')
