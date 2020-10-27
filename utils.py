import json
import time
start = time.time()
from translate import Translator
import pyttsx3
# //3 days,7 days ..
array_time_repeat=['3','7','14','21','30']

def get_next_time_practice(current_nb_repeat):
    current_time_stamp=int(time.time()) #(s)
    
    if current_nb_repeat>len(array_time_repeat)-1:
        return current_time_stamp+int(array_time_repeat[-1])*24*3600
    else:
        return current_time_stamp+int(array_time_repeat[current_nb_repeat])*24*3600

def ham_write_json(dict_data,path_json_file):
    with open(path_json_file,'w') as json_file:
        json.dump(dict_data,json_file)

def ham_read_json(path_json_file):
    data=''
    with open(path_json_file) as json_file:
        data=json.load(json_file)
    return data    


def ham_on_bai(word):
    current_word=word['word']
    current_ipa=word['ipa']
    current_tran=word['tran']
    current_sentence=word['sentence']
    translator= Translator(to_lang="vi")
    translation = translator.translate(current_sentence)
    engine = pyttsx3.init()
    engine.say(current_sentence)
    print('------------New word----------')
    print(current_word)
    print(current_ipa)
    print(current_tran)
    print(current_sentence)
    print(translation)
    engine = pyttsx3.init()
    while True:
        #print('---type again---')
        engine.say(current_sentence)
        engine.runAndWait()
        current_sentence_user=input()
        if current_sentence_user.lower() == current_sentence.lower():
            break
        else:
            print('Repeat...')
    elapsed = (time.time() - start)/60
    a=round(elapsed, 2)
    print('Bạn đã học được Tiếng anh trong ',+ a, ' Phút')  
