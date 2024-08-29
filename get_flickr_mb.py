#!/usr/bin/python3


import flickrapi
import flickr_config
import pprint

extra_params={}
user_id='lesleyablack' #'andrewblack'

flickr = flickrapi.FlickrAPI(flickr_config.API_KEY, flickr_config.API_SECRET, format='parsed-json')
date_prev = ''
photos = flickr.photos.search(user_id=user_id,extras='date_taken,description,geo,tags,machine_tags,url_m',**extra_params)
for photo in photos['photos']['photo']:
    date = photo['datetaken'][0:10]

    if date != date_prev:
        print("------------------")
        print(date)
        date_prev = date 


    print(f'  {photo["title"]}' )
    print ("    " + photo['url_m'])
    print ("    " + photo['tags'])
    
    print ()