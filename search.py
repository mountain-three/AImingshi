# author：shan   time：2021/12/7
# -*- coding: UTF-8 -*-
import whoosh.index as index
import jieba
from whoosh.qparser import QueryParser
import re
# input为要查询的内容，file_index指明要在哪里查询
input = "夫妻之间应以宽容的心善待对方"
file_index =1
# f = re.findall('《(.*?)》',str)
indexname = {1:"married_cases",2:"family_fygx_cases",3:"family_fyjf_cases",4:"family_syjf_cases",
        5:"divorce_hycc_cases",6:"divorce_hhcc_cases",7:"divorce_hhzw_cases"}
ix = index.open_dir("indexdir", indexname=indexname[file_index])
with ix.searcher() as searcher:
    # a集合里放找出的结果，里面是result_case这个类
   a = set()
   jinput = jieba.tokenize(input)
   for tk in jinput:
    query = QueryParser("laws", ix.schema).parse(tk[0])
    results = searcher.search(query)
    for result in results:
        if result["title"] not in a:
            print(result)
            a.add(result["title"])


