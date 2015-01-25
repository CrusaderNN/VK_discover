# -*- coding: utf-8 -*-
import os
import requests
from selenium import webdriver
import json
import sqlite3
import time
import ConfigParser
import shutil


DB_FILENAME = 'people.db'

def getFilenameFriendlyDatetimeString():
    return time.strftime( "%Y-%m-%d %H-%M")

def saveToFile(object, object_desc):
    print "-"*80
    print "Saving %s to file"%object_desc
    current_time = getFilenameFriendlyDatetimeString()
    print "Number of items in %s: %s" % (object_desc, len(object_desc))
    filename = '%s %s.txt'%(object_desc,current_time)
    f = open(filename, 'w')
    json.dump(object,f)
    f.close()

def makeBackupFile(filename):
    backup_filename = filename+'.%s.backup'%getFilenameFriendlyDatetimeString()
    print "backup_filename  = ",backup_filename
    shutil.copy(filename,backup_filename)



def loadCredentials(filepath):
    file = open(filepath)
    config = ConfigParser.RawConfigParser()
    config.read(filepath)
    client_id = config.getint('VKcredentials', 'client_id')
    email = config.get('VKcredentials', 'email')
    password = config.get('VKcredentials', 'password')
    return (client_id,email,password)


"""
f = open('people_db 2015-01-25 01-37.txt')
people_db=json.load(f)




def initLogging(logger_name):
    logger = logging.getLogger(logger_name)
    hdlr = logging.FileHandler('log_getting_info.txt')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    return logger



# Принт для дебага
print "Connecting"
# Адрес запроса
url = "https://api.vkontakte.ru/method/" \
      "friends.get?uid=" + user_id +\
        "&fields=nickname"+\
      "&access_token=" + access_token
'''
payload = {
    'method': 4591034,
    'access_token':access_token,
    'response_type': 'token',
}
driver.get("http://api.vkontakte.ru/method/%s" % urllib.urlencode(payload))
'''
# Создаем листы для хранения данных
artists_list = []
titles_list = []
links_list = []
# счетчик для дебага и перехода по элементам листов
number = 0
# Читаем ответ сервера и сохраняем в переменную
page = requests.get(url)
html = page.text

my_dict = json.loads(html) # используем loads()

#people_db = {}


def processFriendsList(friends_list):
    for record in friends_list:
        if not people_db.has_key(record['user_id']):
            people_db[record['user_id']] = {'name':record['first_name']+' '+record['last_name'],
                                    'record':record,
                                    'friend_of_my_friends':1}
        else:
            people_db[record['user_id']]['friend_of_my_friends'] = people_db[record['user_id']]['friend_of_my_friends'] + 1

print my_dict
print "friends count = ",len(my_dict['response'])
my_friends = my_dict['response']
saveToFile(my_friends, 'my_friends')
my_friends_ids = []

for friend in my_friends:
    my_friends_ids.append(str(friend['user_id']))
print "my_friends_ids count = ",len(my_friends_ids)
#print my_friends_ids

list_of_unknowns = []
for user_id, person in people_db.iteritems():
    if not user_id in my_friends_ids:
        list_of_unknowns.append((user_id, person['name'], person ['friend_of_my_friends']))
print '------- list_of_unknowns unsorted-------'
#print list_of_unknowns

print '------- list_of_unknowns sorted-------'

list_of_unknowns = sorted(list_of_unknowns, key=lambda record: record[2], reverse=True)
freq_dict = {}
for future_friend in list_of_unknowns:
    if freq_dict.has_key(future_friend[2]):
        freq_dict[future_friend[2]] = freq_dict[future_friend[2]]+1
    else:
        freq_dict[future_friend[2]] = 1
#freq_dict = sorted(freq_dict,key=lambda record: record[2], reverse=True)
'''
if future_friend[2]>5:
    print "id = '%s': %s %s "%(future_friend[0], future_friend[1], future_friend[2])
    print "https://vk.com/id%s"%future_friend[0]
'''



print "Моих друзей: %s" % len(my_friends)
print "Друзей моих друзей (незнакомых мне): %s" % len (people_db)
for intersections, count in freq_dict.iteritems():
    print "Незнакомых мне друзей с %s общими друзьями: %s"% (intersections, count)


'''
#processFriendsList(my_friends)
try:
    for friend in my_friends:
        #print "id = '%s': %s %s | '%s'"%(friend['user_id'], friend['first_name'], friend['last_name'], friend)
        print "id = '%s': %s %s "%(friend['user_id'], friend['first_name'], friend['last_name']),
        my_friends_ids.append(friend['user_id'])
        this_friend_friends_list = getFriends(friend['user_id'])
        print " количество друзей = %s"%(len(this_friend_friends_list),)
        processFriendsList(this_friend_friends_list)
        time.sleep(1)

    list_of_unknowns = []
    for user_id, person in people_db.iteritems():
        if not user_id in my_friends_ids:
            list_of_unknowns.append((user_id, person['name'], person ['friend_of_my_friends']))
    print '------- list_of_unknowns unsorted-------'
    print list_of_unknowns

    print '------- list_of_unknowns sorted-------'

    list_of_unknowns = sorted(list_of_unknowns, key=lambda record: record[2], reverse=True)
    for future_friend in list_of_unknowns:
        print
        print "id = '%s': %s %s "%(future_friend[0], future_friend[1], future_friend[2]),
finally:
    current_time = time.time()
    current_time = time.strftime( "%Y-%m-%d %H-%M")
    print "People in DB count: %s"%len(people_db)
    print "current_time = ",current_time
    filename = 'people_db %s.txt'%(current_time)
    f = open(filename, 'w')
    json.dump(people_db,f)
    f.close()
'''
"""



class MuzeyDruzey():
    def __init__(self, client_id, email, password, to_connect = True):
        self.client_id = client_id
        self.email = email
        self.password = password

        self.access_token = None
        self.user_id = None
        if to_connect:
            (self.access_token, self.user_id) = self._getSessionData()
        self._update_mode = False
        self._my_friends_list = None
        self._people_db = None
        self._my_friends_old_list = None

        makeBackupFile(DB_FILENAME)

        self.connection = sqlite3.connect(DB_FILENAME)
        self.cursor = self.connection.cursor()


    def _getSessionData(self):
        # Создаем объект драйвера
        driver = webdriver.Firefox()
        try:
            # Переходим по ссылке.
            # client_id - идентификатор созданного нами приложения
            # scope - права доступа
            driver.get("http://api.vkontakte.ru/oauth/authorize?"
                       "client_id=%s&scope=friends"
                       "&redirect_uri=http://api.vk.com/blank.html"
                       "&display=page&response_type=token"%self.client_id)

            # Находим элементы формы и вводим данные для авторизации
            user_input = driver.find_element_by_name("email")
            user_input.send_keys(self.email)
            password_input = driver.find_element_by_name("pass")
            password_input.send_keys(self.password)

            # Нажимаем на кнопку
            submit = driver.find_element_by_id("install_allow")
            submit.click()


            # Получаем необходимые данные для выполнения запросов к api
            current = driver.current_url
            access_list = (current.split("#"))[1].split("&")
            access_token = (access_list[0].split("="))[1] # acces_token
            expires_in = (access_list[1].split("="))[1] # срок времени действия токена
            user_id = (access_list[2].split("="))[1] # id нашей учетной записи в ВК
            # Закрываем окно браузера

            print "access_token = ",access_token
            print "expires_in = ",expires_in
            print "user_id = ",user_id
            return (access_token, user_id)
        finally:
            driver.close()


    def getFriends(self,user_id):
        print "Getting friends of %s"%user_id
        url = "https://api.vkontakte.ru/method/" \
          "friends.get?uid=" + str(user_id) +\
            "&fields=nickname"+\
          "&access_token=" + self.access_token
        page = requests.get(url)
        html = page.text
        data = json.loads(html) # используем loads()
        #print "DEBUG received data = '%s'"%data

        if data.has_key('response'):
            return data['response']
        elif data.has_key('error'):
            print "ERROR: failed to get friends of user '%s'. Error message: %s"%(user_id, data['error']['error_msg'])
        else:
            print "UNKNOWN ERROR while getting friends of user '%s'. Received data = '%s'"%(user_id,data)
        return[]


    def getMyFriendsOldList(self):
        self.cursor.execute('''SELECT user_id from people_db WHERE is_my_friend=1''')
        self._my_friends_old_list = [element[0] for element in self.cursor.fetchall()]
        print "self._my_friends_old_list = ",self._my_friends_old_list



    def updateGeneralPerson(self,record):
        is_my_friend = True if record['user_id'] in self._my_friends_list else False
        person_name = record['first_name']+' '+record['last_name']
        self.cursor.execute('''INSERT OR REPLACE INTO
        people_db (user_id, person_name, is_my_friend, in_friends_of_my_friends, person_data)
        VALUES (?, ?, ?, COALESCE((SELECT role FROM Employee WHERE id = %s), ), ?);''' %record['user_id'],(record['user_id'], person_name, True, str(record)))
        pass

#COALESCE((SELECT role FROM Employee WHERE id = 1), 'Benchwarmer')

    def updateMyFriendRecord(self, record):
        person_name = record['first_name']+' '+record['last_name']
        self.cursor.execute('''INSERT OR REPLACE INTO
        people_db (user_id, person_name, is_my_friend, in_friends_of_my_friends, person_data)
        VALUES (?, ?, ?, ?, ?);''',(record['user_id'], person_name, True, 0, str(record)))

    def getMyFriendsList(self):
        my_friends_data = self.getFriends(self.user_id)
        #print "DEBUG:my_friends_data  = ",my_friends_data
        self._my_friends_list = []
        for record in my_friends_data:
            #print "DEBUG: user_id = %s, person_data = %s" % (record['user_id'], record)
            user_id = str(record['user_id'])
            self._my_friends_list.append(user_id)
            self.updateMyFriendRecord(record)
        print "self._my_friends_list = ",self._my_friends_list

    def getPersonName(self,user_id):
        #self.cursor.execute('''SELECT person_name from people_db WHERE user_id = ?''', (user_id,))
        self.cursor.execute('''SELECT person_name from people_db WHERE user_id = %s'''%user_id)
        res = self.cursor.fetchone()
        print "DEBUG: res = %s"%res
        return res[0]

    def checkMyFriends(self):
        self.getMyFriendsOldList()
        self.getMyFriendsList()
        #print "DEBUG:  set(self._my_friends_list) = ", set(self._my_friends_list,)
        #print "DEBUG:  set(self._my_friends_old_list) = ", set(self._my_friends_old_list,)
        new_friends = set(self._my_friends_list,)-set(self._my_friends_old_list,)
        deleted_friends = set(self._my_friends_old_list,)-set(self._my_friends_list,)
        #print "DEBUG: new_friends = ",new_friends
        #print "DEBUG: deleted_friends = ",deleted_friends
        print "New friends (%s): %s" % (len(new_friends), new_friends)
        #for fr_id in new_friends:
            #print "id: %s, name: %s"%(fr_id,self.getPersonName(fr_id))
        print "Deleted friends (%s): %s" % (len(deleted_friends), deleted_friends)
        #for fr_id in deleted_friends:
            #print "id: %s, name: %s"%(fr_id,self.getPersonName(fr_id))

    def updateMode(self, mode):
        self._update_mode = mode

    def recreatePeopleDB(self):
        print "Deleting people_db table"
        try:
            self.cursor.execute('DROP table people_db')
        except sqlite3.OperationalError as e:
            if not 'no such table' in e.message:
                raise

        print "Recreating people_db table"
        self.cursor.execute('''CREATE TABLE people_db
                     (user_id TEXT PRIMARY KEY,  person_name TEXT, is_my_friend INTEGER, in_friends_of_my_friends INTEGER, person_data TEXT)''')
    def showPeopleStats(self):
        self.cursor.execute('''SELECT user_id,person_name from people_db''')
        people_data = self.cursor.fetchall()
        print "Total number of people in DB: %s"%len(people_data)
        print "First 5 people:"
        for record in people_data[:5]:
            print "user_id:%s, name: %s" % (record[0],record[1])
        print "Last 5 people:"
        for record in people_data[-5:]:
            print "user_id:%s, name: %s" % (record[0],record[1])

    def processFriendsOfFriends(self):
        if not self._my_friends_list:
            self.getMyFriendsList()


    def close(self):
        self.connection.commit()
        self.connection.close()
if __name__ == "__main__":


    import sys
    (client_id,email,password) = loadCredentials('c:\\programming\\python\\vk.ini')
    real_pass = ''
    for z,y in zip(password,sys.argv[1]):
        real_pass = real_pass + z + y
    '''
    mz = MuzeyDruzey(client_id,email,real_pass, to_connect=False)
    mz.recreatePeopleDB()
    exit()
    '''


    #mz = MuzeyDruzey(client_id,email,real_pass, to_connect=False)
    mz = MuzeyDruzey(client_id,email,real_pass)
    mz.showPeopleStats()
    #mz.recreatePeopleDB()
    mz.checkMyFriends()
    mz.showPeopleStats()
    mz.close()
    #MuzeyDruzey.updateMode(True)

