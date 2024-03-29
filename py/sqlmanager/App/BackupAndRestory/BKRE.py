from concurrent.futures import ThreadPoolExecutor
import os
import time


def task(n):
    print('%s is running' % os.getpid())
    time.sleep(2)
    return n ** 2


def solute(res):
    print('solute', res.result())


if __name__ == '__main__':
    p = ThreadPoolExecutor(max_workers=4)  # 进程池
    for i in range(10):
        p.submit(task, i).add_done_callback(solute)  # 按位置传参
    print('主程序')

