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
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"downloads/{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    links = [
        'https://www.lifewire.com/thmb/ZV_HiWqMpSfLPK1epKdKjrqjN1I=/1500x1000/filters:no_upscale():max_bytes(150000):strip_icc()/lans-wans-and-other-area-networks-817376-v6-5c38d8b6c9e77c0001fb419e-5d9191b94bbb454582be68067656df49.png',
        'https://i.pcmag.com/imagery/articles/04yzUkLxWI14FgY9D81y2XR-10.fit_scale.size_2698x1517.v1569490796.jpg',
        'https://images.idgesg.net/images/article/2019/02/5g_wireless_technology_network_connections_by_credit-vertigo3d_gettyimages-1043302218_3x2-100787550-large.jpg'
    ]

    threads = []
    for link in links:
        t = threading.Thread(target=download_gambar, args=(link,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print('Finish all download')
