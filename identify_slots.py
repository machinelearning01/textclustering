
from operator import itemgetter

def get_lcr(sentences, distance):
    lcr=[]
    for sentence in sentences:
        for i in range(distance, len(sentence)-distance):
            dis_arr = []
            for no in range(distance):
                dis_arr.append(sentence[i - no])
            for no in reversed(range(distance)):
                dis_arr.append(sentence[i + no])
            lcr.append(", ".join(dis_arr) + " (C)", sentence[i])
    return lcr

def get_crr(sentences, distance):
    crr=[]
    for sentence in sentences:
        for i in range(0, len(sentence)-distance):
            dis_arr = []
            for no in range(distance+1):
                if no == distance:
                    crr.append(", ".join(dis_arr) + " (R)", sentence[i+no])
                else:
                    dis_arr.append(sentence[i+no])
    return crr

def get_llc(sentences, distance):
    llc=[]
    for sentence in sentences:
        for i in range(distance, len(sentence)):
            dis_arr = []
            for no in reversed(range(distance+1)):
                if no == i:
                    llc.append(", ".join(dis_arr) + " (L)", sentence[i-no])
                else:
                    dis_arr.append(sentence[i-no])
    return llc


def get_likely_slots(arr):
    res = sorted(arr, key=itemgetter(0))

    dist_list = set(map(tuple, res))
    key_list=[]
    for item in dist_list:
        key_list.append(item[0])

    dist_key_list = set(key_list)
    # print(dist_key_list)

    likely_slots={}
    for key_item in dist_key_list:
        arr_res = [itm[1] for itm in dist_list if itm[0] == key_item]
        if len(arr_res) >= min_items_in_slot:
            likely_slots[key_item] = arr_res

    return likely_slots


strong_relation_distance = 1
min_items_in_slot = 3

def possible_slots(sentences):
    lcr = get_lcr(sentences, strong_relation_distance)
    crr = get_crr(sentences, strong_relation_distance+1)
    llc = get_llc(sentences, strong_relation_distance+1)
    lcr.extend(crr)
    lcr.extend(llc)
    return get_likely_slots(lcr)
