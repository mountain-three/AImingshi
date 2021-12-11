from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer
import os, os.path

analyzer = ChineseAnalyzer()
# 模式里是title是案件名称，reason裁判里有，laws是法律条款
schema = Schema(title=TEXT(stored=True,analyzer=analyzer), reason=TEXT(stored=True,analyzer=analyzer),
                laws=TEXT(stored=True,analyzer=analyzer))
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
# 创建模式,married:婚姻关系，family_XXXX_cases：家庭关系里那三个表格，divorce_xxxx_cases:离婚后财产纠纷里那三个表格
create_in("indexdir", schema,indexname = "married_cases")
create_in("indexdir", schema,indexname = "family_fygx_cases")
create_in("indexdir", schema,indexname = "family_fyjf_cases")
create_in("indexdir", schema,indexname = "family_syjf_cases")
create_in("indexdir", schema,indexname = "divorce_hycc_cases")
create_in("indexdir", schema,indexname = "divorce_hhcc_cases")
create_in("indexdir", schema,indexname = "divorce_hhzw_cases")
# 写入文件


