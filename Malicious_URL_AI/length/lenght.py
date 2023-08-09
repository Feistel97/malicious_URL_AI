import numpy as np
import pandas as pd
import urllib.parse
import urllib.request
import tldextract
import re
import enchant


data = pd.read_csv('malicious_phish.csv',encoding='latin1')
pd.set_option("display.max_rows", None)
d = enchant.Dict("en_US")

data['type'] = data['type'].replace(['benign','defacement','phishing','malware'],[0,1,1,1])

X_data = data['url']
y_data = data['type']

phishing_keywords = ['login', 'secure', 'banking', 'account', 'confirm', 'verify', 'update', 'paypal', 'amazon', 'ebay']
srv_clt_keywords = ['server','client']

def check_phishing_keywords(url, phishing_keywords):
    for keyword in phishing_keywords:
        if keyword in url:
            return keyword
    return None

def check_srv_clt(url, srv_clt_keywords):
    for keyword in srv_clt_keywords:
        if keyword in url:
            return keyword
    return None

url_info_list = []

count = 0

for url in X_data:
    parsed_url = urllib.parse.urlparse(url)
    extracted = tldextract.extract(url)
    url_type = y_data[count]
    count+=1
    subdomain = extracted.subdomain
    if subdomain == 'www':
        www = 1
    else:
        www = 0
    
    protocol = parsed_url.scheme
    if protocol == 'http':
        http = 1
    else:
        http = 0
    if protocol == 'https':
        https = 1
    else:
        https = 0
    path_length = len(parsed_url.path)
    query_length = len(parsed_url.query)
    netloc_length = len(parsed_url.netloc)
    url_length = len(url)
    fragment_length = len(parsed_url.fragment)
    if url_length > 70:
        url70 = 1
    else:
        url70 = 0
    tld_length = len(extracted.suffix)
    url_numbers_count = sum(len(re.findall(r'\d', url)) for url in [url])
    if url_numbers_count > 50:
        url_numbers_50 = 1
    else:
        url_numbers_50 = 0
    url_letter_count = len(re.findall(r'[a-zA-Z]', url))
    url_special_count = len(re.findall(r'[^\w\s]', url))
    at_count = url.count('@')
    and_count = url.count('&')
    sharp_count = url.count('#')
    percent_count = url.count('%')
    dot_count = url.count('.')
    equal_count = url.count('=')
    hyphen_count = url.count('-')
    underscore_count = url.count('_')
    tilde_count = url.count('~')
    semicolon_count = url.count(';')
    keyword = check_phishing_keywords(url, phishing_keywords)
    if keyword:
        phishing = 1
    else:
        phishing = 0
    keyword = check_srv_clt(url, phishing_keywords)
    if keyword:
        srv_clt = 1
    else:
        srv_clt = 0

    url_info = {
        'url_type' : url_type,
        'path_length': path_length, #path 길이
        'query_length': query_length, #quert 길이
        'netloc_length': netloc_length, #netloc 길이 
        'fragment_length': fragment_length,
        'url_length' : url_length, #url 길이
        'url70' : url70, #url의 길이가 70을 넘는지 확인요소
        'tld_length' : tld_length, #tld 길이
        'url_numbers_count' : url_numbers_count, #url의 존재하는 숫자 갯수
        'url_letter_count' : url_letter_count, #url의 존재하는 문자 갯수
        'url_numbers_50' : url_numbers_50, #url의 존재하는 숫자 갯수가 50을 넘는지
        'url_special_count' : url_special_count, #url의 특수문자 갯수
        'at_count' : at_count, #@
        'and_count' : and_count, #&
        'sharp_count' : sharp_count, ##
        'percent_count' : percent_count, #%
        'dot_count' : dot_count, #.
        'equal_count' : equal_count, #=
        'hyphen_count' : hyphen_count, #-
        'underscore_count' : underscore_count, #_
        'tilde_count' :tilde_count , #~
        'semicolon_count' :semicolon_count, #;
        'www' : www, #www
        'http' : http, #http
        'https' : https, #https
        'phishing': phishing, #피싱에 자주 사용되는 키워드 존재 유무
        'srv_clt' : srv_clt, #서버 또는 클라이언트의 단어가 존재하는지
    }
    
    url_info_list.append(url_info)

url_info_df = pd.DataFrame(url_info_list)

print(url_info_df.head())

url_info_df.to_csv('url_info.csv', index=False)