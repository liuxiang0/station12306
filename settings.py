"""
爬虫参数设置
QQ list includes QQ number and password, must give at least 4 QQ,
we have to crawl 300 times, one QQ can only crawl 110 times.
"""

import time 

crawl_hour = int(time.strftime("%H"))  # get HOURS

# 爬取的间隔时间
sleeptime = 3600 # 单位是秒，7200秒即为2小时, 似乎没有用到？ TODO

# define running environment variables, windows os like the following
working_path = "D:\\working\\easygo"
wgs84_file = "D:\\working\\easygo\\stations_wgs.csv"

# 分时段取不同的QQ List，防止一个号爬取到上限。
if crawl_hour < 12:
    qq_list = [["2371683532", "wode123456"], ["2374217858", "wode123456"],
               ["2374836182", "wode123456"], ["2375807532", "wode123456"]]
elif crawl_hour < 20:
    qq_list = [["2148896758", "wode111222"], ["2152673378", "wode111222"],
               ["2145578602", "wode111222"], ["2153302460", "wode111222"]]
else:
    qq_list = [["2145568632", "wode111222"], ["2148367549", "wode111222"],
               ["2145276228", "wode111222"], ["2145176170", "wode111222"]]
"""
qq_list = [["2402255768","wode123456"],["2385456274","wode123456"],
           ["2401036818","wode123456"],["2401359770","wode123456"]]
"""

# 下面这个表单是用来获取cookie的列表，最好多放一些QQ号
# ["1276881424", "huanyin2018"]]
# ["3133794419", "huanyin2018"], ["2152284058", "huanyin2018"]
fre = 126

if __name__ == "__main__":
    print("Hour=%d, QQ List= %s " % (crawl_hour, qq_list))
    for i in range(4):
        print("QQ[%d] = %s " % (i, qq_list[i][0]))