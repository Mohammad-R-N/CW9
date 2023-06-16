from dataclasses import dataclass
import pickle
import pathlib


@dataclass
class Pesron:
    name:str
    age:int
    address:str

def read_obj():
    with open('objs.pickle', 'rb') as file:
        return pickle.load(file)

def write_obj(obj):
    with open('objs.pickle', 'wb') as file:
        pickle.dump(obj,file)

def save_obj(obj):
    info_file=pathlib.Path("objs.pickle")
    if info_file.exists():
        info=read_obj()
        info.append(obj)
        write_obj(info)
    else:
        with open('objs.pickle', 'wb') as file:
            pickle.dump([obj],file)

if __name__=="__main__":

    farzam= Pesron("farzam",31,"tehran")
    hosein= Pesron("hosein",21,"tehran")
    mahdi= Pesron("mahdi",25,"tehran")

    save_obj(farzam)
    save_obj(mahdi)
    x=read_obj()
    for i in x:
        print(i)