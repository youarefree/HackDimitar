from hashing import *


users = [("Rositsa Zlateva", encode_pass("rosiZlat@")),
         ("Slavyana Monkova", encode_pass("obichamWow")),
         ("Dimitar Yordanov", encode_pass("slavyanaM@")
          ), ("Kiril Hristov", encode_pass("abcdefG@12")),
         ("Mariana Dincheva", encode_pass("miMimiMi@")),
         ("Anna Hristova", encode_pass("avelinAries@")),
         ("Viktoriya Kertikova", encode_pass("vikiViki"))]
movies = [("The Hunger Games: Catching Fire", 7.9),
          ("Wreck-It Ralph", 7.8), ("Her", 8.3)]
reservations = [(3, 1, 2, 1),
                (3, 1, 3, 5),
                (3, 1, 7, 8),
                (2, 3, 1, 1),
                (2, 3, 1, 2),
                (5, 5, 2, 3),
                (6, 5, 2, 4)]

projections = [(1, "3D", "2014-04-01", "19:10"),
               (1, "2D", "2014-04-01", "19:00"),
               (1, "4DX", "2014-04-02", "21:00"),
               (3, "2D", "2014-04-05", "20:20"),
               (2, "3D", "2014-04-02", "22:00"),
               (2, "2D", "2014-04-02", "19:30")]
