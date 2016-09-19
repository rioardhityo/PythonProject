def hello():
    print "Hello world"

def getDBConfig():
    config = {
        "driver":"sqlite3",
        "name":"testing.db",
        "path":"/home/user/Documents"
    }

    return config

def getName(id):
    if id == 1:
        name = "Alexander Grotesqiue"
    elif id == 2:
        name = "Saleh Mahmoud Al Qassam"
    elif id == 3:
        name = "Natasha Vorvanova"

    return name

def getHargaDealer(harga):
    harga_baru = harga + ((harga / 100.0) * 15.0)
    return harga_baru

def getNumberList(length):
    x = range(0, length)
    return x

def getLuasPersegiPanjang(p, l):
    x = p * l
    return x

hello()

db_config = getDBConfig()
print db_config

name = getName(3)
print name

harga_dealer = getHargaDealer(1000000)
print harga_dealer

number_list = getNumberList(10)
print number_list

luas = getLuasPersegiPanjang(20, 10)
print luas
