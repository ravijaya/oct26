import re
import matplotlib.pyplot as plt

import pprint

# ipv4 address
pattern = r'\b(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.){3}'
pattern += r'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\b'


def get_ip_address_frequency():
    ip_addr_count = {}

    for line in open('messages'):
        m = re.search(pattern, line)
        if m:
            ip_v4_addr = m.group()
            ip_addr_count[ip_v4_addr] = ip_addr_count.get(ip_v4_addr, 0) + 1

    return ip_addr_count


def separate_count_ip_address():
    ip_address_count = get_ip_address_frequency()

    content = [(count, ip_addr) for ip_addr, count in ip_address_count.items()]
    content = sorted(content)

    ip_counts = [item[0] for item in content[-15:]]
    ip_addrs = [item[1] for item in content[-15:]]
    return ip_counts, ip_addrs


def plot_pie_chart(list_of_addr, list_of_counts):
    """plot pie char"""

    plt.pie(list_of_counts, labels=list_of_addr, startangle=90, autopct='%.1f%%')
    plt.title("Frequency By IP Address")
    plt.savefig('ip_pie.png')
    # plt.show()


def plot_bar_chart(list_of_addr, list_of_counts):
    """plot bar chart"""

    x_pos = range(len(list_of_addr))

    plt.bar(x_pos, list_of_counts)
    plt.xticks(x_pos, list_of_addr, rotation=90)  # mark label on x-axis
    plt.xlabel('IP Address')
    plt.ylabel('Counts')

    plt.title("Frequency By IP Address")

    plt.savefig('ip_bar.png')
    # plt.show()


counts, addrs = separate_count_ip_address()
# plot_pie_chart(addrs, counts)
plot_bar_chart(addrs, counts)
