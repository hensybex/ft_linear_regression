from matplotlib import pyplot as plt

from collections import Counter

import csv

import datetime

import numpy as np


B_Days = []
Cities = []
Genders = []
Heards = []
Statuses = []
Levels = []
contracts = []
Nicknames = []
WaveIds = []

B_Days

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        B_Days.append(line["Birth date"])
        Cities.append(line["Native city"])
        Genders.append(line["Gender"])
        Heards.append(line["Heard about school from"])
        Statuses.append(line["Life status"])
        Levels.append(line["Level"])
        contracts.append(line["contracts"])
        Nicknames.append(line["Nickname"])
        WaveIds.append(line["Wave id"])

if __name__ == "__main__":
    with open("data/clean_wave1_data.csv") as f_obj:
        csv_dict_reader(f_obj)

# ----------------- Overall Info ---------------

OverallInfo = np.zeros((3), dtype=np.integer)
    # 0 - Students summary;
    # 1 - Active summary
    # 2 - Terminated summary

for i, status in enumerate(contracts):
    if contracts[i] == '1':
        OverallInfo[1] += 1
    else:
        OverallInfo[2] += 1
    OverallInfo[0] += 1


def printSummary(name, overall, active, terminated):
    print(name)
    print("Summary:     ---" + str(overall) + "---", "")
    print("Active:      ---" + str(active) + "---", "")
    print("Terminated:  ---" + str(terminated) + "---", "(Termination probability: ", str(terminated / overall * 100) + "%)", "\n")

print("\nOverall Info.")
printSummary("Overall", OverallInfo[0], OverallInfo[1], OverallInfo[2])

# ----------------- Cities Info ---------------

CitiesInfo = np.zeros((6), dtype=np.integer)
    # 0 - Moscow students summary;
    # 1 - Moscow active
    # 2 - Moscow terminated
    # 3 - Outskirts students summary
    # 4 - Outskirts active
    # 5 - Outskirts terminated

for i, city in enumerate(Cities):
    if city == "Москва" or city == "Москве" or city == "МОСКВА" or city == "Москва " or city == "Moscow" or city == "Mosocow" or city == " Москва" or city == "г. Москва" or city == "гор. Москва" or city == "г. Москва," or city == "город Москва" or city == "москва":
        if contracts[i] == '1':
            CitiesInfo[1] += 1
        else:
            CitiesInfo[2] += 1
        CitiesInfo[0] += 1
    else:
        if contracts[i] == '1':
            CitiesInfo[4] += 1
        else:
            CitiesInfo[5] += 1
        CitiesInfo[3] +=1

print("\nCities Info.")
printSummary("Moscow", CitiesInfo[0], CitiesInfo[1], CitiesInfo[2])
printSummary("Outskirts", CitiesInfo[3], CitiesInfo[4], CitiesInfo[5])

# ----------------- Gender info ---------------

GenderInfo = np.zeros((6), dtype=np.integer)
    # 0 - Male students summary;
    # 1 - Male active
    # 2 - Male terminated
    # 3 - Female students summary
    # 4 - Female active
    # 5 - Female terminated

for i, gender in enumerate(Genders):
    if gender == "male":
        GenderInfo[0] += 1
        if contracts[i] == '1':
            GenderInfo[1] += 1
        else:
            GenderInfo[2] += 1
    else:
        GenderInfo[3] +=1
        if contracts[i] == '1':
            GenderInfo[4] += 1
        else:
            GenderInfo[5] += 1

print("\nPrinting Gender Info.")
printSummary("Male", GenderInfo[0], GenderInfo[1], GenderInfo[2])
printSummary("Female", GenderInfo[3], GenderInfo[4], GenderInfo[5])




# ----------------- Heard from info ---------------
HeardFromInfo = np.zeros((27), dtype = np.integer)
    # 0 - Fb/inst summary
    # 1 - Fb/inst active
    # 2 - Fb/inst terminated
    # 3 - From 21 students summary
    # 4 - From 21 students active
    # 5 - From 21 students terminated
    # 6 - From friends summary
    # 7 - From friends active
    # 8 - From friends terminated
    # 9 - From parents summary
    # 10 - From parents active
    # 11 - From parents terminated
    # 12 - From teachers summary
    # 13 - From teachers active
    # 14 - From teachers terminated
    # 15 - Google/yandex summary
    # 16 - Google/yandex active
    # 17 - Google/yandex terminated
    # 18 - Other summary
    # 19 - Other active
    # 20 - Other terminated
    # 21 - Vk ads summary
    # 22 - Vk ads active
    # 23 - Vk ads terminated
    # 24 - Empty summary
    # 25 - Empty active
    # 26 - Empty terminated
    
for i, heardfrom in enumerate(Heards):
    if heardfrom == "fb_inst":
        HeardFromInfo[0] += 1
        if contracts[i] == '1':
            HeardFromInfo[1] += 1
        else:
            HeardFromInfo[2] += 1
    if heardfrom == "from_21_student":
        HeardFromInfo[3] += 1
        if contracts[i] == '1':
            HeardFromInfo[4] += 1
        else:
            HeardFromInfo[5] += 1
    if heardfrom == "from_friends":
        HeardFromInfo[6] += 1
        if contracts[i] == '1':
            HeardFromInfo[7] += 1
        else:
            HeardFromInfo[8] += 1
    if heardfrom == "from_parents":
        HeardFromInfo[9] += 1
        if contracts[i] == '1':
            HeardFromInfo[10] += 1
        else:
            HeardFromInfo[11] += 1
    if heardfrom == "from_teachers":
        HeardFromInfo[12] += 1
        if contracts[i] == '1':
            HeardFromInfo[13] += 1
        else:
            HeardFromInfo[14] += 1
    if heardfrom == "google_yandex":
        HeardFromInfo[15] += 1
        if contracts[i] == '1':
            HeardFromInfo[16] += 1
        else:
            HeardFromInfo[17] += 1
    if heardfrom == "other":
        HeardFromInfo[18] += 1
        if contracts[i] == '1':
            HeardFromInfo[19] += 1
        else:
            HeardFromInfo[20] += 1
    if heardfrom == "vk_ads":
        HeardFromInfo[21] += 1
        if contracts[i] == '1':
            HeardFromInfo[22] += 1
        else:
            HeardFromInfo[23] += 1
    if heardfrom == "":
        HeardFromInfo[24] += 1
        if contracts[i] == '1':
            HeardFromInfo[25] += 1
        else:
            HeardFromInfo[26] += 1

print("\nPrinting Heard From Info.")
printSummary("Heard from Fb/inst", HeardFromInfo[0], HeardFromInfo[1], HeardFromInfo[2])
printSummary("Heard from 21 students", HeardFromInfo[3], HeardFromInfo[4], HeardFromInfo[5])
printSummary("Heard from friends", HeardFromInfo[6], HeardFromInfo[7], HeardFromInfo[8])
printSummary("Heard from parents", HeardFromInfo[9], HeardFromInfo[10], HeardFromInfo[11])
printSummary("Heard from teachers", HeardFromInfo[12], HeardFromInfo[13], HeardFromInfo[14])
printSummary("Heard from google/yandex", HeardFromInfo[15], HeardFromInfo[16], HeardFromInfo[17])
printSummary("Heard from other", HeardFromInfo[18], HeardFromInfo[19], HeardFromInfo[20])
printSummary("Heard from vk ads", HeardFromInfo[21], HeardFromInfo[22], HeardFromInfo[23])
printSummary("Heard from is empty", HeardFromInfo[24], HeardFromInfo[25], HeardFromInfo[26])


# Age Info

Age0_19Info = np.zeros((3), dtype = np.integer)
Age20_23Info = np.zeros((3), dtype = np.integer)
Age24_27Info = np.zeros((3), dtype = np.integer)
Age28_31Info = np.zeros((3), dtype = np.integer)
Age32_35Info = np.zeros((3), dtype = np.integer)
Age36_39Info = np.zeros((3), dtype = np.integer)
Age40_60Info = np.zeros((3), dtype = np.integer)

wave1Start = datetime.datetime(2018, 11, 19)
wave2Start = datetime.datetime(2019, 4, 1)
wave3Start = datetime.datetime(2019, 9, 2)

for i in enumerate(B_Days):
    B_Days[i[0]] = datetime.strptime(i[1], '%Y-%m-%d')

for i, date in enumerate(B_Days):
    if date > 2000:
        Age0_19Info[0] += 1
        if contracts[i] == '1':
            Age0_19Info[1] += 1
        else:
            Age0_19Info[2] += 1

    elif yearN.year > 1996:
        Age20_23Info[0] += 1
        if contracts[i] == '1':
            Age20_23Info[1] += 1
        else:
            Age20_23Info[2] += 1

    elif yearN.year > 1992:
        Age24_27Info[0] += 1
        if contracts[i] == '1':
            Age24_27Info[1] += 1
        else:
            Age24_27Info[2] += 1

    elif yearN.year > 1988:
        Age28_31Info[0] += 1
        if contracts[i] == '1':
            Age28_31Info[1] += 1
        else:
            Age28_31Info[2] += 1

    elif yearN.year > 1984:
        Age32_35Info[0] += 1
        if contracts[i] == '1':
            Age32_35Info[1] += 1
        else:
            Age32_35Info[2] += 1

    elif yearN.year > 1980:
        Age36_39Info[0] += 1
        if contracts[i] == '1':
            Age36_39Info[1] += 1
        else:
            Age36_39Info[2] += 1

    else:
        Age40_60Info[0] += 1
        if contracts[i] == '1':
            Age40_60Info[1] += 1
        else:
            Age40_60Info[2] += 1


print("\nPrinting Age Info.")
printSummary("0-19", Age0_19Info[0], Age0_19Info[1], Age0_19Info[2])
printSummary("20-23", Age20_23Info[0], Age20_23Info[1], Age20_23Info[2])
printSummary("24-27", Age24_27Info[0], Age24_27Info[1], Age24_27Info[2])
printSummary("28-31", Age28_31Info[0], Age28_31Info[1], Age28_31Info[2])
printSummary("32-35", Age32_35Info[0], Age32_35Info[1], Age32_35Info[2])
printSummary("36-39", Age36_39Info[0], Age36_39Info[1], Age36_39Info[2])
printSummary("40+", Age40_60Info[0], Age40_60Info[1], Age40_60Info[2])

print("Youngest student BD:", str(max(B_Days).year) + "." + str(max(B_Days).month) + "." + str(max(B_Days).day))
print("Oldest student BD:", str(min(B_Days).year) + "." + str(min(B_Days).month) + "." + str(min(B_Days).day))

