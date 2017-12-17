import argparse
import sys
import os
import time
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, help='Url to download file from')
parser.add_argument('--dir', type=str, default='./', help='Directory to store the file.')

URLs = [
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/DP.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MC-TD.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/control.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/FA.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/pg.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/dyna.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/XX.pdf',
    'http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/games.pdf'
]


def maybe_download_data(url):
    filename = url.split('/')[-1]
    filepath = os.path.join(FLAGS.dir, filename)
    if not os.path.exists(filepath):
        tic = time.time()

        def _progress(count, block_size, total_size):
            nonlocal tic
            if count % 20 == 0:
                toc = time.time()
                duration = toc - tic
                speed = '{:.1f}KB/s'.format(20 * block_size * 1e-3 / duration)
                percentage = '{:.1%}'.format(count * block_size / total_size)
                tic = toc
                sys.stdout.write('\r>>> Downloading {} {}({:6})'.format(filename, percentage, speed))
                sys.stdout.flush()
        filepath, _ = urllib.request.urlretrieve(url, filepath, _progress)
        file_stat = os.stat(filepath)
        print('Successfully downloaded', filename, file_stat.st_size, 'bytes!!!')


def main():
    if FLAGS.url == 'all':
        for item in URLs:
            maybe_download_data(item)
    else:
        maybe_download_data(FLAGS.url)


if __name__ == '__main__':
    FLAGS = parser.parse_args()
    main()
