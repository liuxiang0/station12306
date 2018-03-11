# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:21:10 2018

@author: xydroot

crawl all station list from 12306.cn

"""

#下载所有的车次数据  保存为 train_list.txt文件  
def getTrain_list():  
    requests.adapters.DEFAULT_RETRIES = 5  
    response = requests.get(train_list_url, stream=True,verify=False)  
    status = response.status_code  
    if status == 200:  
        with open('train_list.txt', 'wb') as of:  
            for chunk in response.iter_content(chunk_size=102400):  
                if chunk:  
                    of.write(chunk)  
  
  
#分析train_list.txt文件 得出火车 出发站到终点站的数据  
def trainListStartToEnd():  
    global station_start_end_set  
    with open('train_list.txt','rb') as of:  
        text=of.readline()  
        tt=text.decode("utf-8")  
        ss=tt.replace("},{","}\n{").replace("2017-","\n").replace("[","\n").split("\n")  
        m_list=list()  
        for s in ss:  
            pattern = re.compile(r'\((\w+-\w+)\)')  
            match = pattern.search(s)  
            if match:  
                m_list.append(match.group(1))  
        station_start_end_set=set(m_list)  
            
#利用出发站到终点站 爬取期间的列车数据  
def getTrainNoList(back_date,train_date,from_station,from_station_name,to_station,to_station_name):  
    post_data= {'back_train_date':back_date,  
                '_json_att':"",'flag':'dc',  
                'leftTicketDTO.from_station':from_station,  
                'leftTicketDTO.to_station':to_station,  
                'leftTicketDTO.from_station_name':from_station_name,  
                'leftTicketDTO.to_station_name':to_station_name,  
                'leftTicketDTO.train_date':train_date,  
                'pre_step_flag':'index',  
                'purpose_code':'ADULT'}  
  
    init_resp=requests.post(init_url,data=post_data,headers=HEADERS,allow_redirects=True,verify=False)  
    cookies=init_resp.cookies  
    cookies.set('_jc_save_fromStation', from_station_name+','+from_station, domain='kyfw.12306.cn', path='/')  
    cookies.set('_jc_save_toStation', to_station_name+','+to_station, domain='kyfw.12306.cn', path='/')  
    cookies.set('_jc_save_fromDate', train_date, domain='kyfw.12306.cn', path='/')  
    cookies.set('_jc_save_toDate', back_date, domain='kyfw.12306.cn', path='/')  
    cookies.set('_jc_save_wfdc_flag', 'dc', domain='kyfw.12306.cn', path='/')  
    url=query_url+"leftTicketDTO.train_date="+train_date+"&leftTicketDTO.from_station="+from_station+"&leftTicketDTO.to_station="+to_station+"&purpose_codes=ADULT"  
    try:  
        response = requests.get(url, headers=HEADERS, allow_redirects=True,cookies=cookies,verify=False,timeout=10)  
        data=""  
        if response.status_code==200:  
            data=response.content  
        data=data.decode("UTF-8")  
        return data,cookies  
    except  Exception as err:  
        logger.exception('getTrainNoList error 获取车次列表错误 日期'+train_date+'从'+from_station_name+'到'+to_station_name+' :%s',err)  
        return None,None  