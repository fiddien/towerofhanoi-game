import random
import pickle

def color_use(var):
    """Digunakan untuk ngambil kode warna yang dipakai"""

    # warna umum yang sering dipakai selama game berjalan
    col_color = {"black": (33, 33, 33),
                 "white": (220, 237, 200)
                 }

    # warna spesifik ke suatu objek
    col_object = {"background": (220, 237, 220),           
                  "button_ok": (0, 188, 212),              # strongbluesky
                  "button_ok_hover": (0,200,222),          
                  "button_no": (104,159,56),               # green
                  "button_no_hover": (139, 195, 74),       # lightgreen
                  "button_normal": (189, 189, 189),        # ngga kepikiran
                  "button_normal_hover": (244, 244, 244),  # ngga kepikiran
                  "board_color": (33, 33, 33),
                  "disc_1": (102, 145, 133),
                  "disc_2": (110, 155, 133),
                  "disc_3": (118, 135, 133)
                  }

    # outputkan kode warna yang bersesuaian dengan var
    if var in col_color:
        return(col_color[var])
    elif var in col_object:
        return(col_object[var])
    else:
        print('tidak ada "{}" di color()'.format(var))


def color_random():
    """Ngehasilkan warna random

    mungkin kepakai di GamePlay, kalau warna disknya mau random."""
    return (random.randint(100, 220),
            random.randint(100, 220),
            random.randint(100, 220))

def data_read():
    """ngebuka dan ngebaca data dari database"""

    # coba buka database, kalau database ngga ada, isi dengan data default
    try:
        with open("database.pkl", "rb") as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = {'sound': True,
                'lang': True, #pilih en
                'hof': {3: [], 4: [], 5: [], 6: [], 7: []}
                }

    return data

def data_write(data):
    """ngebuka dan nulis semua data ke database"""

    # simpan data ke database. kalau database ngga ada, file baru
    # otomatis dibuat terlebih dahulu.
    with open("database.pkl", "wb") as f:
        pickle.dump(data, f)


def algo_addSorted(HOF, disks, newdata):
    """menambahkan databaru ke HOF dengan menjaga data tetap terurut. Hall Of
    Fame (HOF) bentuknya dict dengan key banyak disks.

    value untuk setiap key adalah list dengan format:
    [[username, totaltime, totalmove]]"""
    
    LIMIT = 3

    def sortkey(item):
        "aturan ngesort"
        return (item[1], item[2])

    HOF[disks].append(newdata)
    HOF[disks] = HOF[disks][:LIMIT]
    HOF[disks].sort(key=sortkey)
    return HOF


def algo_makeHOF(HOF):
    """ngehasilkan teks daftar peringkat yang bisa dicetak ke layar"""

    teks = ''
    for level in HOF:
        teks += "Level {}\n".format(level)
        for ranking in HOF[level]:
            teks += "{:20} {:20} {:20}\n".format(ranking[0], ranking[1], ranking[2])
        teks += '\n'

    teks = teks[:-2]
    return teks
