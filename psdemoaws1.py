import boto3
from pprint import pprint as pp
import os


# os.environ['HTTP_PROXY'] = 'http://user:passwd@isas.danskenet.net:80'
# os.environ['HTTPS_PROXY'] = 'http://user:passwd@isas.danskenet.net:80'
# HTTP_PROXY
# HTTPS_PROXY


def get_session(region):
    return boto3.session.Session(region_name=region)


def get_ec2_instances_ids(ec2_client):
    ec2_ids = []

    for reservations_info in ec2_client.describe_instances()['Reservations']:
        ec2_ids.append(reservations_info['Instances'][0]['InstanceId'])

    return ec2_ids


if __name__ == '__main__':
    session = get_session('ap-south-1')
    print(session)
    print()
    client = session.client('ec2')
    print(client)
    print()
    instances_ids = get_ec2_instances_ids(client)
    print()

    client.stop_instances(InstanceIds=instances_ids)


    #pp(get_ec2_instances_ids(client))

    # for reservations_info in client.describe_instances()['Reservations']:
    #     pp(reservations_info['Instances'][0]['InstanceId'])

    # for reservations_info in client.describe_instances()['Reservations']:
    #     for key, value in reservations_info.items():
    #         if key == 'Instances':
    #             for instance in value:
    #                 print(instance['InstanceId'])
    #
