import datetime
def get_nowdate():
    now_time = (datetime.datetime.now()).strftime("%Y%m%d%H%M")
    # print(now_time)
    # print(type(now_time))
    return now_time
get_nowdate()
