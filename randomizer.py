#@author: Flavia Ninsiima Delmira
#@email: delmira91@gmail.com

'''This code will randomly sample the metadata of 100 images
   the metadata is in a file ImageMetadataExtractor.csv
   that was generated by the MetadataExtractor.py
'''

import random   #for randomizing
import csv      #for opening Metadata.csv file

#ignore the next line of code
#random_lines=random.sample(list(open('ImageMetadatorExtractor.csv')))

#opening our file in read mode
readdata = csv.reader(open('ImageMetadata.csv','r'))

#create empty list that stores our rows of read lines
metadata=[]
for row in readdata:
    metadata.append(row)

#popping the headers of the columns i.e...titles such as ImageName,Date,Time,...
#refer to MetadataExtractor.py to understand the above comment
Header = metadata[0]
metadata.pop(0)

#randomly picking 100 lines of metadata
random_metadata_list = random.sample(metadata,100)


no_gps_count = 0
for item in random_metadata_list:
    if item[4] == 'None':
        no_gps_count += 1


print '...printing percentage that have gps: '
print str(100-no_gps_count) + '%'
print '...printing percentage that have no gps: '
print str(no_gps_count) + '%' 
