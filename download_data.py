import requests
import json
from zipfile import ZipFile
import argparse

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    zf = ZipFile(save_path)
    zipinfos = zf.infolist()
    for ind, zipinfo in enumerate(zipinfos):
        zipinfo.filename = save_path.replace('.zip', f'_{ind}.json')
        zf.extract(zipinfo)
    zf.close()

def main(args):
    url = 'https://api.fda.gov/download.json'
    data = requests.get(url).json()['results']
    urls = []
    fsizes = 0
    substring = args.year+args.quarter
    for part in data['drug']['event']['partitions']:
        urld = part['file']
        if substring in urld:
            urls.append(urld)
            fsizes += float(part['size_mb'])
        
    print(f'Downloading {len(urls)} files containing {fsizes} Mb')

    for i, url in enumerate(urls):
        print(f'Downloading {url}')
        download_url(url, f'{args.output}/{args.year}_part_{i}.zip')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', default='2022', required=False)
    parser.add_argument('--quarter', default='q1', required=False)
    parser.add_argument('--output', default='./data/', required=False)

    args = parser.parse_args()
    
    main(args)
    
