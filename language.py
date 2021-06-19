game_dict = {"en":{"game_title"         : "TOWER OF HANOI",
                    # About
                   "about"              : "About",
                   "about_text"         : "Projects of\nElementary Number Theory Course (MA2252)\n2nd Semester of Academic Year 2018/2019\nLecturer : Hilda Assiyatun, M.Si., Ph.D.\n\nGame created by:\n10117005 Irma Nazelia\n10117019 Ilma Aliya Fiddien\n10117073 Nurul Syafithri\n10117113 Agapitus Keyka Vigiliant ",
                   "play_now"           : "Play Now!",
                   "instruction"        : "How To Play",
                   "instruction_text"   : "In this game, there are three pegs and some discs of different sizes. The objective of this game is to move the discs on the leftmost peg to the rightmost peg. You can use the middle peg to help you.\n\nThere is only one rule of this game. That is, a disc cannot be placed over a larger disc.\n\nTo move a disc, drag and drop the disc to the targeted peg.\n\nDo this procedure repeatedly until you manage to move all the discs to the rightmost peg.",
                   "highscore"          : "Highscore",
                    # Settings
                   "settings"           : "Settings",
                   "sound"              : "Sound",
                   "language"           : "Language",
                    # Play
                   "enter_name"         : "Write your name then press enter",
                   "play_info"          : "{} moves in {} seconds",
                   "number_discs"       : "Select the number of discs",
                   "play_again"         : "Play again",
                   "change_disc"        : "Change the number disc",
                   "main_menu"          : "Main menu",
                   "congrats_min"       : "Congratulations! You just finished the game with the minimums movements! :)",
                   "congrats_aja"       : "You just finished the game, now try again with the minimum movements! ;)",
                    # History
                   "next"               : "next",
                   "history"            : "History",
                   "history_text"       : "The Tower of Hanoi is a puzzle that was widely believed to be invented by the French mathematician Eduoard Lucas in 1883.\n\nThe puzzle, also called the Tower of Brahama or End of the World Puzzle, was created out of an old Hindu legend.\n\nThe story tells of a Hindu temple at the center of the world where priests were given a stack of 64 golden disks of decreasing size.\n\nThe disks were stacked on one of three towers. The priests were to transfer the stack of disks from the starting tower to another, using some given rules.\n\nThe priests were to work diligently. There are some variations of this legend.",
                   "the_secret"         : "The Secret",
                    # secret
                   "secret"             : "The Mathematic Secret...",
                   "secret_text1"       : "There is a mathematical secret behind this game… It turns out you only need no more than 2^n-1 moves to move n discs from the initial peg to the final peg. This optimum solution is based on a recursive process. That is, a process which is done repeatedly.\n\nBy knowing this process, you can solve this game much quicker! All you need to do is memorising this process (or as we like to call it, algorithm).\n\nTo make things easier, we label the peg A, B, and C, as follows.",
                   "secret_text2"       : "So the main idea behind the algorithm to solve the game using n discs can be summarised as follows:\n\n1. Move all discs, except the largest one, from initial peg (A) to auxiliary (a peg other than the initial and target peg) peg (B).\n\n2. Move the largest disc from initial peg (A) to target peg (C).\n\n3. Move the discs which is now in auxiliary peg (B) to target peg (C). ",
                   "secret_text3"       : "Obviously we cannot move more than 1 disc at once, so step 1 and step 3 can only be done using multiple steps. So how to do step 1 and 3?\n\nJust use this algorithm! But instead of setting A as the initial peg and C as the target peg, set A as the initial peg and B as the target peg because we want to move n-1 discs from peg A to peg B, if you want to do step 1. Similarly, set B as the initial peg and C as the final peg if you want to execute step 3 above.\n\nThe point is, use this algorithm whenever you want to move a set of discs by adjusting the initial peg, auxiliary peg, and the target peg accordingly.",
                   "secret_text4"       : "So where does the 2^n-1 come from?\n\nWell, let’s have a look at our algorithm. Let Hn be the number of moves needed to move n discs from an initial peg to target peg. Since there are n-1pegs to be moved in step 1, thus step 1 needs H^n-1 moves. It is obvious that step 2 needs only 1 move.\n\nHow about step 3? For the same reason as step 1, it needs Hn-1moves. So, we can conclude that H^n = H^n-1 + H^n-1 + 1 = 2Hn^-1 + 1. By solving this recurrence relation, you can find that H^n = 2^n - 1, by setting H^1 = 1.\n\nThis result can also be proved using induction.",
		   "citation_text"	: "Source:\n\nLiu, D. The Tower of Hanoi.\nRetrieved from http://www2.mtsd.k12.wi.us/homestead/users /ordinans/Tower%20of%20Hanoi.html. \n\nMG's Tower of Hanoi For Python.\nRetrieved from https://www.pygame.org/project/3191"},

             "id":{"game_title"         : "MENARA HANOI",
                    # About
                   "about"              : "Tentang",
                   "about_text"         : "Tugas Besar Mata Kuliah\nPengantar Teori Bilangan (MA2252)\nSemester 2 Tahun Ajaran 2018/2019\nDosen Pengampu : Hilda Assiyatun, M.Si., Ph.D.\n\nPermainan dibuat oleh:\n10117005 Irma Nazelia\n10117019 Ilma Aliya Fiddien\n10117073 Nurul Syafithri\n10117113 Agapitus Keyka Vigiliant. ",
                    # Instruction
                   "play_now"           : "Main!",
                   "instruction"        : "Cara Bermain",
                   "instruction_text"   : "Dalam permainan ini terdapat 3 tiang dan beberapa buah piringan berukuran berbeda. Anda harus memindahkan piringan-piringan tersebut dari tiang paling kiri ke tiang paling kanan dengan tiang tengah sebagai alat bantu.\n\nAturan mainnya hanya satu, yakni piringan yang lebih besar tidak boleh diletakkan di atas piringan yang lebih kecil.\n\nUntuk memindahkan piringan, geser lalu lepaskan piringan pada tiang tujuan.\n\nLakukan prosedur tersebut secara terus-menerus sampai Anda berhasil memindahkan semua piringan ke tiang paling kanan.",
                   "highscore"          : "Peringkat",
                    # Settings
                   "settings"           : "Pengaturan",
                   "sound"              : "Suara",
                   "language"           : "Bahasa",
                    # Play
                   "enter_name"         : "Tulis namamu lalu tekan enter",
                   "play_info"          : "{} gerakan dalam {} detik",
                   "number_discs"       : "Pilih banyaknya piringan",
                   "play_again"         : "Main lagi",
                   "change_disc"        : "Ubah banyaknya disk",
                   "main_menu"          : "Menu utama",
                   "congrats_min"       : "Yeay! Kamu menyelesaikan game dengan langkah yang efisien! :)",
                   "congrats_aja"       : "Yeay! Coba lagi sampai langkahnya efisien, ya! ;)",
                    # History
                   "next"               : "lanjut",
                   "history"            : "Sejarah",
                   "history_text"       : "Menara hanoi adalah teka-teki yang seringkali dianggap ditemukan oleh Eduoard Lucas, seorang matematikawan Prancis, pada tahun 1883.\n\nTeka teki ini, yang juga dikenal dengan Menara Brahama atau Teka-teki Akhir Dunia, terinspirasi dari sebuah legenda Hindu.\n\nLegenda ini menceritakan tentang pura Hindu yang diletakkan di pusat dunia.\n\nDi pura ini, para pendeta Hindu diberikan tumpukan yang terdiri dari 64 kepingan emas dengan ukuran yang semakin mengecil dan ditumpuk diatas salah satu dari tiga tiang.\n\nPara pendeta harus memindahkan kepingan-kepingan tersebut dari salah satu tiang ke tiang lainnya menurut aturan-aturan tertentu. Para pendeta ini mengerjakan hal tersebut dengan sungguh-sungguh.\n\nTerdapat versi yang berbeda-beda dari legenda ini.",
                   "the_secret"         : "Rahasianya",
                   # secret
                   "secret"             : "Rahasia Matematika...",
                   "secret_text1"       : "Ternyata, terdapat konsep matematika yang menarik di balik game ini! Untuk menyelesaikan game ini, Anda tidak membutuhkan lebih 2^n-1 gerakan dengan n adalah jumlah kepingan. Terdapat banyak cara untuk menunjukkan hal ini. Salah satu cara tersebut adalah dengan menggunakan proses rekursif, yaitu prosedur yang dilakukan secara berulang-ulang.\n\nDengan mengetahui proses (algoritma) ini, Anda bisa menyelesaikan permainan ini dengan lebih cepat.\n\nUntuk memudahkan penjelasan, mari kita namakan tiang-tiang dengan tiang A, B, dan C.",
                   "secret_text2"       : "Jadi, inti dari algoritma penyelesaian dari permainan ini terdiri dari 3 langkah:\n\n1. Pindahkan semua kepingan selain kepingan paling besar dari tiang awal (A) ke tiang selain tiang awal dan tiang tujuan (tiang B).\n\n2.Pindahkan kepingan paling besar dari tiang awal (A) ke tiang tujuan (C).\n\n3. Pindahkan kepingan-kepingan yang sekarang berada di tiang selain tiang awal dan tiang tujuan (B) ke tiang tujuan (C).",
                   "secret_text3"       : "Jelas bahwa kita tidak bisa memindahkan lebih dari satu keping dalam satu langkah sehingga langkah 1 dan langkah 3 tidak bisa dilakukan sekali jalan. Lalu bagaimana melakukan, misalnya, langkah 1?\n\nMudah saja, gunakan algoritma yang sama, tetapi anggap tiang awal adalah tiang A dan tiang tujuan adalah tiang B sebab dalam langkah 1 kita ingin memindahkan semua keping (selain keping terbesar) dari A ke B. Hal yang serupa bisa diaplikasikan pada langkah tiga dengan menganggap tiang B sebagai tiang awal dan tiang C sebagai tiang tujuan.\n\nAplikasikan algoritma ini setiap kali anda ingin memindahkan kepingan-kepingan dengan menyesuaikan tiang awal dan tiang akhir sesuai tujuan Anda.",
                   "secret_text4"       : "Lalu, dari mana kita tahu bahwa kita memerlukan 2^n-1 langkah untuk memindahkan n keping?\n\nHasil tersebut bisa didapat dengan memperhatikan algoritma yang digunakan. Misal Hn adalah langkah yang diperlukan untuk memindahkan n keping dari tiang awal ke tiang tujuan. Sebab kita ingin memindahkan n-1 keping pada langkah 1, banyaknya langkah yang diperlukan untuk melakukan langkah 1 adalah H^n-1. Jelas bahwa kita perlu hanya 1 langkah untuk melakukan langkah 2.\n\nDengan alasan yang serupa dengan langkah 1, kita memerlukan Hn-1 langkah untuk melakukan langkah 3 sehingga kita mendapatkan hubungan rekursif H^n = H^n-1 + H^n-1 + 1 = 2H^n-1 + 1.\n\nDengan menginisialisasi nilai H^1 = 1, bisa didapat bahwa Hn = 2^n-1. Hasil ini juga dapat dibuktikan menggunakan induksi.",
		   "citation_text"  	: "Sumber:\n\nLiu, D. The Tower of Hanoi.\nDiterima dari http://www2.mtsd.k12.wi.us/homestead/users /ordinans/Tower%20of%20Hanoi.html. \n\nMG's Tower of Hanoi For Python.\nDiterima dari https://www.pygame.org/project/3191"}
             }
