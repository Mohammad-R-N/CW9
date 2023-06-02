def dict_index_eq_value(*args):
    new_dict={}
    for key,value in enumerate(args):
        new_dict[key+1]=value
    return new_dict

if __name__=="__main__":
    print(dict_index_eq_value(1,2,3,4,"hi","bye"))