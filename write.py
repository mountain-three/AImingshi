# author：shan   time：2021/12/7
# -*- coding: UTF-8 -*-
import whoosh.index as index
import pandas as pd
import math
indexname = {1:"married_cases",2:"family_fygx_cases",3:"family_fyjf_cases",4:"family_syjf_cases",
        5:"divorce_hycc_cases",6:"divorce_hhcc_cases",7:"divorce_hhzw_cases"}
write_file_index =1
df = pd.read_excel('婚姻家庭三分类-二级分类/婚姻关系x.xlsx',sheet_name = 1,usecols=[2,13,15],skiprows = [0,1]).dropna()#读取xlsx中第一个sheet
# 输入你要写入的文档【1234567分别对应模式里的1~7】
df.replace("/r")
ix = index.open_dir("indexdir", indexname=indexname[write_file_index])
writer = ix.writer()
for index in df.index:
    if  df.loc[index][1]!="裁判理由" :
        writer.add_document(title=df.loc[index][0],reason=df.loc[index][1],
                    laws=df.loc[index][2])
writer.commit()