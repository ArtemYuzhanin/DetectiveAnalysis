from pymystem3 import Mystem
import re
import subprocess


def Processor(inputfile):
    cmd = "C:/Users/dogme/PycharmProjects/Lingva/mystem.exe -gnidl " + inputfile
    output = subprocess.check_output(cmd).decode("utf-8")
    name = 1
    results = []
    words_count = 0
    verb_count = 0
    adverb_count = 0
    subject_count = 0
    adjective_count = 0
    mestoim_count = 0
    topstoslovar = {}
    allres = []
    elite = set()
    for line in output.split("\n"):
        if not (re.match("bruhus", line)):
            if (name == 1 and re.match("name[а-яА-Я]+",line)):
                results.append(re.search("[а-яА-Я]+",line).group(0))
                name = 0
            else:
                example = re.search("[а-яА-Я]+-*[а-яА-Я]*=[A-Z]+", line)
                if example:
                    words_count += 1
                    word = example[0].replace(",", "").split("=")
                    if (word[1] == 'V'):
                        verb_count += 1
                    elif (word[1] == 'S'):
                        subject_count += 1
                    elif (word[1] == 'A'):
                        adjective_count += 1
                    elif (word[1] == 'ADV'):
                        adverb_count += 1
                    elif (word[1] == 'SPRO'):
                        mestoim_count += 1

                    if (word[1] in ['V', 'S', 'A', 'ADV', 'SPRO']):
                        if (word[0] in topstoslovar):
                            topstoslovar[word[0]] += 1
                        else:
                            topstoslovar.update({word[0]: 1})
        else:
            name = 1
            topdic = list(topstoslovar.items())
            topdic.sort(key=lambda i: i[1])
            topdic.reverse()
            del topdic[100:]
            topset = {i[0] for i in topdic}
            results.append(words_count)
            results.append(f"{subject_count / words_count:.2f}")
            results.append(f"{verb_count / words_count:.2f}")
            results.append(f"{adjective_count / words_count:.2f}", )
            results.append(f"{adverb_count / words_count:.2f}", )
            results.append(f"{mestoim_count / words_count:.2f}")
            results.append(dict(topdic))
            results.append(set(topset))
            allres.append(list(results))
            topdic.clear()
            topset.clear()
            topstoslovar.clear()
            results.clear()
            words_count = 0
            verb_count = 0
            adverb_count = 0
            subject_count = 0
            adjective_count = 0
            mestoim_count = 0
    kol = len(allres)
    for x in range(kol):
        etalon1 = set(allres[x][-1])
        for toppat in etalon1:
            kol_word = 0
            for y in range(kol):
                if toppat in allres[y][-1]:
                    allres[y][-1].remove(toppat)
                    kol_word += 1
            if kol_word >= int(kol*0.6):
                elite.add(toppat)

    allres.append(elite)
    return allres


resuletto = Processor('C:/Users/dogme/PycharmProjects/Lingva/Easy.txt')
with open("outputEasy.txt", mode='w', encoding="utf8") as f:
    for proizv in resuletto:
        if type(proizv) is list:
            for charac in proizv:
                f.write(str(charac))
                f.write('\n')
        else:
            f.write(str(proizv))
