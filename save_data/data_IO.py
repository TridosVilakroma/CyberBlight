import pickle
from os import path,listdir
from os.path import isfile, join

def save(data,slot):
    pickle_out = open(rf'save_data\saves\{slot}', 'wb')
    pickle.dump(data, pickle_out)
    pickle_out.close()

def load(slot):
    if path.exists(rf'save_data\saves\{slot}'):
        pickle_in = open(rf'save_data\saves\{slot}', 'rb')
        data = pickle.load(pickle_in)
        pickle_in.close()
        return data

def existing_files(folder):
    saves_dict={i: i for i in listdir(folder)}
    saves_dict['New Game']= len(saves_dict)+1
    return saves_dict


