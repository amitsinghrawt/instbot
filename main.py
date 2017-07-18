import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from termcolor import colored
APP_ACCESS_TOKEN = '4777564375.e5bdecf.cf7da029386947f1be3f647066303471'
#it is the base url of instabot
BASE_URL = 'https://api.instagram.com/v1/'
#this funtion is use for collecting the informtion of over
a = []
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
      request_url =(BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
      print 'GET request url : %s'%request_url
      own_media = requests.get(request_url).json()
    except:
        print colored("get request is not working","red")
    try:
        if own_media['meta']['code'] == 200:
            if len(own_media['data']):
                image_name = own_media['data'][0]['id'] + '.jpeg'
                image_url = own_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print colored("your post is downloading","red")
            else:
                print colored('Post does not exist!','red')
        else:
          print colored ('Status code other than 200 received!','green')
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
          print "get request url :%s"%request_url
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
        if len(user_info['data']):#get the infomtion of instgram user
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
        print ("GET request isn't working properly")  # print this when get request isn't correct

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
                print ('POST request url : %s' % (request_url))
                post_a_like = requests.post(request_url,payload).json()
          except:
              print colored("request is not working",'red')
          try:
            if post_a_like['meta']['code'] == 200:
                print colored('Like was successful!','blue')
            else:
                print colored('Your like was unsuccessful. Try again!','red')
          except:
                print KeyError

    #we are comment on the post
def comment_on_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id==None:
        print colored('invailed user id','red')
    else:
        media_id = get_media_id(user_id)
        if media_id==None:
            print colored("no media found",'red')
        else:
            try:

                comment_text = raw_input("Your comment: ")
                payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
                request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                print('POST request url : %s' % (request_url))

                make_comment = requests.post(request_url, payload).json()
            except:
                    print colored('request is not working','red')
            try:
                  if make_comment['meta']['code'] == 200:
                        print "Successfully added a new comment!"
                  else:
                        print "Unable to add comment. Try again!"
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
        media_id=get_media_id(user_id)
        if media_id==None:
            print "no media found"
        else:
           try:
                request_url=(BASE_URL + 'media/%s/likes?access_token=%s')%(media_id , APP_ACCESS_TOKEN)
                print 'Get request url : %s'%(request_url)
                like_list = requests.get(request_url).json()

           except:
                print'request is not working'
           try:
               if(like_list['meta']['code'] == 200):
                   if (like_list['data']):
                       for b in range(0, len(like_list['data'])):
                           print like_list['data'][b]['username']
                   else:
                       print(colored("like doesn't exsist.", 'red'))
               else:
                   print(colored("status code other than 200.", 'red'))

           except:
              print KeyError
#this function is use for download the recent image liked by owner
def recent_media_liked():
    try:
        request_url=(BASE_URL +"users/self/media/liked?access_token=%s")%APP_ACCESS_TOKEN
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
     user_id= get_user_id(insta_username)
     if user_id==None:
         print 'invaild user name'
     else:
         media_id = get_media_id(user_id)
         if media_id==None:
             print'no media found'
         else:
             try:
                request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
                print 'GET request url : %s' % (request_url)
                comment_info = requests.get(request_url).json()
             except:
                 print'request is not working'
             try:
                if comment_info['meta']['code'] == 200:
                    for i, d in enumerate(comment_info["data"]):
                        print d["text"]
                        a.append(d["text"])
                    return a

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
            #try:
                request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
                print 'GET request url : %s' % (request_url)
                comments_info= requests.get(request_url).json()
                print "tt"
            #except:
                print'request is not found'
            #try:
                if comments_info["meta"]["code"]==200:
                    print"ee"
                    if len(comments_info["data"]):
                        print "gg"     # Here's a naive implementation of how to delete the negative comments :)
                        for x in range(0, len(comments_info["data"])):
                            comment_id = comments_info["data"][x]["id"]
                            comment_list = comments_info["data"][x]["text"]
                            blob = TextBlob(comment_list, analyzer=NaiveBayesAnalyzer())
                            print "pp"
                            if(blob.sentiment.p_neg > blob.sentiment.p_pos):
                                print colored("Your comment is %s :(", "red") % comment_list  # print if negtive comment
                                try:
                                    request_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)  # url for getting the commments
                                    print "Delete request url :%s" % (request_url)  # dislay url
                                    del_info = requests.delete(request_url).json()  # deleting the data of the url above mentioned using requests package and using json()
                                except:
                                    print colored("Request URL not coorect!", "red")  # print when url not correct
                                if del_info['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                                    print colored("Comment deleted :) ", "green")  # print when sucessful in deleting negative comments
                                else:
                                    print colored("Unable to delete comment :", "red")  # print when unsucess in deleting comments
                            elif( blob.sentiment.p_neg == blob.sentiment.p_pos):  # if comment have 50-50 ratio of positive and negative sentiment
                                    print colored("Your comment is 50% positive and 50% negative","red")
                                    choice = raw_input(colored("1.Do you want to delete this comment ? \n 2.Do you want to download this image? \n 3.Do want to go back to Mai", "blue"))
                                    if choice == "1":
                                        try:
                                            request_url = (BASE_URL + 'media/%s/comments/%s?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                                            print "Delete request url :%s" % (request_url)
                                            del_info = requests.delete(request_url).json()  # deleting the data of the url above mentioned using requests package and using json()
                                        except:
                                            print colored("Request URL not coorect!", "red")  # print when url not correct
                                        if del_info['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                                            print colored("Comment deleted : ", "green")  # print when sucessful in deleting negative comments
                                        else:
                                            print colored("Unable to delete comment :", "red")  # print when unsucess in deleting comments
                                    elif choice == '2':
                                        try:
                                            request_url = (BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id, APP_ACCESS_TOKEN)  # url for the recent media using userid
                                            print "get request url :%s" % (request_url)
                                            get_img = requests.get(request_url).json()  # deleting the data of the url above mentioned using requests package and using json()
                                        except:
                                            print colored("Request URL not coorect!", "red")  # print when url not correct
                                        if (get_img['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                                            if len(get_img['data']):  # checking if we have anything in data of friend's id
                                                image_name = get_img['data'][0]['id'] + '.jpeg'  # fetching post id from data and storing it in image_name with .jpeg extension
                                                image_url = get_img['data'][0]['images']['standard_resolution']['url']  # getting url of post and storing in image_url
                                                urllib.urlretrieve(image_url,image_name)  # retriving the image from image_url and saving in image_name
                                                print colored('Your image has been downloaded! :) ', "green")  # SUCCESS MESSASGE
                                        elif choice == '3':
                                            StartBot()
                                        else:
                                             print colored("You entered a wrong choice !", "red")  # print when wrong choicce entered
                            else:
                                print colored("%s is a Positive comment : ", "green") % (comment_list)  # print when its a positive commment

                    else:
                         print colored("No comments present on this post", "red")  # print when no comments present on post
                else:
                    print colored("The request url is not in accepted state", "red")
            #except:
                #KeyError
                #print KeyError


def like_min_liked_post(id):
    #This function gets media id as input and like that post

    if id == None:  # check if media id none
        print colored("There is no media in this account", "red")  # print when media id is null
    else:
        try:
            request_url = (BASE_URL + 'media/%s/likes') % (id)  # url to like the post using media id
            payload = {"access_token": APP_ACCESS_TOKEN}  # payload as a dictionary
            print 'POST request url : %s' % (request_url)  # display the POST url
            post_like = requests.post(request_url,payload).json()  # posting  the data to the url above mentioned using requests package and using json()
        except:
            print colored("POST request is not working properly", "red")  # print when incorrect url

        try:
            if post_like['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                print colored("SUCESSFULLY LIKED THE POST :)", "green")  # print if post is sucessfully liked
            else:
                print colored("You couldn't like the POST :( ", "red")  # printing if post is not sucessfully liked
        except:
            KeyError  # catch keyerror
            print KeyError
def choose():
    #this function choose the post with either minimum no of likes or by searching in caption a particular word or sentence

    print colored("Choose one of the following option:) ","blue")
    print colored("a.Choose post with minimum likes of user","yellow")
    print colored("b.Choose any recent post by tag of user","green")
    choice=raw_input("Enter your choice: ")         #taking choice input from user and storing in choice variable
    if choice=='a':
        insta_username=raw_input("Enter the username")
        user_id=get_user_id(insta_username)          #calling get_user_id() and passing the user's instagram name as parameter
        if user_id==None:
            print colored("Invalid username :(",'red')      #if user_id returned from get_user_id() is none then print invalid user!.
        else:
            try:
                request_url = (BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id, APP_ACCESS_TOKEN)   # getting users media list from "user/user_id/media/recent" end point
                print "Get url is: %s" % (request_url)      # display the GET url
                user_media = requests.get(request_url).json()       # requesting to get the data from the url above mentioned using requests package and using json()
            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url

            try:
                if user_media['meta']['code'] == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(user_media['data']):     # checking if we have anything in data of user's id
                        like_list=[]        #creating a list
                        for i in range(len(user_media['data'])):        #for every i the data list
                            likes=user_media['data'][i]['likes']['count']       #getting the like count
                            url=user_media['data'][i]['images']['standard_resolution']['url']       #getting url of posts
                            like_list.append(likes)     #appending the no of likes on every post in like_list[]
                        min_count=min(like_list)            #finding minimum in list
                        print colored("Least number of likes is %s" ,"magenta")%(min_count)
                        #providing user with certain options
                        choice=raw_input("What do you want to do with this post with least likes? \n 1. Download this image?\n 2. Like this post? \n 3.Return to main menu? ")
                        if choice=="1":                                             #download  image function
                            for i in range(len(user_media['data'])):             #for every i the data list
                                if user_media['data'][i]['likes']['count']==min_count:      #comparing no of likes of every post with min likes
                                    get_id=user_media['data'][i]['id']      #fetching id of min liked post
                                    image_name = get_id + '.jpeg'
                                    image_url = user_media['data'][i]['images']['standard_resolution']['url']       #fetching image url
                                    urllib.urlretrieve(image_url, image_name)       #downloadinf image
                            print colored('Your image has been downloaded! :)', 'green')
                        elif choice=="2":           #like the post with min no of liked
                            for i in range(len(user_media['data'])):            #for every i the data list
                                if user_media['data'][i]['likes']['count']==min_count:      #comparing no of likes of every post with min likes
                                    id=user_media['data'][i]['id']      #fetching id of min liked post
                                    like_min_liked_post(id)         #calling like_min_liked_post() function and passing id as parameter
                        elif choice=="3":
                            StartBot()          #going back to main menu
                        else:
                            print colored("Enter the correct choice : ","red")     #print when wrong choice entered
                    else:
                        print colored("There is no data :", "red")  # print when no data
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError  # catching Key error
                print KeyError  # printing keyerror
    elif choice == 'b':
        username = raw_input(colored("Enter the username whose post you want to choose using caption?", "blue"))  # getting username
        user_id = get_user_id(username)  # fetching user id from get_user_id() function
        if user_id == None:
            print colored("Invalid user : ","red")  # if user_id returned from get_user_id() is none then print invalid user!.
        else:
            try:
                request_url = (BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id,APP_ACCESS_TOKEN)  # getting users media list from "user/user_id/media/recent"
                print "GET request url: %s" % (request_url)  # print GET url
                media_list = requests.get(request_url).json()  # requesting to get the data from the url above mentioned using requests package and using json()
            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if media_list['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(media_list['data']):  # checking if we have anything in data of user's id
                        word = raw_input(colored("Enter the word you want to search in caption : ","green"))  # get the word you want to search in caption or hashtag
                        list = []  # creating list
                        for i in range(len(media_list['data'])):  # for every i the data list
                            if media_list['data'][i]['caption'] != None:  # checking if caption is there or not
                                caption = media_list['data'][i]['caption']['text']  # if caption is present then store it in variable
                                list.append(caption)  # appending the caption in list
                            else:
                                print colored("You dont have any caption ", "red")  # print if no caption present
                        if len(list) > 0:  # check if there is any caption in list
                            for i in range(len(list)):  # for every i the data list
                                if word in list[i]:  # if word which is  searched is present in caption
                                    print colored("The caption is : %s ", "magenta") % list[i]
                                    choice = raw_input(colored("Do you want to download this image or not? Y/N ",
                                                               "green"))  # asking if user want to download the post retrieved uby searching caption
                                    if choice.upper() == "Y":  # if yes then download
                                        id = media_list['data'][i]['id']  # fetching id
                                        image_name = id + '.jpeg'
                                        image_url = media_list['data'][i]['images']['standard_resolution']['url']  # fetching url
                                        urllib.urlretrieve(image_url, image_name)  # downloading image
                                        print colored('Your image has been downloaded!','blue')  # print when image downloaded sucessfully
                                    elif choice.upper() == "N":  # if no then return None
                                        return None
                                    else:
                                        print colored("Enter either Y or N!", "red")  # print when wrong choice entered

                        else:
                            print colored("You dont have any caption", "red")  # no caption in any post
                    else:
                        print colored("No data available!", 'red')  # print when no data
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError  # Catching keyerror
                print KeyError  # printing keyerror
    else:
        print colored("Choose either a or b !", 'red')


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
        print "g.get comment list\n "
        print "h.Comment on post\n"
        print "i.Delete negative comments \n"
        print"j.unlike user post"
        print"k.to get recent media liked by the user"
        print "l.To choose post by minimum likes or tag\n"
        print "x.Exit the application"
        choice = raw_input(colored("enter your choice\n","blue"))
        #getting menu choice from user6
        if(choice.isalpha()):
            if choice =="a":
                self_info()         #if choice is "1" then self_info() called
            elif choice == "b":
                insta_username = raw_input(colored("Enter the username of the user: ",'green'))
                get_user_info(insta_username)     #if choice is "2" then get_user_info() called and friend's insta name is passed as parameter
            elif choice == "c":
                get_own_post()      #if choice is 3 then get_own_post() called
            elif choice =="d":
                insta_username = raw_input(colored("Enter the username of the user: ","green"))
                get_user_post(insta_username)  # if choice is "4" then get_user_post() called and friend's insta name is passed as parameter
            elif choice=="e":
                insta_username = raw_input(colored("Enter the username of the user: ",'green') )
                get_like_list(insta_username)
            elif choice=="f":
                insta_username = raw_input(colored("Enter the username whose post you want to like","green"))
                like_a_post(insta_username)
            elif choice == "g":
                insta_username=raw_input(colored('Enter the username of the user','green'))
                get_comment_list(insta_username)
            elif choice =="h":
                insta_username = raw_input(colored("Enter the username whose post you want to comment on: ","green"))
                comment_on_post(insta_username)
            elif choice=="i":
                insta_username=raw_input(colored('Enter the username :','green'))
                delete_negative_comment(insta_username)
            elif choice=="j":
                insta_username=raw_input(colored("Enter the username whose post you want to unlike:","green"))
                unlike_a_post(insta_username)
            elif choice=="k":
                recent_media_liked()
            elif choice == "l":
                choose()
            elif choice=="x":
                exit()              #exit the program

             #if choice entered is wrong then print
        else:
            print(colored("You have entered a wrong choice !Try Again",'red'))

StartBot()
#sandbox user
#amitrawat5188	admin
#raj_2802
#manirajyadav
#rvt_surbhi