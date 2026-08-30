# Variabel adalah tempat menyimpan data 
# menaruh / assignment nilai # di python tidak perlu deklarasi

a = 10 
x = 5 
panjang = 1000 

# pemanggilan pertama 

print("Nilai a = ", a) 
print("Nilai x = ", x) 
print("Nilai panjang = ", panjang) 

# penamaan      
nilai_y = 15 # dengan menggunakan underscore   
juta10 = 10000000 # ini boleh   
nilaiZ = 17.5 # ini boleh    

# pemanggilan kedua  
print("Nilai a = ", a)  
a = 7  
print("Nilai a = ", a)   
# assignment indirect  
b = a  
print("Nilai b = ", b) 

#TIPE DATA

a = 10 # a adalah variable dengan nilai 10 

data_integer = 1   
print("data : ", data_integer)   
print("- bertipe ", type(data_integer))

data_float = 1.5   
print("data : ", data_float)   
print("- bertipe ", type(data_float))

data_string = "ucup"    
print("data : ", data_string)   
print("- bertipe ", type(data_string))

data_bool = True   
print("data : ", data_bool)   
print("- bertipe ", type(data_bool)) 

data_complex = complex(5,6)   
print("data : ", data_complex)   
print("- bertipe ", type(data_complex)) 

from ctypes import c_double    

data_c_double = c_double(10.5)   
print("data : ", data_c_double)   
print("- bertipe ", type(data_c_double)) 


# KONFERSI TIPE DATA
data_int = 9    
data_float = float(data_int)  
data_str = str(data_int)  
data_bool = bool(data_int) # akan false jika nilai integer = 0   
print("data = ", data_float, ",type = ", type(data_float))  
print("data = ", data_str, ",type = ", type(data_str))  
print("data = ", data_bool, ",type = ", type(data_bool)) 

data_float = 9.2    
data_int = int(data_float)  
data_str = str(data_float)  
data_bool = bool(data_float) # akan false jika nilai integer = 0   
print("data = ", data_int, ",type = ", type(data_int))  
print("data = ", data_str, ",type = ", type(data_str))  
print("data = ", data_bool, ",type = ", type(data_bool)) 

data_str = "10"    
data_int = int(data_str)  
data_float = float(data_str)  
data_bool = bool(data_str)    
print("data = ", data_int, ",type = ", type(data_int))  
print("data = ", data_float, ",type = ", type(data_float))  
print("data = ", data_bool, ",type = ", type(data_bool)) 


# MENGAMBIL INPUT DATA DARI USER
data = input("Masukan data: ") 
print("data ",data,",type =",type(data)) 

angka = int(input("masukan angka: ")) 
print("data ",angka,",type =",type(angka))