#import flickr_api

#flickr_api.set_keys(api_key = 'f7b255ae41bcdc3b873be83f1cd17308', api_secret = 'a460d7ea98349d52')
#a = flickr_api.auth.AuthHandler();
#flickr_api.set_auth_handler(a);
#url = a.get_authorization_url('write');
#print url

#flickr_api.set_auth_handler('login')
#photoset = flickr_api.Photoset.create(title = "The title of the photoset", primary_photo=photos[0])
#USAR LA OTRA API :(
#user = flickr_api.test.login()

import flickr_api
flickr_api.set_keys(api_key = 'f7b255ae41bcdc3b873be83f1cd17308', api_secret = 'a460d7ea98349d52')
flickr_api.set_auth_handler('login')
user = flickr_api.test.login()
photos = user.getPhotos()
#listar photos y agregar la ultima al photoset que quiero
import flickapi
api_key = '10cd65c09e76e712b4f338ae1b51d3a4'
api_secret = 'f5228a3aeda5c4bf'
flickr = flickrapi.FlickrAPI(api_key, api_secret)
(token, frob) = flickr.get_token_part_one(perms='write')
flickr.get_token_part_two((token, frob))
flickr.upload(filename='test.jpg', callback=None)
#Subir photo
