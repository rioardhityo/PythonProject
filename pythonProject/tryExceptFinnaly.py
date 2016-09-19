orang = {"nama":"syuaib", "kota":"jepara", "umur":"20"}

try:
    print orang["pekerjaan"]
except KeyError, e:
    print "Terjadi error KeyError: ", e
finally:
    print "baris ini akan selalu dieksekusi"    

print orang
