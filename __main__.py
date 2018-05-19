import paramiko.rsakey
from paramiko import Transport
import paramiko.sftp_client as sftp
import json
import sys
import os
from urllib.request import urlopen
import cgi


with open(os.path.join(os.path.dirname(__file__), 'settings.json'), 'rt') as f:
    settings = json.load(f)


def mx(src: str):
    spl = src.split(':')
    if len(spl) != 2:
        raise BaseException('Invalid url')
    map_id = spl[1]
    print('Downloading from MX: {}'.format(map_id))
    with urlopen('https://tm.mania-exchange.com/tracks/download/{}'.format(map_id)) as res:
        _, params = cgi.parse_header(res.headers.get('Content-Disposition', ''))
        filename = params.get('filename', '{}.Map.Gbx'.format(map_id))
        data = res.read()
    t = Transport((settings['host'], settings['port']))
    print('Connecting')
    t.connect(username=settings['user'], pkey=paramiko.rsakey.RSAKey.from_private_key_file(settings['pkey']))
    print('Connected')
    client = sftp.SFTPClient.from_transport(t)
    print('Uploading file')
    dst = settings['dest']
    with client.open('{}/{}'.format(dst, filename), 'wb') as file:
        file.write(data)
    print('Done')
    client.close()
    t.close()


def main():
    if len(sys.argv) < 2:
        print('Usage: {} <map file>'.format(sys.argv[0]))
        raise BaseException('')
    src = sys.argv[1]
    if not os.path.isfile(src):
        if src.startswith('mxupload:'):
            mx(src)
            return
        print('File not found {}'.format(src))
        raise BaseException('')
    t = Transport((settings['host'], settings['port']))
    print('Connecting')
    t.connect(username=settings['user'], pkey=paramiko.rsakey.RSAKey.from_private_key_file(settings['pkey']))
    print('Connected')
    client = sftp.SFTPClient.from_transport(t)
    print('Uploading file')
    dst = settings['dest']
    client.put(sys.argv[1], '{}/{}'.format(dst, os.path.basename(src)))
    print('Done')
    client.close()
    t.close()


if __name__ == '__main__':
    try:
        main()
    except BaseException as ex:
        print(ex)
        input('')
