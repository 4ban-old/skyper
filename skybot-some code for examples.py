# coding: utf-8
__author__ = 'Dmitry Kryukov'
__email__ = "remasik@gmail.com"

import Skype4Py
import re
import urllib
import getpass
import urllib2
import xml
from sgmllib import SGMLParser
import time
import json
import random
import sys, os
import codecs
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
def getHandle():
    return getAPI().CurrentUser.Handle
def getBetween(strSource, strStart,strEnd):
        start = strSource.find(strStart) + len(strStart)
        end = strSource.find(strEnd,start)
        return strSource[start:end]

class SkypeBot:
        def __init__(self):
                self.skype = Skype4Py.Skype(Events=self)
                self.skype.Attach()

        def AttachmentStatus(self, status):
                if status == Skype4Py.apiAttachAvailable:
                        self.skype.attach()
        def MessageStatus(self, message, status):
                if status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent:
                        splitMessage = message.Body.split()
                        print splitMessage
                        for command, function in self.commands.items():
                                if command in splitMessage[0]:
                                        function(self, message)
                                        break
        def commandJoke(self, message):
                shitt = urllib2.urlopen('http://www.jokesclean.com/OneLiner/Random/').read()
                shit = getBetween(shitt,'<p class="c"> <font size="+2">',"</font></p>")
                message.Chat.SendMessage(strip_tags('/me'+shit))
        def commandFml(self,message):
                tit = urllib2.urlopen('http://m.fmylife.com/random').read()
                fml = getBetween(tit,'<p class="text">','</p>')
                message.Chat.SendMessage(strip_tags('/me '+fml))
        def commandFml(self,message):
                dataa = urllib2.urlopen('http://m.fmylife.com/random').read()
                fml = getBetween(dataa,'<p class="text">','</p>')
                message.Chat.SendMessage(strip_tags('/me '+fml))
        def commandUrban(self, message):
                urban = message.Body.split('define')
                word = urban[1].strip()
                r  = urllib2.urlopen('http://api.urbandictionary.com/v0/define?term=' + word)
                data = json.loads(r.read())
                if ( len(data['list']) > 1 ):
                      data['list'] = data['list'][:1]  # only print 2 results
                      for i in range(len(data['list'])):
                        word = data['list'][i][u'word']
                        definition = data['list'][i][u'definition']
                        example = data['list'][i][u'example']
                        permalink = data['list'][i][u'permalink']
                        message.Chat.SendMessage('/me '+word+': ' + definition),
                        message.Chat.SendMessage('/me Example: ' + example)
                else:
                      print 'Word not found.'

        def command8ball(self, message):
                        splitMessage = message.Body.split(' ',1)
                        messageText = splitMessage[1]
                        Choice = ["It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"]
                        time.sleep(2)
                        message.Chat.SendMessage('/me '+Choice[random.randint(0,11)])
        def commandTube(self, message):
                        global Finder
                        global Finder2
                        splitMessage = message.Body.split(' ',1)
                        Finder = message.Body.split(' ',5)
                        Finder2 = message.Body.split(' ',5)
                        messageText = splitMessage[1]
                        SplitSearch = splitMessage[1].replace(' ','+')
                        URL = urllib2.urlopen('http://www.youtube.com/results?q='+SplitSearch).read()
                        String = re.findall(r'\/watch\?v=\w{11}',URL)
                        Array = []
                        for x in String:
                                if x in Array:
                                        pass
                                else:
                                        Array.append(x)
                        #print Array
                        message.Chat.SendMessage('/me Searching (3) Results for: '+messageText)
                        for i in Array[0:3]:
                                time.sleep(2)
                                message.Chat.SendMessage('/me http://youtube.com'+i)
        def commandPing(self, message):
                message.Chat.SendMessage('/me pong')
        def commandDice(self, message):
                message.Chat.SendMessage('/me Put a bet on numbers 1 through 6.')
                time.sleep(8)
                rolled = random.randint(1,6)
                message.Chat.SendMessage('/me *rolls dice*')
                time.sleep(1)
                message.Chat.SendMessage('/me The dice rolled the number:')
                rolled = str(rolled)
                message.Chat.SendMessage("/me "+rolled)
        def commandSay(self, message):
                splitMessage = message.Body.split(' ',1)
                messageText = splitMessage[1]
                message.Chat.SendMessage('/me '+messageText)
        def commandGoogle(self, message):
                splitMessage = message.Body.split(' ',1)
                messageText = splitMessage[1]
                message.Chat.SendMessage("/me http://lmgtfy.com/?q="+messageText)
        def commandResolve(self, message):
                ips = message.Body.split('resolve')
                ip = ips[1].strip()
                response = urllib2.urlopen("http://api.predator.wtf/resolver/?arguments=" + ip).read()
                message.Chat.SendMessage("/me Grabbing Latest IP for the user ["+ip+"].")
                time.sleep(2)
                message.Chat.SendMessage('/me %s' % response)
        def commandWebres(self, message):
                ips = message.Body.split('webresolve')
                ip = ips[1].strip()
                response = urllib2.urlopen("http://api.predator.wtf/cfwresolve/?arguments=" + ip).read()
                message.Chat.SendMessage("/me Grabbing the IP for the website ["+ip+"].")
                time.sleep(2)
                message.Chat.SendMessage('/me %s' % response)
        def commandPwgen(self, message):
                ips = message.Body.split('pwgen')
                ip = ips[1].strip()
                response = urllib2.urlopen("http://api.predator.wtf/passgen/?arguments=" + ip).read()
                message.Chat.SendMessage("/me Generating Password ["+ip+"] charactors long.")
                time.sleep(2)
                message.Chat.SendMessage('/me %s' % response)
        def commandSlap(self, message):
                ips = message.Body.split('slap')
                ip = ips[1].strip()
                message.Chat.SendMessage("/me has slapped "+ip+"'s ass. ;)")
        def commandKiss(self, message):
                ips = message.Body.split('kiss')
                ip = ips[1].strip()
                message.Chat.SendMessage("/me has given "+ip+" a big fat kiss :*")
        def commandTopicAppend(self, message):
                messageSplit = message.Body.split()[1:]
                message.Chat.SendMessage('/topic %s | %s' % (message.Chat.Topic, ' '.join(messageSplit)))
        def commandCommands(self, message):
                message.Chat.SendMessage('/me Commands: http://maiestas.org/Plexus/commands.txt')
        def commandGeo(self, message):
                ips = message.Body.split('geo')
                ip = ips[1].strip()
                response = urllib2.urlopen("http://api.predator.wtf/geoip/?arguments=" + ip).read()
                message.Chat.SendMessage("/me Generating data on the IP ["+ip+"].")
                time.sleep(2)
                message.Chat.SendMessage(strip_tags('/me '+response))
        def commandIpHost(self, message):
                ips = message.Body.split('ip2host')
                ip = ips[1].strip()
                response = urllib2.urlopen("http://api.predator.wtf/ip2host/?arguments=" + ip).read()
                message.Chat.SendMessage("/me Generating data on the IP ["+ip+"].")
                time.sleep(2)
                message.Chat.SendMessage('/me '+response)
        def commandIpSkype(self, message):
                ips = message.Body.split('ip2skype')
                ip = ips[1].strip()
                response = urllib2.urlopen("http://api.predator.wtf/lookup/?arguments=" + ip).read()
                message.Chat.SendMessage("/me Generating data on the IP ["+ip+"].")
                time.sleep(2)
                message.Chat.SendMessage('/me '+response)
        def commandInsult(self, message):
                while 1:
                    try:
                     message.Chat.SendMessage('this groupchat is cancer')
                    except Exception,e:
                     message.Chat.SendMessage('spam')
                    else:
                     message.Chat.SendMessage('skype4py ftw spam spam spam')

        commands = {
                '!ping': commandPing,
                '!topicappend': commandTopicAppend,
                '!joke': commandJoke,
                '!dice': commandDice,
                '!say': commandSay,
                '!resolve': commandResolve,
                '!tube': commandTube,
                '!8ball':command8ball,
                '!define': commandUrban,
                '!google': commandGoogle,
                '!commands': commandCommands,
                '!pwgen': commandPwgen,
                '!ip2skype': commandIpSkype,
                '!fml': commandFml,
                '!slap': commandSlap,
                '!kiss': commandKiss,
                '!webresolve': commandWebres,
                '!geo': commandGeo,
                '!spam': commandInsult,
                '!cmds': commandCommands
        }

if __name__ == '__main__':
        bot = SkypeBot()

while True:
                print('             __________.__                               ')
                print('             \______   \  |Plexus Skype Bot      ______')
                print('              |     ___/  | _/ __ \   \/  /  |  \/  ___/')
                print('              |    |   |  |_\  ___/ >    <|  |  /\___ \ ')
                print('              |____|   |____/\___  >__/\_ \____//____  >')
                print('                                 \/      \/          \/ ')
                skype = Skype4Py.Skype();
                print '               User Running PlexusBot:',skype.CurrentUserHandle, "\n"
                print('               You are a [ Platinum ] User       ')

                raw_input()