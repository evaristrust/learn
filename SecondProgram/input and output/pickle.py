# concept: Serialization: the process that allows objects to be saved to file
#                           so that they can be restored from the file later

# python provides mechanism of serializing objects using method called pickling

import pickle

imelda = ("More Maythtem",
          "Imelda May",
          "2011",
          ((1, "Pulling the Rug"),
           (2, "Maythem"), (3, "Pscho"),
           (4, "Kentish Town waltz")))
# going to save this tuple using pickle methods

with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)

# then how to retrieve it?

with open("imelda.pickle", 'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
print(imelda2)

album, artist, year, tracks = imelda

print(album)
print(artist)
print(year)

for song in tracks:
    track_number, track_name = tracks
    print(track_number, track_name)

# You can also stored different types of data or information in
# one file ...
# for example, store odd and even numbers ... nothing hard

