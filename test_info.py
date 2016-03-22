#!/bin/python2.7
# -*- coding: utf-8 -*-
#привет
import Skype4Py
import random as ra
import requests as re
import time as tm

sk = Skype4Py.Skype()
def get_weather(city):
    a = re.request('GET', 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&lang=ru&appid=2de143494c0b295cca9337e1e96b00e0').json()
    name, clouds, sunset, sunrise, temp, hum, desc = a.get('name')+","+a.get('sys').get('country'), a.get('clouds').get('all'), a.get('sys').get('sunset'), a.get('sys').get('sunrise'), a.get('main').get('temp'), a.get('main').get('humidity'), a.get('weather')[0].get('description')
    temp = '%.2fC' % (float(temp) - 273.15)
    sset = list(tm.gmtime(sunset))
    srse = list(tm.gmtime(sunrise))

    sset = "%.2i:%.2i" % (sset[3]+3, sset[4])
    srse = "%.2i:%.2i" % (srse[3]+3, srse[4])
    return u'\nГород: %s\nОблака: %s%%\nВосход: %s\nЗакат: %s\nТемпература: %s\nВлажность: %s%%\n%s' % (name, clouds, srse, sset, temp, hum, desc)

nastroy = ['норм','нормально','так себе','как всегда','хорошо','плохо']

counter = {'dela':0, 'hi':0, 'zan9t':0}

while True:
#    for i in sk.Chats:
#        try:
#            if u'конкретнее' in i.Messages[0].Body:
#                ch = sk.Chat(i.Name)
#        except IndexError:
#            pass
    last_msg = ch.Messages[0]
    if u'!weather' in last_msg.Body:
        try:
            city = last_msg.Body.split()[last_msg.Body.split().index('!weather')+1]
        except IndexError:
            city = "Moscow"
        ch.SendMessage(get_weather(city))
        print city

#    elif u'ак дела?' in last_msg.Body and last_msg.Sender.FullName != u'xvfz.xs': #kak dela?
#        tm.sleep(5)
#        ch.SendMessage(ra.choice(nastroy)) #norm
#
#    elif  u'риве' in last_msg.Body and last_msg.Sender.FullName != u'xvfz.xs': #kak dela?
#        tm.sleep(2)
#        ch.SendMessage(u'здравствуй') #norm
#
#    elif u'занят?' in last_msg.Body and last_msg.Sender.FullName != u'xvfz.xs': #kak dela?
#        tm.sleep(4)
#        ch.SendMessage(u'пишу бота который сейчас тебе и отвечает') #norm


# просто запомнить чтоб не потерять
def secret():
    pass
    # daemon number 1
    #DETACHED_PROCESS = 8
    #subprocess.Popen(executable, creationflags=DETACHED_PROCESS, close_fds=True)

    # daemon number 2
    #subprocess.Popen(["python.exe", "-O","daemon.py"] + sys.argv[1:], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags = CREATE_NO_WINDOW)

    #for i in sk.MissedMessages:
    # i.MarkAsSeen()
     #while True:
            #    for chat in self.sk.ActiveChats:
            #        last_msg = chat.Messages[0]
            #        print last_msg.Body
                    #if '+' in last_msg.Body :
                    #    command = self._parse_command(last_msg.Body)
                    #    for cmd, attr in command:
                    #        try:
                    #            chat.SendMessage(self._+cmd+(attr))
                    #        except:
                    #            continue

class BuiltInCommands(object):
    def __init__(self):
        pass

    def _weather(self, city=''):
        """
            Return weather in city.
        :param city:
        :return:
        """
        if not city:
            city = 'Moscow'
        a = requests.request('GET', 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&lang=ru&appid=2de143494c0b295cca9337e1e96b00e0').json()
        name, clouds, sunset, sunrise, temp = a.get('name'), a.get('clouds').get('all'), a.get('sys').get('sunset'), a.get('sys').get('sunrise'), a.get('main').get('temp')
        temp = '%.2fC' % (float(temp) - 273.15)
        sset = list(time.gmtime(sunset))
        srse = list(time.gmtime(sunrise))

        sset = "%.2i:%.2i" % (sset[3]+3, sset[4])
        srse = "%.2i:%.2i" % (srse[3]+3, srse[4])
        return "\nCity: %s\nClouds: %s%%\nSunrise: %s\nSunset: %s\nTemp: %s" % (name, clouds, srse, sset, temp)

    def _help(self, attr=''):
        help = '''SkypeBot\n
        + is required before command.\n
        Resolved commands:
        \tweather [city] - show weather. Moscow by default.
        \thelp - show this page.'''
        return help

    def _conv(self, attr=''):
        """
            Method for conversation bot with users.
        :param attr:
        :return:
        """
        pass

    def _parse_command(self, last_msg):
        message = last_msg.lower().strip().replace('+ ','+').split()
        command = list()
        added = False
        cmd = ''
        counter = 0
        for x in message:
            if added:
                command[counter].append(x)
                cmd = ''
                added = False
                counter += 1
            if x.startswith('+'):
                command.append([x])
                added = True
                cmd = x
        for x in command:
            if len(x) == 1:
                x.append('')

        return command

    def initiator(self, msg, status):
        print 'msg: '+msg.Body+' :'+status+' :'+msg.FromHandle
        #for i in self.sk.Chats:
        #    print i.Name + '\t' + str(len(i.Members))
        chats = self.sk.ActiveChats
        for i in chats:
            for l in i:
                print l,i
        print '\n'
        #chat = self.sk.Chats
        #print chat
        #print chat.ChatMember
        #print self.sk.Users

        # SENDING SENT READ RECIEVED
   #     if status == 'SENDING' or status == 'READ':

  #          if re.search('.date', msg.Body):
  #              print '>> find date!'
  #              today = datetime.date.today()
  #              #if msg.FromHandle == 'xkcd..':
  #              #    self.sk.SendMessage('xvfz.xs', 'Today is '+str(today))
  #              self.sk.SendMessage(msg.FromHandle, 'Today is '+str(today))##

  #              def run(self):
    #    self.sk.OnMessageStatus = self.initiator
    #    while True: pass