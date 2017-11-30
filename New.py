# -*- coding: utf-8 -*-

import TOBY
import requests,json,urllib,tempfile
from TOBY.lib.curve.ttypes import *
from datetime import datetime
from gtts import gTTS
from urllib import urlopen
import time,random,sys,json,codecs,threading,glob,re
import os.path,sys,urllib,shutil,subprocess

cl = TOBY.LINE()
cl.login(token="EnUJv8nS7V8m1YSpE2hd.rQI3sHKUFOJycabz4N2cBq.lZEhzy6OVQXkcP9AwgHQuPEVyL8MvRYQ2jO6vAJqeIw=")
cl.loginResult()

ki = TOBY.LINE()
ki.login(token="Emg9hyEg1xLqtJiBm7j9.2SozhwGBFV9FQbKJq2aRAq.B3k4nN2xTh33wOidJQU9Rix3x/JCDB2h7EOjiCo603E=")
ki.loginResult()

kk = TOBY.LINE()
kk.login(token="EmjyWR5ZvhjxMPH949N6.ryL8meN5fHOxOBvDACRubG.F7lCrllrp2Fk75thepVhE7WG4xeFC8QRwQY1nbfYvFw=")
kk.loginResult()

kc = TOBY.LINE()
kc.login(token="EmLEz2PJCLPcNeYL9Mud.pgyoXnuZmwEdeTR5IqrUVq.rSKWKEGsatlAYhT6wi/mioyxElup7k58KditcfQd48k=")
kc.loginResult()

kd = TOBY.LINE()
kd.login(token="EmyHrw1vesKO9VqNcn4e.66Kq6+c33PXN2dKNS6xQ+G.wXNGDbZoVcWY4BvVpE7gQ9E0VI0UNTsnqCJ4/f+q+Qs=")
kd.loginResult()

ka = TOBY.LINE()
ka.login(token="EnF4YxoB2RsGYgc5x9Ta.N+zTfHuEXFaQ5DKCS+Wx2G.fQEnZBR295Fh0xA9AqgM0Y3kjMVsLoyM2b+MG6Nvd4I=")
ka.loginResult()

ke = TOBY.LINE()
ke.login(token="EnBBD6ENmcS62nTg0mw1.3UuOSO3/Lhqll3bytJB9Sq.3fHvRbQ7jo2hi8psFC2Q/cKsA5LMc+uf+LlCo8r76e0=")
ke.loginResult()

# client_id = ''
# client_secret = ''
# access_token = ''
# refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

# album = None
# image_path = 'tmp/tmp.jpg'

helpMessage ="""

=====C͓̽o͓̽m͓̽m͓̽a͓̽n͓̽d͓̽ C͓̽r͓̽e͓̽a͓̽t͓̽o͓̽r͓̽=====

•ᴀʟʟʙɪᴏ: •/ɴᴀᴍᴀʙᴏᴛᴄʜᴀɴɢᴇɴᴀᴍᴇ:
•ʙᴏᴛ:ʀᴇsᴛᴀʀᴛ [ʀᴇsᴛᴀʀᴛ ʙᴏᴛs]
•ᴄʙᴄ [ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏɴᴛᴀᴄᴛ]
•ᴍᴀʏʜᴇᴍ [ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀ]
•ᴀᴅᴍᴀᴅᴅ @ [ᴀᴅᴅ ɴᴇᴡ ᴀᴅᴍɪɴ]
•ᴀᴅᴍʀᴇᴍ @ [ᴅᴇʟʟᴇᴛᴇ ᴀᴅᴍɪɴ]

=====A͓̽d͓̽m͓̽i͓̽n͓̽ C͓̽o͓̽m͓̽m͓̽a͓̽nd͓͓̽̽=====

•sᴇᴛ [sʜᴏᴡ sᴇᴛᴛɪɴɢ ʙᴏᴛs]
•ʙʏᴇ @ [ᴋɪᴄᴋ 2/10 ᴍᴇᴍʙᴇʀ]
•ᴠᴋ @ [ᴋɪᴄᴋ 1 ᴍᴇᴍʙᴇʀ]
•ɢᴜᴇsᴛ ᴏɴ/ᴏғғ [ʙʟᴏᴄᴋ ɪɴᴠɪᴛᴇ]
•ᴍᴀᴅ ᴏɴ/ᴏғғ[ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ]
•sᴘᴀᴍɢ ᴏɴ/ᴏғғ ᴊᴜᴍʟᴀʜ ᴋᴀᴛᴀ2
•ʙᴀɴ @ [ʙᴀɴɴᴇᴅ ʙʏ ᴛᴀɢ]
•ᴜɴʙᴀɴ @ [ᴜɴʙᴀɴ ʙʏ ᴛᴀɢ]
•ʙᴀɴ [ʙᴀɴ ʙʏ sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ]
•ᴜɴʙᴀɴ [ᴜɴʙᴀɴ ʙʏ sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ]
•ʙᴀɴʟɪsᴛ [sʜᴏᴡ ʙᴀɴɴᴇᴅ ʟɪsᴛ]
•ǫʀ ᴏɴ/ᴏғғ [ᴘʀᴏᴛᴇᴄᴛ ǫʀ]
•sᴘᴇᴇᴅ [sʜᴏᴡ sᴘᴇᴇᴅ ʙᴏᴛs]
•ʀᴇsᴘᴏɴ [sʜᴏᴡ ɴᴀᴍᴇ ʙᴏᴛs]
•ᴋɪʟʟ ʙᴀɴ [ᴋɪʟʟ ᴀʟʟ ʙᴀɴ ᴜsᴇʀ]
•ᴍɪᴍɪᴄ:ᴏɴ/ᴏғғ
•ᴍɪᴍɪᴄ:ᴀᴅᴅ:
•ᴍɪᴍɪᴄ:ᴅᴇʟ:
•ᴄᴏɴᴛᴀᴄᴛ @ [sʜᴏᴡ ᴄᴏɴᴛᴀᴄᴛ]
•ᴛᴀɢᴀʟʟ [ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs]
•ᴍᴀsᴜᴋ [ᴊᴏɪɴᴇᴅ ᴀʟʟ ʙᴏᴛs]
•ᴏᴜᴛ [ᴏᴜᴛ ᴀʟʟ ʙᴏᴛs]
•ᴏᴜʀʟ [ᴏᴘᴇɴ ᴜʀʟ ɢʀᴏᴜᴘs]
•ᴄᴜʀʟ [ᴄʟᴏsᴇ ᴜʀʟ ɢʀᴏᴜᴘs]
•ᴄᴀɴᴄᴇʟ [ᴄʟᴇᴀʀ ɪɴᴠɪᴛᴇs]
•ɢɪғᴛ [ʙᴏᴛs sᴇɴᴅ ɢɪғᴛ]
•ɢɴ [ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ɴᴀᴍᴇ]
•ᴍᴇ [sᴇɴᴅ ʏᴏᴜʀ ᴄᴏɴᴛᴀᴄᴛ]

=====P͓̽U͓̽B͓̽L͓̽I͓̽C͓̽ C͓̽O͓̽M͓̽M͓̽A͓̽N͓̽D͓̽=====

•ᴀᴘᴀᴋᴀʜ [ɪʏᴀ/ᴛɪᴅᴀᴋ]
•ᴄᴇᴋ ᴛᴀɴɢɢᴀʟᴀʜɪʀ-ʙᴜʟᴀɴ-ᴛᴀʜᴜɴ
•ᴄʀᴇᴀᴛᴏʀ [sʜᴏᴡ ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛ]
•ɢᴄʀᴇᴀᴛᴏʀ
•ɢɪɴғᴏ
•ʀᴇᴀᴅ ᴘᴏɪɴᴛ [sᴛᴀʀᴛ ᴄᴇᴋ sɪᴅᴇʀ]
•ᴄᴇᴋ sɪᴅᴇʀ [ᴄᴇᴋ ᴍᴇᴍʙᴇʀ sɪᴅᴇʀ]

====================
© ʙʏ ᴊᴜsᴛɪᴄᴇ ᴛᴇᴀᴍ ʙᴏᴛs
====================

"""
KAC=[cl,ki,kk,kc,kd]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Pmid = ka.getProfile().mid
Emid = ke.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Pmid,Emid]
admin=["ufa308a279f813fa5b17bf3bb2a56f403","u32e6d670aeab696b817073392ead18cb","ufaa1968b6ee9b15170ff74aab7379f43","u162e9820c437e180a8e6b77d08c6100e"]
creator=["ufa308a279f813fa5b17bf3bb2a56f403"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : line://ti/p/~syalifr17",
    "lang":"JP",
    "spam":{},
    "comment":"Owner : line://ti/p/~syalifr17",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "winvite":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":True,
    "ProtectQR":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)





def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "•" + Name
                wait2['ROM'][op.param1][op.param2] = "•" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G = ki.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("•",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
            if op.param2 not in Bots:
                group = random.choice(KAC).getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = random.choice(KAC).getContact(op.param2).displayName + " [NewMemb]\n\nSelamat Datang" + random.choice(KAC).getContact(op.param2).displayName + " di [" + group.name + "]\nJGN NAKAL OK!!" + "\n\nCreator => " + group.creator.displayName
                random.choice(KAC).sendMessage(cb)
        if op.type == 15:
            if op.param2 in Bots:
                return
            ki.sendText(op.param1, "Good Bye Kaka")
            print "MemberLeft"
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    kk.acceptGroupInvitation(op.param1)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    kc.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"

            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    kd.acceptGroupInvitation(op.param1)
                    print "BOT 5 Joined"
                else:
                    print "autoJoin is Off"

            if Pmid in op.param3:
                if wait["autoJoin"] == True:
                    ka.acceptGroupInvitation(op.param1)
                    print "BOT 6 Joined"
                else:
                    print "autoJoin is Off"

            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    ke.acceptGroupInvitation(op.param1)
                    print "BOT 7 Joined"
                else:
                    print "autoJoin is Off"


        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)


        if op.type == 19:
            if op.param3 in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,admin)
            else:
                pass

        if op.type == 19:
            if op.param2 not in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group�1�7�1�7\n["+op.param1+"]\n�1�7�1�7\n["+op.param2+"]\n�1�7�1�7�1�7�1�7�1�7�1�7�1�7��1�7�1�7�0�0�1�7�1�7�1�0�1�7�1�7�1�7�0�0�1�7�1�7�1�7�1�7�1�7\n�1�7�0�9�1�7�0�2�1�7�1�7�7�8�1�7�0�3�1�7�0�1�1�7�0�6�1�7�1�7�1�0�1�7�1�7�1�7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�1�7�1�7�1�7�1�7�1�7�1�7�0�0�1�7�1�7or�1�7�1�7�1�7�1�7`�1�7�0�2�0�4�1�7�1�7�1�4�1�7�1�7�0�9�1�7�1�7�\n["+op.param1+"]\n�1�7�1�7\n["+op.param2+"]\n�1�7�1�7�1�7�1�7�1�7�1�7�1�7��1�7�1�7�0�0�1�7�1�7�1�0�1�7�1�7�1�7�0�0�1�7�1�7�1�7�1�7�1�7\n�1�7�0�9�1�7�0�2�1�7�1�7�7�8�1�7�0�3�1�7�0�1�1�7�0�6�1�7�1�7�1�0�1�7�1�7�1�7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�1�7�1�7�1�7�1�7�1�7�1�7�0�0�1�7�1�7or�1�7�1�7�1�7�1�7`�1�7�0�2�0�4�1�7�1�7�1�4�1�7�1�7�0�9�1�7�1�7�\n["+op.param1+"]\n�1�7�1�7\n["+op.param2+"]\n�1�7�1�7�1�7�1�7�1�7�1�7�1�7��1�7�1�7�0�0�1�7�1�7�1�0�1�7�1�7�1�7�0�0�1�7�1�7�1�7�1�7�1�7\n�1�7�0�9�1�7�0�2�1�7�1�7�7�8�1�7�0�3�1�7�0�1�1�7�0�6�1�7�1�7�1�0�1�7�1�7�1�7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�1�7�1�7�1�7�1�7�1�7�1�7�0�0�1�7�1�7or�1�7�1�7�1�7�1�7`�1�7�0�2�0�4�1�7�1�7�1�4�1�7�1�7�0�9�1�7�1�7�\n["+op.param1+"]\n�1�7�1�7\n["+op.param2+"]\n�1�7�1�7�1�7�1�7�1�7�1�7�1�7��1�7�1�7�0�0�1�7�1�7�1�0�1�7�1�7�1�7�0�0�1�7�1�7�1�7�1�7�1�7\n�1�7�0�9�1�7�0�2�1�7�1�7�7�8�1�7�0�3�1�7�0�1�1�7�0�6�1�7�1�7�1�0�1�7�1�7�1�7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

        #------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
               cl.kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�1�70�1�79�1�76�1�79�1�7�1�7\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot1 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv1 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv2 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "Bot1 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "Bot2 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "Bot3 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif "Bot1 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 invite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "Bot2 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 invite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "Bot3 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 invite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': msg.from_}
                                        random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Bot1"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
            elif msg.text in ["Bot2"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Bot1 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Bot2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Bot3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"No one is inviting")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 curl","Bot1 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 curl","Bot2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 curl","Bot3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
                                        ke.sendText(msg.to,Emid)
                                        ka.sendText(msg.to,Pmid)
            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "Bot2 mid" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "Bot3 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Cury PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɢᴜᴇsᴛ sᴛʀᴀɴɢᴇʀ [ᴏɴ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɢᴜᴇsᴛ sᴛʀᴀɴɢᴇʀ [ᴏɴ]")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɢᴜᴇsᴛ sᴛʀᴀɴɢᴇʀ [ᴏғғ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɢᴜᴇsᴛ sᴛʀᴀɴɢᴇʀ [ᴏғғ]")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ1�7","K on","Contact on","é¡¯ç¤ºï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
						else:
							cl.sendText(msg.to,"ᴅᴏɴᴇ")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ�1�7�1�7","K off","Contact off","é¡¯ç¤ºï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ")
						else:
							cl.sendText(msg.to,"ᴅᴏɴᴇ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1�7��1�7�å�1�7�åń1�7 :ã‚ªãƒ1�7","Join on","Auto join:on","è‡ªå�1�7��1�7�åƒåń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ [ᴏɴ]")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ [ᴏɴ]")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1�7��1�7�å�1�7�åń1�7 :ã‚ªãƒ�1�7�1�7","Join off","Auto join:off","è‡ªå�1�7��1�7�åƒåń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"å…³äº�1�7�é�1�7�€è¯·æ‹�1�7�ç»ã€‚è¦æ�1�7�¶å¼€è¯·æŒ‡å®šäººæ�1�7�°å�1�7�é€")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš�1�7�å°ç»�1�7�ç�1�7�¨è�1�7�ªåŠ¨é�1�7�€è¯·æ‹�1�7�ç»1�7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ1�7","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ�1�7�1�7","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ�1�7�1�7:ã‚ªãƒ1�7","Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å…±æœ�1�7�1�7:ã‚ªãƒ�1�7�1�7","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif msg.text in ["Set"]:
				if msg.from_ in admin:
					md = "sᴇᴛᴛɪɴɢ ʙᴏᴛs\n\n"
					if wait["contact"] == True: md+=" ✅ᴄᴏɴᴛᴀᴄᴛ : on\n"
					else: md+=" ❌ᴄᴏɴᴛᴀᴄᴛ : off\n"
					if wait["autoJoin"] == True: md+=" ✅ᴀᴜᴛᴏ ᴊᴏɪɴ : on\n"
					else: md +=" ❌ᴀᴜᴛᴏ ᴊᴏɪɴ : off\n"
					if wait["autoCancel"]["on"] == True:md+=" ✅ɢʀᴏᴜᴘ ᴄᴀɴᴄᴇʟ :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= " ❌ɢʀᴏᴜᴘ ᴄᴀɴᴄᴇʟ : off\n"
					if wait["leaveRoom"] == True: md+=" ✅ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ : on\n"
					else: md+=" ❌ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ : off\n"
					if wait["timeline"] == True: md+=" ✅sʜᴀʀᴇ : on\n"
					else:md+=" ❌sʜᴀʀᴇ : off\n"
					if wait["autoAdd"] == True: md+=" ✅ᴀᴜᴛᴏ ᴀᴅᴅ : on\n"
					else:md+=" ❌ᴀᴜᴛᴏ ᴀᴅᴅ : off\n"
					if wait["commentOn"] == True: md+=" ✅ᴄᴏᴍᴍᴇɴᴛ : on\n"
					else:md+=" ❌ᴄᴏᴍᴍᴇɴᴛ : off\n"
					if wait["Protectcancel"] == True: md+="  ✅ᴍᴀᴅ : on\n"
					else:md+=" ❌ᴍᴀᴅ : off\n"
					if wait["Protectguest"] == True: md+=" ✅ɢᴜᴇsᴛ : on\n"
					else:md+=" ❌ɢᴜᴇsᴛ : off\n"
					cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1�7�äº�1�7�çš�1�7�ç�1�7�¸å�1�7�Œã€ 1�7")
            elif msg.text in ["Group id","ç¾¤çµ„å�1�7�¨id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"æ‹�1�7�ç»äº�1�7�å�1�7�¨éƒ¨çš�1�7�é�1�7�€è¯·ã€�1�7�1�7")
            elif "album removeâ†�1�7�1�7" in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album removeâ†�1�7�1�7","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1�7�äº�1�7�çš�1�7�ç�1�7�¸å�1�7�Œã€ 1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ1�7","Add on","Auto add:on","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ�1�7�1�7","Add off","Auto add:off","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneã€�1�7�1�7")
            elif msg.text in ["Message","è‡ªå�1�7��1�7�è¿½åń1�7 å•å€™èªžç¢ºèª1�7"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsã€�1�7�\n\n" + wait["message"])
            elif "Comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ1�7","Comment on","Comment:on","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ�1�7�1�7","Comment on","Comment off","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª1�7"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")
#-----------------------------------------------
            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    random.choice(KAC).sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------

            elif msg.text in ["Masuk","0878"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
                                                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                                        time.sleep(0.2)
                                                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                                        time.sleep(0.2)
                                                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                                        time.sleep(0.2)
                                                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                                        time.sleep(0.2)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							kk.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ki.updateGroup(G)
							kk.updateGroup(G)
							cl.sendText(msg.to,"ʙᴏᴛs ɪᴛ's ᴀʟʀᴇᴀᴅʏ ᴊᴏɪɴ")
#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							print "kicker ok"
							G.preventJoinByTicket = True
							kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Out","Pulang"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
                                                        kc.leaveGroup(msg.to)
                                                        kd.leaveGroup(msg.to)
                                                        ke.leaveGroup(msg.to)
                                                        ka.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv1 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Cv2 @bye"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv3 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Fuck You")
							kc.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[List Grup]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Mayhem" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    cl.sendText(msg.to,"�� Mayhem\nMayhem is STARTING�7�8\n' abort' to abort�7�8")
                    ki.sendText(msg.to,"�� Mayhem ��\n46 victims shall yell hul��la��ba��loo�7�8\n/�0�5h�0�5l�0�5b�0�5�0�4lo�0�0o,�0�4h�0�5l�0�5b�0�5�0�5lo�0�0o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots and admin:
                                try:
                                   klist=[cl,ki,kk,kc,kd]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Succes Cv")
										kk.sendText(msg.to,"Fuck You"),
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										k3.sendText(msg.to,"Succes Cv")
									except:
										ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
                                                gs = kc.getGroup(msg.to)
                                                gs = kd.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                                        cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ")
									ki.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ")
                                                                        kk.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ")
                                                                        kc.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ")
                                                                        kd.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
                                                gs = kc.getGroup(msg.to)
                                                gs = kd.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak DiTemukan")
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                                        cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴ ᴀɴɢɢᴏᴛᴀ")
									ki.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴ ᴀɴɢɢᴏᴛᴀ")
                                                                        kk.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴ ᴀɴɢɢᴏᴛᴀ")
                                                                        kc.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴ ᴀɴɢɢᴏᴛᴀ")
                                                                        kd.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴ ᴀɴɢɢᴏᴛᴀ")
								except:
									ki.sendText(msg.to,"Berhasil")
#-----------------------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-------------–----------------------------------------





#------------------------------------------------
            elif msg.text in ["Test"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Hadir Boss")
					ki.sendText(msg.to,"Hadir Boss")
					kk.sendText(msg.to,"Hadir Boss")
#-----------------------------------------------
            elif "Tob say " in msg.text:
					bctxt = msg.text.replace("Tob say ","")
					cl.sendText(msg.to,(bctxt))
					ki.sendText(msg.to,(bctxt))
					kk.sendText(msg.to,(bctxt))
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "ufa308a279f813fa5b17bf3bb2a56f403"}
					cl.sendText(msg.to,"ᴛʜɪs ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛs")
					ki.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "ufa308a279f813fa5b17bf3bb2a56f403"}
					cl.sendText(msg.to,"ᴛʜɪs ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛs")
					kk.sendText(msg.to,"Di Add Ya!!")
					ki.sendMessage(msg)
#-----------------------------------------------
            elif "Spam " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#-----------------------------------------------
            elif msg.text == "Read Point":
                    cl.sendText(msg.to, "ʙᴏᴛ ᴀᴋᴀɴ ᴍᴇɴᴅᴇᴛᴇᴋsɪ sɪᴅᴇʀ")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text == "Cek sider":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "== Bakekok Sider == %s\nthat's it\n\nPeople who have ignored reads\n%skampret lo sider. \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n��set��you can send �7�8 read point will be created �7�8")
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       ki.sendText(msg.to,"Grup Creator Telah Diinvite")
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
#-----------------------------------------------
            elif "Cstatus:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
            elif "Cstatus1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                else:
                    ki.sendText(msg.to,"Done")
#-----------------------------------------------
            elif "Cname:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
            elif "Cname1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.displayName = string
                    Ki.updateProfile(profile)
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Rate" in msg.text:
                tanya = msg.text.replace("Rate","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "Stalk " in msg.text:
                print "[Command]Stalk executing"
                stalkID = msg.text.replace("Stalk ","")
                subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                files = glob.glob("tmp/*.jpg")
                for file in files:
                    os.rename(file,"tmp/tmp.jpg")
                fileTmp = glob.glob("tmp/tmp.jpg")
                if not fileTmp:
                    cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                    print "[Command]Stalk,executed - no image found"
                else:
                    image = upload_tempimage(client)
                    cl.sendText(msg.to, format(image['link']))
                    subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                    print "[Command]Stalk executed - succes"
#----------------------------------------------
            elif ".Music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
#-----------------------------------------------
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalam grup itu")
#------------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    ginfo = ki.getGroup(msg.to)
                    ginfo = kk.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
                    ki.sendMessage(msg)
                    kk.sendText(msg.to,"Pembuat Grup =>" + gCreator1)
#-----------------------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                                ki.sendText(msg.to,"Selamat Kamu Admin Baru")
                                kk.sendText(msg.to,"Selamat Ya Selamat")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Lu bukan Creator")
                    cl.sendText(msg.to,"Admin/Member Tidak Bisa Menggunakan Command Add Admin")
                    ki.sendText(msg.to,"Cuma Creator Yang bisa Menggunakan")
            elif "Admrem @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                                ki.sendText(msg.to,"Kamu DiPecat Jadi Admin :(")
                                kk.sendText(msg.to,"Yang Sabar Ya Boss..")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    ki.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")
                    ki.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                    ki.sendText(msg.to,"The adminlist is empty")
                    kk.sendText(msg.to,"Tidak Ada Admin")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    ki.sendText(msg.to,"Tunggu...")
                    kk.sendText(msg.to,"Sabar Jink")
                    mc = ""
                    gh = ""
                    fh = ""
                    for mi_d in creator:
                        mc += "👑" +cl.getContact(mi_d).displayName + "\n"
                    for mi_d in admin:
                        gh += "•" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"=======OWNER=======\n\n" + mc + "\n=======ADMIN=======\n\n" + gh +"\n===================\n")
                    print "[STAFFLIST]"
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                         ki.sendText(msg.to,"Jgn cancel undangan atau autokick!")
                     else:
                         cl.sendText(msg.to,"done")
                         ki.sendText(msg.to,"sudah")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                        ki.sendText(msg.to,"Protect Csncel Off")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"sudah")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                        ki.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"sudah")
#-----------------------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"sᴜᴄᴄᴇs ʙᴀɴɴᴇᴅ ᴀʟʟ")
                   except:
                      pass
#------------------------------------------------------
            elif "Steal dp @" in msg.text:
                nama = msg.text.replace("Steal dp @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        midddd = cl.getContact(linedev.mid)
                        PATH = "http://dl.profile.line-cdn.net/" + midddd.pictureStatus
                    cl.sendImageWithURL(msg.to,PATH)
#------------------------------------------------------------ Restart_Program
            elif msg.text in ["Bot:Restart"]:
                cl.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                ki.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                kk.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                kc.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                kd.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                ka.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                ke.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ")
                restart_program()
                print "@Restart"
#-----------------------------------------------------------------













#-----------------------------------------------------------
            elif msg.text in ["Protect Off","Mode Off"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Gname OFF")
                else:
                    wait["Protectgroupname"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")      
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        mid = cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + tob.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#-----------------------------------------------
            elif "Contact:" in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Contact:","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":midd}
                    cl.sendMessage(msg)
                    ki.sendText("Tuh Midnya Boss")
#-----------------------------------------------------
            elif "Spam change:" in msg.text:
              if msg.from_ in admin:
                wait["spam"] = msg.text.replace("Spam change:","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
              if msg.from_ in admin:
                wait["spam"] = msg.text.replace("Spam add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam:" in msg.text:
              if msg.from_ in admin:
                strnum = msg.text.replace("Spam:","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
#------------------------------------------------------------
            elif "Spamg " in msg.text:
               if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spamg "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                 #@rid1bdbx
                if txt[1] == "on":
                    if jmlh <= 1000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#----------------------------------------------------------------
            elif msg.text in ["Halo","halo"]:
                ki.sendText(msg.to,"halo juga " + ki.getContact(msg.from_).displayName)
                kk.sendText(msg.to,"halo juga " + kk.getContact(msg.from_).displayName)

            elif "Broadcast" in msg.text:
              if msg.from_ in admin:
                 bctxt = msg.text.replace("Broadcast","")
                 n = cl.getGroupIdsJoined()
                 for manusia in n:
                        cl.sendText(manusia,bctxt +"\n\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName)

            elif "Contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Cbc " in msg.text:
               if msg.from_ in admin:
                    bctxt = msg.text.replace("Cbc ", "")
                    t = ki.getAllContactIds()
                    t = kk.getAllContactIds()
                    t = kc.getAllContactIds()
                    t = kd.getAllContactIds()
                    t = ka.getAllContactIds()
                    t = ke.getAllContactIds()
                    for manusia in t:
                        ki.sendText(manusia, (bctxt))
                        kk.sendText(manusia, (bctxt))
                        kc.sendText(manusia, (bctxt))
                        kd.sendText(manusia, (bctxt))
                        ka.sendText(manusia, (bctxt))
                        ke.sendText(manusia, (bctxt))

            if 'MENTION' in msg.contentMetadata.keys() != None:
              if settings["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Dont tag me, im busy",cName + " ngapain ngetag?",cName + " nggk ush tag.klo pnting pc aja","tersummon-_-"]
                    ret_ = "[Auto Respond] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break

            elif "Cek " in msg.text:
                tanggal = msg.text.replace("Cek ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)


            elif "/ig " in msg.text:
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig ","")
                nk1 = nk0.rstrip(' ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig hairu.ones")

            elif "/say " in msg.text:
                    query = msg.text.replace("/say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'id', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)


            elif '.lyric ' in msg.text:
                try:
                    songname = msg.text.lower().replace('.lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#-------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban:" + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
#-----------------------------------------------------------
            elif msg.text in ["Invite:on"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")






#------------------------------------------------------------
            elif "Allbio:" in msg.text:
               if msg.from_ in creator:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "Bio Updated.")
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to, "Bio Updated.")
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to, "Bio Updated.")
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to, "Bio Updated.")
                    profile = kd.getProfile()
                    profile.statusMessage = string
                    kd.updateProfile(profile)
                    kd.sendText(msg.to, "Bio Updated.")
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                    ke.sendText(msg.to, "Bio Updated.")
#-------------------------------------------------------
            elif "/SkuldChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/SkuldChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

            elif "/LeonardoChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/LeonardoChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

            elif "/VerdandiChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/VerdandiChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

            elif "/IanChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/IanChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

            elif "/AthenaChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/AthenaChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = kd.getProfile()
                        profile.displayName = string
                        kd.updateProfile(profile)
                        kd.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

            elif "/PussChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/PussChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = ka.getProfile()
                        profile.displayName = string
                        ka.updateProfile(profile)
                        ka.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

            elif "/SkadiChangename: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/SkadiChangename: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = kd.getProfile()
                        profile.displayName = string
                        ke.updateProfile(profile)
                        ke.sendText(msg.to,"Ganti nama menjadi \"" + string + "\" berhasil")

#------------------------------------------------------
            elif msg.text in ["Protect On","Mode On"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                        ki.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"Gname ON")
                        ki.sendText(msg.to,"Gname ON")
                else:
                    wait["Protectgroupname"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                        ki.sendText(msg.to,"Protect Group On")
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                        ki.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"Block On")
                        ki.sendText(msg.to,"Block On")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                        ki.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"Block On")
                        ki.sendText(msg.to,"Block On")
#-----------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            		ki.sendText(msg.to,text)
            		kk.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            			kk.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            			kk.sendMessage(msg)
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"ᴍɪᴍɪᴄ ᴏɴ")
            				ki.sendText(msg.to,"ᴍɪᴍɪᴄ ᴏɴ")
            				kk.sendText(msg.to,"ᴍɪᴍɪᴄ ᴀᴋᴛɪғ")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            				ki.sendText(msg.to,"Mimic already on")
            				kk.sendText(msg.to,"Mimic Sudah On")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            				ki.sendText(msg.to,"Mimic off")
            				kk.sendText(msg.to,"Mimic Mati")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            				ki.sendText(msg.to,"Mimic already off")
            				kk.sendText(msg.to,"Mimic Telah Mati")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			gInfo = kk.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            				ki.sendText(msg.to,"No targets")
            				kk.sendText(msg.to,"Tidak Ada Target")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ")
            						ki.sendText(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ")
            						kk.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴀʀɢᴇᴛ")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						ki.sendText(msg.to,"Failed")
            						kk.sendText(msg.to,"Gagal")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			gInfo = kk.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            				ki.sendText(msg.to,"No targets")
            				kk.sendText(msg.to,"Tidak Ada Target")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"sᴜᴄᴄᴇs ᴅᴇʟᴇᴛᴇ ᴛᴀʀɢᴇᴛ")
            						ki.sendText(msg.to,"sᴜᴄᴄᴇs ᴅᴇʟᴇᴛᴇ ᴛᴀʀɢᴇᴛ")
            						kk.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴀʀɢᴇᴛ")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						ki.sendText(msg.to,"Failed!")
            						kk.sendText(msg.to,"Gagal")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
            				ki.sendText(msg.to,"No target")
            				kk.sendText(msg.to,"Tidak Ada Target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + ki.getContact(mi_d).displayName +" | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
                                ki.sendText(msg.to,lst + "\nTotal:" + total)
#-----------------------------------------------
#-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#-----------------------------------------------
            elif msg.text in ["Qr On","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴍᴏᴅᴇ [ᴏɴ]")
                        ke.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴍᴏᴅᴇ [ᴏɴ]")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                        ki.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴍᴏᴅᴇ [ᴏɴ]")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Qr Off","qr Off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴍᴏᴅᴇ [ᴏғғ]")
                        ki.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴍᴏᴅᴇ [ᴏғғ]")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                        ki.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴍᴏᴅᴇ [ᴏғғ]")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
#-----------------------------------------------
            elif msg.text in ["hmm"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Batuk Kong??")
            elif msg.text in ["wkwkwk"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"malik mana ya , gw jadi kangen naena sama dia")
            elif msg.text in ["Cv say chomel pekok"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
					kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
					kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Selamat datang di Grup")
					kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping","Samlekom","samlekom"]:
				ki.sendText(msg.to,"Apa 􀜁􀅔Har Har􏿿")
				kk.sendText(msg.to,"Bgsd 􀜁􀅔Har Har􏿿")
				kc.sendText(msg.to,"Asw 􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Responsename","Respon"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"sᴋᴜʟᴅ")
					ki.sendText(msg.to,"ʟᴇᴏɴᴀʀᴅᴏ")
					kk.sendText(msg.to,"ᴠᴇʀᴅᴀɴᴅɪ")
                                        kc.sendText(msg.to,"ɪᴀɴ")
                                        kd.sendText(msg.to,"ᴀᴛʜᴇɴᴀ")
                                        ka.sendText(msg.to,"ᴘᴜss")
                                        ke.sendText(msg.to,"sᴋᴀᴅɪ")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "[sᴘᴇᴇᴅ ʙᴏᴛs...]")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%sseconds" % (elapsed_time))
					ke.sendText(msg.to, "%sseconds" % (elapsed_time))
					kk.sendText(msg.to, "%sseconss" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")                  
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜsᴇʀ ᴛᴇʀʙᴀɴɴᴇᴅ")
					else:
						cl.sendText(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "�1�7" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"Cancel Success!")
						ki.sendText(msg.to,"Cancel Success!")
            elif "random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "album" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecâ†�1�7�1�7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecâ†�1�7�1�7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass

        if op.type == 55:
           try:
               if op.param1 in wait2['readPoint']:
                   Name = cl.getContact(op.param2).displayName
                   if Name in wait2['readMember'][op.param1]:
                       pass
                   else:
                       wait2['readMember'][op.param1] += "\n↪"+ Name
                       wait2['ROM'][op.param1][op.param2] = "🔑" + Name
               else:
                   cl.sendText
           except:
               pass


        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
					        cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By line://ti/p/~syalifr17")
						ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Bot Fantasia")
                                                kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                                                kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by SyalifR\n\nhttp://line.me/ti/p/~syalifr17")
                                                kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                                                kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by SyalifR\n\nhttp://line.me/ti/p/~syalifr17")
                                                kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                                                kd.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by SyalifR\n\nhttp://line.me/ti/p/~syalifr17")
                                                ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                                                ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By line://ti/p/~syalifr17")
                                                ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                                                ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By line://ti/p/~syalifr17")
						print "DiLike"
					except:
							pass
				else:
						print "Sudah DiLike"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
