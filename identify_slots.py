
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
            lcr.append([", ".join(dis_arr) + " (C)", sentence[i]])
    return lcr

def get_crr(sentences, distance):
    crr=[]
    for sentence in sentences:
        for i in range(0, len(sentence)-distance):
            dis_arr = []
            for no in range(distance+1):
                if no == distance:
                    crr.append([", ".join(dis_arr) + " (R)", sentence[i+no]])
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
                    llc.append([", ".join(dis_arr) + " (L)", sentence[i-no]])
                else:
                    dis_arr.append(sentence[i-no])
    return llc

def find_n_occurences(key_value_array, n):
    found_duplicates = []
    for ech in key_value_array:
        arrToStr = ' '.join(map(str, ech))
        found_duplicates.append(arrToStr)

    n_occurs=[]
    found_duplicates.sort()

    # Constants Declaration
    prev = -1
    count = 0
    flag = 0

    # Iterating
    for item in found_duplicates:
        if item == prev:
            count = count + 1
        else:
            count = 1
        prev = item

        if count == n:
            flag = 1
            n_occurs.append(item)

    # If no element is not found.
    if flag == 0:
        print("No occurrences found")

    n_occurs_arr = []
    for occ in n_occurs:
        rssplt = occ.rsplit(' ', 1)
        n_occurs_arr.append(rssplt)
    return n_occurs_arr

def get_likely_slots(arr):
    sorted_arr = sorted(arr, key=itemgetter(0))

    key_list=[]
    for item in sorted_arr:
        key_list.append(item[0])
    dist_key_list = set(key_list)
    # print(dist_key_list)

    n_occurs_arr = find_n_occurences(sorted_arr, consider_min_occurences_of_keyword)

    likely_slots={}
    for key_item in dist_key_list:
        arr_res = [itm[1] for itm in n_occurs_arr if itm[0] == key_item]
        if len(arr_res) >= min_items_in_slot:
            likely_slots[key_item] = arr_res

    return likely_slots


strong_relation_distance = 1
consider_min_occurences_of_keyword = 3
min_items_in_slot = 3


def possible_slots(sentences):
    lcr = get_lcr(sentences, strong_relation_distance)
    crr = get_crr(sentences, strong_relation_distance+1)
    llc = get_llc(sentences, strong_relation_distance+1)
    lcr.extend(crr)
    lcr.extend(llc)
    return get_likely_slots(lcr)
