#!/usr/bin/python3


import flickrapi
import flickr_config
import pprint
import re
import sys

extra_params={}
# For command line
user_id = sys.argv[1]  # eg'lesleyablack' or 'andrewblack'
min_taken_date = sys.argv[2 ] # eg '2024-08-29'
unwanted = 'churchdetail'


flickr = flickrapi.FlickrAPI(flickr_config.API_KEY, flickr_config.API_SECRET, format='parsed-json')
date_prev = ''
photos = flickr.photos.search(user_id=user_id, \
                            #tags=tags, \
                            min_taken_date =min_taken_date, \
                            extras='date_taken,description,geo,\
                            tags,machine_tags,url_m',\
                            **extra_params)
for photo in photos['photos']['photo']:
    tags=photo['tags']

    if not re.search(unwanted,tags) :
        ## re.search(f'\b{unwanted}\b',tags) :
   
        date = photo['datetaken'][0:10]
        if date != date_prev:
            print("------------------")
            print(date)
            date_prev = date 

        print(f'  {photo["title"]}' )
        print ("    " + photo['url_m'])
        print ("    " + photo['tags'])
        
        print ()