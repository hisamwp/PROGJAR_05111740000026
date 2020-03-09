import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}")
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


link = ['https://2.bp.blogspot.com/--GbHE6JbJ-8/W-bBTajXkLI/AAAAAAAADuU/EPIjgib0G1QkMYRpW27JH-pOhKizi746QCLcBGAs/s1600/PicsArt_11-05-06.49.16.jpg',
        'https://i.kym-cdn.com/entries/icons/original/000/024/062/jerry.jpg']

for i in link:    
    thr = threading.Thread(target=download_gambar, args=(i,))
    thr.start()
    thr.join()