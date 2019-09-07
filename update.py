import glob
import os
import subprocess
import time
import requests
import re
import sys

# staging
path = '/coding/coding-staging-k8s/service/'
kubectl_path = 'kubectl --kubeconfig /coding/yjk-repo/bak-files/staging-config'

# online
# path = '/coding/qcloud-ops/kubernetes/services/'
# kubectl_path = 'kubectl --kubeconfig /coding/yjk-repo/bak-files/online-config'



def get_path(service_name):
    """传入服务名，返回完整路径"""
    for file in glob.glob('{path}/*/*.y*ml'.format(path=path), recursive=True):
        name = os.path.splitext(os.path.basename(file))[0]
        if service_name == name and (file.count('coding-job') != 1):
            return file


def health_check(service_name):
    """传入服务名，检测服务是否更新完毕"""
    kubectl_cmd = "%s get pods |grep  %s|awk '{print $2}'|uniq -c|wc -l" % (kubectl_path, service_name)
    # status = int(subprocess.check_output(kubectl_cmd, shell=True).decode('utf-8'))
    status = int(1)
    if status == 1:
        print('%s 已更新完毕!' % (service_name))
        print('-' * 40)
        return True
    else:
        print('%s 正在更新中...' % (service_name))
        return False


def update(service_name):
    """传入服务名，执行更新操作"""
    update_cmd = "%s apply -f %s" % (kubectl_path, get_path(service_name))
    print('正在执行更新 %s' % (service_name))
    print(update_cmd)
    # subprocess.check_output(update_cmd,shell=True)


def login():
    """登录"""
    login_url = 'https://codingcorp.coding.net/api/v2/account/login'
    post_data = {
        'account': 'yangjingkai@coding.net',
        'password': 'befbc48ba52f0842da019507001ae8b0dbdb0835',
        'enterprise_key': 'codingcorp',
        'feie_password': 'SGUxMTB3b3JsZC4u',
    }

    with requests.Session() as session:
        session.post(login_url, data=post_data)
        return session


def services(text):
    '''传入字符串，获取所有更新的服务，返回服务列表'''
    pat = re.compile('[a-z]+.*2019.*\\d+')
    services = []
    for i in pat.findall(text):
        a = i.split('|')[0].strip()
        services.append(a)
    return services


def main(services):
    for service_name in services:
        update(service_name)
        while True:
            if health_check(service_name):
                break
            else:
                time.sleep(10)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('输入 tag 重新执行')
        exit()
    tag = sys.argv[1]
    url = 'https://codingcorp.coding.net/api/user/codingcorp/project/coding-dev/depot/coding-dev/git/releases/tag/%s'%(tag)
    try:
        text = login().get(url).json()['data']['body']
    except KeyError as e:
        print('tag 输入错误，请重新输入！')
        exit()
    for item in services(text):
        print(item)
    action = input('将要更新以上服务共 %d 个，是否执行 y/n : ' % (len(services(text))))
    if action.lower() == 'y':
        print('ok')
        main(services(text))
    elif action.lower() == 'n':
        print('已放弃更新！')
        exit()
    else:
        print('输入错误，退出！')
