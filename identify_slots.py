"""
Text Clustering: Identify_Slots

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

This class constructor takes array of utterances and four integer parameter
which actually defines the mode of generating synonyms (auto_generate_synonym_modes - explained in index.py file).
> performs cleaning the utterances like given in the global variable ``steps``.
> identify synonyms and replace the words in the utterances by synonym name
> generates maximum number of clusters
and returns clustered utterances

``execute`` is the main method which initiates the execution
"""

class Identify_Slots:
    def __init__(self, sentences, strong_relation_distance, min_occurrences_of_neighbour_keys, min_occurrences_of_keyword, min_items_in_slot):
        self.sentences = sentences
        self.distance = strong_relation_distance
        self.min_occurrences_of_neighbour_keys = min_occurrences_of_neighbour_keys
        self.min_occurrences_of_keyword = min_occurrences_of_keyword
        self.min_items_in_slot = min_items_in_slot

    def get_lcr(self):
        lcr=[]
        for sentence in self.sentences:
            for i in range(self.distance, len(sentence)-self.distance):
                dis_arr = []
                for no in range(self.distance):
                    dis_arr.append(sentence[no])
                for no in range(i+1, i+self.distance+1):
                    dis_arr.append(sentence[no])
                lcr.append(["".join(dis_arr) + "c", sentence[i]])
        return self.get_likely_slots(lcr)

    def get_crr(self):
        crr=[]
        distn = self.distance + 1
        for sentence in self.sentences:
            for i in range(0, len(sentence)-distn):
                dis_arr = []
                for no in reversed(range(distn+i+1)):
                    if no == i:
                        # crr.append(["".join(dis_arr) + "r", sentence[no]])
                        crr.append(["".join(dis_arr) + "r", sentence[no]])
                    else:
                        dis_arr.append(sentence[no])

        return self.get_likely_slots(crr)

    def get_llc(self):
        llc=[]
        distn = self.distance + 1
        for sentence in self.sentences:
            for i in range(distn, len(sentence)):
                dis_arr = []
                for no in range(distn+1):
                    if no == distn:
                        llc.append(["".join(dis_arr) + "l", sentence[no]])
                    else:
                        dis_arr.append(sentence[no])
        return self.get_likely_slots(llc)

    def find_n_occurrences(self, key_value_array, n):
        key_value_stringified = []
        for ech in key_value_array:
            arrToStr = ' '.join(map(str, ech))
            key_value_stringified.append(arrToStr)

        n_occurs_of_key_value=[]
        key_value_stringified.sort()

        prev = -1
        count = 0
        flag = 0

        for item in key_value_stringified:
            if item == prev: count = count + 1
            else: count = 1
            prev = item

            if count == n:
                flag = 1
                n_occurs_of_key_value.append(item)

        # if flag == 0:
        #     print("No occurrences found")

        arr_n_occurs_of_key_value = []
        for occ in n_occurs_of_key_value:
            rssplt = occ.rsplit(' ', 1)
            arr_n_occurs_of_key_value.append(rssplt)
        return arr_n_occurs_of_key_value

    def get_likely_slots(self, arr):
        key_list = []
        for item in arr:
            key_list.append(item[0])
        dist_key_list = set(key_list)

        if self.min_occurrences_of_neighbour_keys >= 1:
            arr_n_occurs_of_key=[]
            for ech in dist_key_list:
                if key_list.count(ech) >= self.min_occurrences_of_neighbour_keys:
                    arr_n_occurs_of_key.append(ech)
            dist_key_list = arr_n_occurs_of_key

        arr_n_occurs_of_key_value = self.find_n_occurrences([kv for kv in arr if kv[0] in dist_key_list], self.min_occurrences_of_keyword) if self.min_occurrences_of_keyword >= 1 else arr

        likely_slots={}
        for key_item in dist_key_list:
            arr_res = [itm[1] for itm in arr_n_occurs_of_key_value if itm[0] == key_item]
            if len(arr_res) >= self.min_items_in_slot:
                if arr_res not in likely_slots.values():
                    # likely_slots[key_item] = arr_res
                    likely_slots[arr_res[0]] = arr_res

        return likely_slots

    def uniqueVals(self, data):
        duplicateValues = list()
        uniqueValues = list()
        for x in data.values():
            if x not in uniqueValues:
                uniqueValues.append(x)
                #     duplicateValues.append(x)
        return uniqueValues

    def possible_slots(self):
        lcr = self.get_lcr()
        crr = self.get_crr()
        llc = self.get_llc()
        identified_slots = {**lcr, **crr, **llc}
        return identified_slots

# remove the subsets and create dictionary
def remove_subsets(ips):
    for k, v in ips.items():
        for key, value in ips.items():
            if v != value:
                if set(v).issubset(set(value)):
                    del ips[k]
                    remove_subsets(ips)
    return ips

def identify_possible_slots(sentences, slots_config):
    split_sentences = []
    for sentence in sentences:
        split_sentences.append(sentence.split())

    if len(slots_config) == 1:
        idfy_slots = Identify_Slots(split_sentences, slots_config[0][0], slots_config[0][1], slots_config[0][2], slots_config[0][3])
        identify_possible_slots = idfy_slots.possible_slots()
        return remove_subsets(identify_possible_slots)
    else:
        idfy_slots=Identify_Slots(split_sentences, slots_config[0][0], slots_config[0][1], slots_config[0][2], slots_config[0][3])
        lcr=idfy_slots.get_lcr()
        print(idfy_slots.uniqueVals(lcr))

        idfy_slots=Identify_Slots(split_sentences, slots_config[1][0], slots_config[1][1], slots_config[1][2], slots_config[1][3])
        crr=idfy_slots.get_crr()
        print(idfy_slots.uniqueVals(crr))

        idfy_slots=Identify_Slots(split_sentences, slots_config[2][0], slots_config[2][1], slots_config[2][2], slots_config[2][3])
        llc=idfy_slots.get_llc()
        print(idfy_slots.uniqueVals(llc))

        identify_possible_slots = idfy_slots.uniqueVals(lcr) + idfy_slots.uniqueVals(crr) + idfy_slots.uniqueVals(llc)
        print("end2")
        return remove_subsets(identify_possible_slots)