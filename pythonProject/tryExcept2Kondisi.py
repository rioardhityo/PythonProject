orang = {"nama":"syuaib", "kota":"jepara", "umur":"20"}

try:
    contact = open("contact.txt", 'r')
    print orang["pekerjaan"]
except IOError, e:
    print "Terjadi error IO: ", e
except KeyError, e:
    print "Terjadi kesalahan pada akses list/dict/tuple:", e

print orang
