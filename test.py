import re
import subprocess

def mystem(text_f, res_f):
    cmd = "C:/Users/dogme/PycharmProjects/Lingva/mystem.exe -gnidl " + text_f
    output = subprocess.check_output(cmd).decode("utf-8")
    with open(res_f, 'w', encoding='utf-8') as res:
        for line in output.split("\n"):
            if not (re.match("bruhus", line)):
                if (name == 1 and re.match("name[а-яА-Я]+", line)):
                    res.write(re.match("\name[а-яА-Я]+", line).group(0))
                    name = 0
                else:
                    word_match = re.search("[а-яА-Яa-zA-Z]+-*[а-яА-Я]*=[A-Z]*", line)

                    if word_match:
                        # if word_match and "PR" not in word_match[0]:
                        word = word_match[0].replace(",", "").split("=")
                        res.write(word[1] + '_' + word[0])
                res.write("\n")
            else:
                res.write("\nSTOPOCHKA\n\n")

mystem('C:/Users/dogme/PycharmProjects/Lingva/input1.txt','C:/Users/dogme/PycharmProjects/Lingva/output1.txt')


