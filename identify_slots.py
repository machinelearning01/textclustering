from operator import itemgetter

class Identify_Slots:
    def __init__(self, sentences, strong_relation_distance, min_occurrences_of_keyword, min_items_in_slot):
        self.sentences = sentences
        self.distance = strong_relation_distance
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
                lcr.append([", ".join(dis_arr) + " (C)", sentence[i]])
        return self.get_likely_slots(lcr)

    def get_crr(self):
        crr=[]
        distn = self.distance + 1
        for sentence in self.sentences:
            for i in range(0, len(sentence)-distn):
                dis_arr = []
                for no in reversed(range(distn+i+1)):
                    if no == i:
                        crr.append([", ".join(dis_arr) + " (R)", sentence[no]])
                    else:
                        dis_arr.append(sentence[no])
        return self.get_likely_slots(crr)

    def get_llc(self):
        llc=[]
        distn = self.distance + 1
        for sentence in self.sentences:
            for i in range(distn, len(sentence)):
                dis_arr = []
                for no in reversed(range(distn+1)):
                    if no == distn:
                        llc.append([", ".join(dis_arr) + " (L)", sentence[no]])
                    else:
                        dis_arr.append(sentence[no])
        return self.get_likely_slots(llc)

    def find_n_occurrences(self, key_value_array, n):
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

    def get_likely_slots(self, arr):
        sorted_arr = arr  #sorted(arr, key=itemgetter(0))

        key_list=[]
        for item in sorted_arr:
            key_list.append(item[0])
        dist_key_list = set(key_list)
        # print(dist_key_list)

        n_occurs_arr = self.find_n_occurrences(sorted_arr, self.min_occurrences_of_keyword)

        likely_slots={}
        for key_item in dist_key_list:
            arr_res = [itm[1] for itm in n_occurs_arr if itm[0] == key_item]
            if len(arr_res) >= self.min_items_in_slot:
                likely_slots[key_item] = arr_res

        return likely_slots

    def possible_slots(self):
        lcr = self.get_lcr()
        crr = self.get_crr()
        llc = self.get_llc()
        lcr.extend(crr)
        lcr.extend(llc)
        return self.get_likely_slots(lcr)
