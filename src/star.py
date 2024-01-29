import requests
import os
from astrometry_net_client import Session
from astrometry_net_client import FileUpload

# hello
# url_image = 'https://c2cpicdw.qpic.cn/offpic_new/2016741487//2016741487-3567923580-B88EFE28A92703A92CD1B21181ADCA5C/0?term=2&amp;is_origin=0'

def star(url_image: str):
    # 初始化 Session
    s = Session(api_key='kjelalvdcvfvseuu')

    # 下载图像并保存为本地文件
    local_filename = './tmp/local_image.jpg'
    response = requests.get(url_image)
    with open(local_filename, 'wb') as f:
        f.write(response.content)

    # 初始化 FileUpload
    upl = FileUpload(local_filename, session=s)

    # 提交文件并等待处理完成
    submission = upl.submit()
    submission.until_done()

    # 获取第一个 job
    job = submission.jobs[0]

    jobid = str(job.id)
    addr = "http://nova.astrometry.net/annotated_display/" + jobid

    # 等待 job 完成
    job.until_done()

    # 删除本地文件
    os.remove(local_filename)
    return addr