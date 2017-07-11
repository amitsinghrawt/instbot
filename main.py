import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

APP_ACCESS_TOKEN = '4777564375.e5bdecf.cf7da029386947f1be3f647066303471'
#it is the base url of instabot
BASE_URL = 'https://api.instagram.com/v1/'
#this funtion is use for collecting the informtion of over
def self_info():
    try:
        request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_info = requests.get(request_url).json()
    except:
        print "get request is not working "
    try:
      if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            #get the informtion of self
          print 'Username: %s' % (user_info['data']['username'])
          print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
          print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
          print 'User does not exist!'
      else:
        print 'Status code other than 200 received!'
    except:
        KeyError
    #this fuction is use for showing the recent post owner
def get_own_post():
    try:
      request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
      print 'GET request url : %s' % (request_url)
      own_media = requests.get(request_url).json()
    except:
        print"get request is not working"
    try:
        if own_media['meta']['code'] == 200:
            if len(own_media['data']):
                image_name = own_media['data'][0]['id'] + '.jpeg'
                image_url = own_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print "your post is downloading"
            else:
                print 'Post does not exist!'
        else:
            print 'Status code other than 200 received!'
    except:
        KeyError
#this fuction is use for collting the informtion of other user
def get_user_id(insta_username):
    try:
        request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_info = requests.get(request_url).json()
    except:
        print"get request is not working"
    try:
      if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
             return None

      else:
        print 'Status code other than 200 received!'
        exit()
    except:
        KeyError
#this fuction is use for geting the recent post of instagram user
def get_user_post(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  else:
    try:
      request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
      print 'GET request url : %s' % (request_url)
      user_media = requests.get(request_url).json()
    except:
        print"get request is not working"
    try:
      if user_media['meta']['code'] == 200:
        if len(user_media['data']):
          image_name = user_media['data'][0]['id'] + '.jpeg'
          image_url = user_media['data'][0]['images']['standard_resolution']['url']
          #now we are download the post of user
          urllib.urlretrieve(image_url, image_name)
          return user_media['data'][0]['id']
          print 'Your image has been downloaded!'
        else:
          print 'Post does not exist!'
      else:
        print 'Status code other than 200 received!'
    except:
        KeyError
      #this function for get the informtion of other user
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  else:
    try:
      request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
      print 'GET request url : %s' % (request_url)
      user_info = requests.get(request_url).json()
    except:
        print"get request is not working"
    try:
      if user_info['meta']['code'] == 200:
        if len(user_info['data']):
          #get the infomtion of instgram user
          print 'Username: %s' % (user_info['data']['username'])
          print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
          print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
          print 'There is no data for this user!'
      else:
        print 'Status code other than 200 received!'
    except:
        KeyError
    #this function for like the post
def get_media_id(user_id):

    try:
        request_url = (BASE_URL + "users/%s/media/recent?&access_token=%s") % (user_id, APP_ACCESS_TOKEN)  #fetching the recent media of user using user_id and acesstoken

        print "The GET request url is %s" % (request_url)       # display the GET url
        user_info = requests.get(request_url).json()        # requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print ("GET request isn't working properly", "red")  # print this when get request isn't correct

    try:
        if user_info['meta']['code'] == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):       # checking if we have anything in data of friend's if
                id = user_info['data'][0]['id']        # storing the id of friend in "id" variable
                return id           # returning the id
            else:
                return None         #if no data in corresponding instaname then return none
        else:
            print("The request url is not in accepted state")  # print when status is in "not accepted" state
    except:
        KeyError  # catching keyerror of dictionary user-info
        print KeyError

def like_a_post(insta_username):
  user_id = get_user_id(insta_username)
  if(user_id==None):
      print ' you enter invilad id'
  else:
      media_id=get_media_id(user_id)
      if(media_id==None):
          print"there is no media"
      else:
          try:
                request_url = (BASE_URL + 'media/%s/likes') % (media_id)
                payload = {"access_token": APP_ACCESS_TOKEN}
                print 'POST request url : %s' % (request_url)
                post_a_like = requests.post(request_url, payload).json()
          except:
              print"request is not working"
          try:
            if post_a_like['meta']['code'] == 200:
                print 'Like was successful!'
            else:
                print 'Your like was unsuccessful. Try again!'
          except:
                print KeyError

    #we are comment on the post
def comment_on_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id==None:
        print'invailed user id'
    else:
        media_id = get_media_id(user_id)
        if media_id==None:
            print"no media found"
        else:
            try:

                comment_text = raw_input("Your comment: ")
                payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
                request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                print 'POST request url : %s' % (request_url)

                make_comment = requests.post(request_url, payload).json()
            except:
                    print'request is not working'
            try:
                  if make_comment['meta']['code'] == 200:
                        print "Successfully added a new comment!"
                  else:
                        print "Unable to add comment. Try again!"
            except:
                print KeyError


def own_comment_info():
    #this fuction is use for comment on self post
     user_id=get_own_post()
     if user_id==None:
         print "invaied user id"
     else:
        media_id = get_media_id(user_id)
        if media_id==None:
            print"no medaia found"
        else:
            try:
                request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
                print 'GET request url : %s' % (request_url)
                comment_info1 = requests.get(request_url).json()
            except:
                print"request is not working"
            try:
                 if comment_info1['meta']['code'] == 200:
                     if len(comment_info1):
                         a = 0
                         for a in range(0,len(comment_info1["data"])):
                             print "%s commented : %s" % (comment_info1["data"][a]["from"]["username"], comment_info1["data"][a]["text"])
                             a = a + 1
                     else:
                         print "no data"
                 else:
                   print"code not 200"
            except:
               print KeyError


def unlike_a_post(insta_username):
    # This function gets input as instagram username of your friend and unlike the recent post of your friend
    user_id = get_user_id(insta_username)         #calling get_user_id()
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)        #calling get_media_id()
        if media_id == None:
            print "There is no media in this account"  # print when media id is null
        else:
            try:
                request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)      #url of liking the recent post corresponding to media id
                post_del = requests.delete(request_url).json()      #deleteing the data to the url above mentioned using requests package and using json()
            except:
                print ("DELETE request is not working properly")  # print when incorrect url

            try:
                if post_del['meta']['code'] == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    print ("SUCESSFULLY UNLIKED THE POST")      #print if post is sucessfully unliked
                else:
                    print"You couldn't unlike the POST :"          #printing if post is not sucessfully unliked
            except:
                KeyError        #catching
#this funtion is use for geting the list how like your post

def get_like_list(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print'invailed user name'
    else:
        media_id=get_own_post()
        if media_id==None:
            print "no media found"
        else:
            try:
                request_url=(BASE_URL+'media/%s/like/?access_token=%s')%(media_id,APP_ACCESS_TOKEN)
                payload = {"access_token": APP_ACCESS_TOKEN}
                print'Get request url : %s'%(request_url)
                post_a_like = requests.get(request_url, payload).json()
            except:
                print'request is not working'
            try:
                if post_a_like['meta']['code'] == 200:
                     if len(post_a_like):
                         a=0
                         while a<len(post_a_like):
                                print "%s like : "%(post_a_like["data"][a]["from"]["username"])
                                a=a+1
                     else:
                        print "no data"
                else:
                     print"code not 200"
            except:
                print KeyError
#this function is use for download the recent image liked by owner
def recent_media_liked():
    try:
        request_url=(BASE_URL +"user/self/media/liked?accec_token=%s")%APP_ACCESS_TOKEN
        print'the get request url is %s'%request_url
        liked_post=requests.get(request_url).json()
    except:
        print'get request is not working'
    try:
        if(liked_post['meta']['code'])==200:
            if len(liked_post['data']):
                image_name=liked_post['data'][0]['id'] + '.jpeg'
                image_url=liked_post['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url,image_name)
                print'your image has been downloaded'
            else:
                print'you did not liked any post recently'
        else:
            print'the request url is not accepted'
    except:
        print KeyError

#this for geting the comment on post
def get_comment_list(insta_username):
     user_id=get_user_id(insta_username)
     if user_id==None:
         print 'invaild user name'
     else:
         media_id = get_own_post()
         if media_id==None:
             print'no media found'
         else:
             try:
                request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
                print 'GET request url : %s' % (request_url)
                comment_info = requests.get(request_url).json()
             except:
                 print'request is not working'
             try:
                 if comment_info['meta']['code'] == 200:
                     if len(comment_info):
                         a=0
                         while a<len(comment_info):
                                print "%s commented : %s"%(comment_info["data"][a]["from"][""],comment_info["data"][a]["text"])
                                a=a+1
                     else:
                         print "no data"
                 else:
                     print"code not 200"
             except:
                 print KeyError

def delete_negative_comment(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print'invailed user name'
    else:
        media_id = get_media_id(user_id)
        if media_id==None:
            print'no media found'
        else:
            try:
                request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
                print 'GET request url : %s' % (request_url)
                comments_info= requests.get(request_url).json()
            except:
                print'request is not found'
            try:
                if comments_info['meta']['code'] == 200:
                    if len(comments_info['data']):
                              # Here's a naive implementation of how to delete the negative comments :)
                        for x in range(0, len(comments_info['data'])):
                            comment_id = comments_info['data'][x]['id']
                            comment_text = comments_info['data'][x]['text']
                            blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())

                            if (blob.sentiment.p_neg > blob.sentiment.p_pos):

                                print 'Negative comment : %s' % (comment_text)
                                try:
                                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                                    print 'DELETE request url : %s' % (delete_url)
                                    delete_info = requests.delete(delete_url).json()
                                    if delete_info['meta']['code'] == 200:
                                        print 'Comment successfully deleted!\n'
                                    else:
                                        print 'Unable to delete comment!\n'
                                except:
                                    print'comment not find'
                            else:
                                print 'Positive comment : %s\n' % (comment_text)
                    else:
                        print 'There are no existing comments on the post!\n'
                else:
                    print 'Status code other than 200 received!\n'
            except:
                print KeyError


def StartBot():
    print("Welcome to InstaBot app")  # ***  WELCOMING INSTABOT USER ***
    print ('Here are your menu options:')
    while True:
                       #Printing various menu option
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get user's recent post by username\n"
        print "e.Get list of people who has liked your posts\n"
        print "f.Like the post of your friend\n"
        print "g.get list of recent comment on your post\n "
        print "h.Comment on post\n"
        print "i.Delete negative comments \n"
        print"j.unlike user post"
        print"k.to get recent media liked by the user"
        print "x.Exit the application"
        choice = raw_input("enter your choice\n")
        #getting menu choice from user6
        if(choice.isalpha()):
            if choice =="a":
                self_info()         #if choice is "1" then self_info() called
            elif choice == "b":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_info(insta_username)     #if choice is "2" then get_user_info() called and friend's insta name is passed as parameter
            elif choice == "c":
                get_own_post()      #if choice is 3 then get_own_post() called
            elif choice =="d":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_post(insta_username)  # if choice is "4" then get_user_post() called and friend's insta name is passed as parameter
            elif choice=="e":
                insta_username = raw_input("Enter the username of the user: " )
                get_like_list(insta_username)
            elif choice=="f":
                insta_username = raw_input("Enter the username whose post you want to like")
                like_a_post(insta_username)
            elif choice == "g":
                insta_username=raw_input('Enter the username of the user')
                get_comment_list(insta_username)
            elif choice =="h":
                insta_username = raw_input("Enter the username whose post you want to comment on: ")
                comment_on_post(insta_username)
            elif choice=="i":
                insta_username=raw_input('Enter the username :')
                delete_negative_comment(insta_username)
            elif choice=="j":
                insta_username=raw_input("Enter the username whose post you want to unlike:")
                unlike_a_post(insta_username)
            elif choice=="k":
                recent_media_liked()
            elif choice=="x":
                exit()              #exit the program

             #if choice entered is wrong then print
        else:
            print("You have entered a wrong choice !Try Again")

StartBot()
