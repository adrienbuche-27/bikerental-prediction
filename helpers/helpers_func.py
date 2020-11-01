import pickle

def save_pickle(filename, arg):
    pickle_out = open(filename,"wb")
    pickle.dump(arg, pickle_out)
    pickle_out.close()
    print('Variable saved at:' + filename)
    

def open_pickle(filename):
    infile = open(filename,'rb')
    new_dict = pickle.load(infile)
    infile.close()
    return new_dict