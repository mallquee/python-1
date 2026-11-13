# LIST 
# menggunakan kurung siku 
data_list = [10,2,4,3,2] 
print(data_list)  

# tuples 
data_tuples = (7,8,10,11) 
print(data_tuples) 
print(data_tuples[1])  

# tidak bisa dilakukan 
# data_tuples[1] = “ucup” 
# data_tuples.append(1)  

# sets (himpunan) 
data_sets = [10,4,3,2,7,6,5] 
print(data_sets)  

print(data_sets[0]) 


## Disctionary

# list -> array, mengakses dengan menggunakan index

data_list = ['ucup', 'rensi', 'salsa']
print (data_list[0])

#  dictionary (dict) -> associative array
# identifier -> key

data_dict = { 
    'key':'value', 
    'cp': 'ucup', 
    'rd': 'rendi', 
    'sl': 'salsa', 
    'nmbr': 100, 
    'list': data_list 
}  
print(data_dict['cp']) 
print(data_dict['nmbr']) 
print(data_dict['list']) 


## --- Operasi Dictionary ---

data_dict = {
    "cup":"ucup surucup",
    "pet":"opet saripet",
    "ndo":"nando surundo"
}

# panjang dictionary
LENDICT = len(data_dict)
print (f"panjang dictionary: (LENDICT)")

# mengecek key exist atau tidak 
KEY = "cup" 
CHECKKEY = KEY in data_dict 
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")  

# mengakses value (read) dengan get 
print(data_dict["cup"]) 
print(data_dict.get("cup")) 
print(data_dict.get("kis","key tidak ditemukan")) # check key dengan message  

# mengupdate data 
data_dict["cup"] = "ucup si ganteng" 
print(data_dict) 
data_dict["de"] = "ade si adek" 
print(data_dict) 

data_dict.update({"cup":"ucup surucup"}) 
print(data_dict) 
data_dict.update({"iwn":"iwan mang keren"}) # akan di tambah jika tidak ada 
print(data_dict)  

# menghapus data 
del data_dict["iwn"] 
print(data_dict) 


## --- Looping Dictionary ---  
teman_teman = {  
    "cup":"ucup surucup",  
    "tong":"sotong surotong",  
    "lur":"lur sedulur",  
    "wel":"bung towel"  
}  
# looping first try (yang keluar hanya key) 
for teman in teman_teman: 
    print(teman) 

# operator untuk mengambil item 
keys = teman_teman.keys() 
print(keys) 

for key in teman_teman.keys(): 
    print(teman_teman.get(key)) 
    
values = teman_teman.value() 
print(values) 

for value in teman_teman.values(): 
    print(value) 
    
items = teman_teman.items() 
print(items) 

for item in teman_teman.items(): 
    print(item) 
    
for key,value in teman_teman.items(): 
    print(f"key = {key}, value = {value}")