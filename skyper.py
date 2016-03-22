# coding: utf-8
__author__ = 'Dmitry Kryukov'
__email__ = "remasik@gmail.com"

"""
    Windows version of skype bot.
    Imitate of developer.
"""

import time
import sys
import subprocess
import random
import json
import Queue
import datetime
import requests
import Skype4Py
import re
import lxml.html
import lxml.etree


class BuiltInCommands(object):
    def __init__(self):
        self.commands = {
                        'ping': self._ping,
                        'topicappend': self._topicAppend,
                        'advice': self._advice,
                        'adv': self._advice,
                        'resolve': self._resolve,
                        'ball': self._8ball,
                        'define': self._define,
                        'google': self._google,
                        'commands': self._commands,
                        'geo': self._geo,
                        'spam': self._spam,
                        'cmds': self._commands
        }

    def _ping(self, message):
        message.Chat.SendMessage('/me pong')

    def _topicAppend(self, message):
        messageText = message.Body.split()[1:]
        message.Chat.SendMessage('/topic %s | %s' % (message.Chat.Topic, ' '.join(messageText)))

    def _advice(self, message):
        resp = requests.get('http://fucking-great-advice.ru/api/random')
        r = resp.json()['text']
        message.Chat.SendMessage('/me %s' % r)

    def _resolve(self, message):
                ips = message.Body.split('resolve')
                ip = ips[1].strip()
                resp = requests.get('http://api.predator.wtf/resolver/?arguments='+ip)
                message.Chat.SendMessage("Latest IP for the user ["+ip+"].")
                time.sleep(2)
                message.Chat.SendMessage('%s' % resp.text)

    def _8ball(self, message):
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
                  "Very doubtful"
                ]
        time.sleep(2)
        message.Chat.SendMessage('/me '+Choice[random.randint(0,11)])

    def _define(self, message):
        urban = message.Body.split('define')
        word = urban[1].strip()
        resp  = requests.get('http://api.urbandictionary.com/v0/define?term='+word)
        r = resp.text
        data = json.loads(r)
        print data
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

    def _google(self, message):
        splitMessage = message.Body.split(' ',1)
        messageText = splitMessage[1]
        message.Chat.SendMessage("/me http://lmgtfy.com/?q="+messageText)

    def _commands(self, message):
        message.Chat.SendMessage('/me Commands: %s' % self.commands.keys())

    def _geo(self, message):
        ips = message.Body.split('geo')
        ip = ips[1].strip()
        resp = requests.get("http://api.predator.wtf/geoip/?arguments="+ip)
        message.Chat.SendMessage('/me '+resp)

    def _spam(self, message):
        while True:
            try:
                message.Chat.SendMessage('Insult')
            except Exception, e:
                message.Chat.SendMessage('spam')
            else:
                message.Chat.SendMessage('Insult Insult Insult')


class Skyper(BuiltInCommands):
    def __init__(self):
        super(Skyper, self).__init__()
        self.sk = Skype4Py.Skype(Events=self)
        self.sk.Attach()

    def AttachmentStatus(self, status):
        if status == Skype4Py.apiAttachAvailable:
            self.sk.attach()

    def MessageStatus(self, message, status):
        if status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent:
            splitMessage = message.Body.split()
            print splitMessage
            for command, function in self.commands.items():
                if command in splitMessage[0]:
                    function(message)
                    break


    def run(self):
        art = """

          ▄▄▄                   ▄▄▄▄▄▄▄
        █▀░▀█           ▄▀▀▀░░░░░░░▀▀▄▄
        █░░░░█     ▄▀░░░░░░░░░░░░░░░▀▄            ▄▄▄
        █▄░░░▀▄▄▀░░██░░░░░░░░░░░░░░▀█       █▀▀░█
         █░░░░█▀░░░▀░░░░░░░░██░░░░░░▀█ ▄█░░░░█
          ▀█░░▄█░░░░░░░▄▄▄░░░░▀░░░░░░░███░░░░█▀
            █▄░█░░░░░▄███████▄░░░░░░░░░█▀░░░░▄▀
            ▀█░█░░░░▄██████████░░░░░░░▄█░░░░▄▀
            ███░░░░███████████░░░░░░▄█░░░░█▀
               █░░░░░██████████▀░░░░░░█░░░░█▀
               █░░░░░░▀███████▀░░░░░░░█▄▄▄▀
               █░░░░░░░░▀▀▀▀░░░░░░░░░░░▀█
               █░░░░░░░░░░░░░░░░░░░░░░░░█
               █░░░░░░░░░░░░░░░░░░░░░░░░█
               █░░░░░░░░░░░░░░░░░░░░░░░░█

        """
        while True:
            print art
            print '\t\t\t\t\tHello, this is Skyper bot.'
            raw_input()


bot = Skyper()
bot.run()
