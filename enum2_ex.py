from enum import Enum

class hari(Enum):
    Senin   = 1
    Selasa  = 2
    Rabu    = 3
    Kamis   = 4
    Jumat   = 5
    Sabtu   = 6
    Minggu  = 7

h1 = hari.Senin.value
h2 = hari.Minggu.value
selisih = h2-h1
print("Selisih hari = ", selisih)