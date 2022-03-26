class Yin: pass
class Yang:
    def __del__(self):
        print("Yang destruido")
        print("?")
yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)
print(yang is yin.yang)
del(yang)

