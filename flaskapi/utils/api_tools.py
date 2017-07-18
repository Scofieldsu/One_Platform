# encoding: utf-8

PARAMS_TYPE = ['dict','int','str','float','list','datetime']

fgs = [
    "name",                # flags[0]
    "param_explain",       #    1
    "description",         #    2
    ":description",        #    3
    "params",              #    4
    ":param",              #    5
    "return",              #    6
    ":return:",            #    7
    "\n"
]


# 把function的__doc__字符串转换为字典
def trans_str_to_dict(do_str):
    result = {fgs[1]: dict()}
    if not do_str:
        return result
    tem_list = do_str.split(fgs[8])
    for x in tem_list:
        if fgs[3] in x:
            result[fgs[2]] = x.split(fgs[3])[1].strip()
        elif fgs[5] in x:
            params = x.split(fgs[5])[1]
            if params.strip():
                tem = params.split(':')
                if len(tem) >= 2 and tem[1].strip().lower() in PARAMS_TYPE:
                    result[tem[0].strip()] = tem[1].strip()
                if len(tem) >= 3 :
                    result[fgs[1]][tem[0].strip()] = tem[2].strip()
        elif fgs[7] in x:
            result[fgs[6]] = x.split(fgs[7])[1].strip()
    return result


# 字典b是字典a中的一个value，把字典b中的一个键值对移动到字典a
def dict_move_key(dict_a, dict_b, key):
    if key in dict_b:
        dict_a[key] = dict_b[key]
        dict_b.pop(key)
    return dict_a


# 重组接口信息为get_all_api_tem中的数据格式
def compose_api_info(key, api_dict):
    tem_res = dict()
    tem_res[fgs[0]] = key
    doc_dict = trans_str_to_dict(api_dict[key].__doc__)
    move_key = [
        "description",
        "return",
        "param_explain"
    ]
    for x in move_key:
        tem_res = dict_move_key(tem_res,doc_dict, x)
    tem_res[fgs[4]] = doc_dict
    return tem_res