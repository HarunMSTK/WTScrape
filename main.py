#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import discord
import os
import json 

#API'S

def getUser(nickname):
    base_url = "https://wtapi.joygame.com:443/api/Profile/GetPublicGameInfo"
    base_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "chrome-extension://gmmkjpcadciiokjpikmkkmapphbmdjok", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    base_json={"nickname": f"{nickname}"}
    r = requests.post(base_url, headers=base_headers, json=base_json)
    data = r.json()
    if data["Data"] != None:
        return data 
    else:
        return False
def getMemberList(clan):
    base_url = "https://wtapi.joygame.com/api/Clan/GetClanMemberList"
    base_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "chrome-extension://gmmkjpcadciiokjpikmkkmapphbmdjok", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    base_json={"ClanName": f"{clan}"}
    r = requests.post(base_url, headers=base_headers, json=base_json)
    data = r.json()
    if data["Data"] != None:
        return data 
    else:
        return False
def getClan(clan):
    base_url = "https://wtapi.joygame.com/api/Clan/GetClanInfo"
    base_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "chrome-extension://gmmkjpcadciiokjpikmkkmapphbmdjok", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    base_json={"ClanName": f"{clan}"}
    r = requests.post(base_url, headers=base_headers, json=base_json)
    data = r.json()
    if data["Data"] != None:
        return data 
    else:
        return False
def getClanRank(clan):
    base_url = "https://wtapi.joygame.com/api/Ranking/GetClanDailyRanking"
    base_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "chrome-extension://gmmkjpcadciiokjpikmkkmapphbmdjok", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    base_json={"ClanName": f"{clan}"}
    r = requests.post(base_url, headers=base_headers, json=base_json)
    data = r.json()
    if data["Data"] != None:
        return data 
    else:
        return False
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 

# DISCORD BOT   
  
TOKEN = "YOUR_BOT_TOKEN"
client = discord.Client(command_prefix="!")
@client.event
async def on_ready():
    print(f'Connected To {client.user}!')
@client.event
async def on_message(message):
    async with message.channel.typing():
        if "!hesapara" in message.content:
            nickname = message.content.replace("!hesapara","").strip()
            data = getUser(nickname) 
            if data != False:
                Rank = data["Data"]["Rank"]
                Grade = data["Data"]["Grade"]
                PrevRank = data["Data"]["PrevRank"]
                UserName = data["Data"]["Name"]
                ClanName = data["Data"]["ClanName"]
                Exp = data["Data"]["Exp"]
                Win = data["Data"]["Win"]
                Lose= data["Data"]["Lose"]
                Dead = data["Data"]["Dead"]
                HeadShot = data["Data"]["HeadShot"]
                WolfKill = data["Data"]["WolfKill"]
                Kill = data["Data"]["Kill"]
                Dead = data["Data"]["Dead"]
                TotalRound = data["Data"]["TotalRound"]
                GrenadeKill = data["Data"]["GrenadeKill"]
                CampaignFlag = data["Data"]["CampaignFlag"]
                LastLoginDate = data["Data"]["LastLoginDate"]
                FirstCashUse = data["Data"]["FirstCashUse"]
                PrideRegisterTime = data["Data"]["PrideRegisterTime"]
                PrideOrder = data["Data"]["PrideOrder"]
                BoxCount = data["Data"]["BoxCount"]
                UserCreateDate = data["Data"]["UserCreateDate"]
                PlayTime = int(data["Data"]["PlayTime"] / 60 / 24)
                FavWeapon = data["Data"]["FavouriteWeapon"]["Name"]
                FavWeaponIMG = data["Data"]["FavouriteWeapon"]["ImageUrl"]
                with open('rankData.json',encoding='utf-8') as f:
                    data = json.load(f)
                    for n in range (0,73):
                        if data["Data"][n]["RankId"] == Grade:
                            RankTitle = data["Data"][n]["Title"]
                            IMG = data["Data"][n]["ImageUrl"]
                            if "http" not in IMG:
                                IMG = "http:"+data["Data"][n]["ImageUrl"]
                            else:
                                IMG = data["Data"][n]["ImageUrl"]
                embed=discord.Embed(title=UserName+" Kullanıcısının Bilgileri", color=0x6d01a7)
                embed.set_author(name=RankTitle, icon_url=IMG)
                embed.set_thumbnail(url=FavWeaponIMG)
                embed.add_field(name="Sıralama", value=Rank, inline=True)
                embed.add_field(name="Gelişim Puanı", value=Exp, inline=True)
                embed.add_field(name="Klan", value=ClanName, inline=True)
                embed.add_field(name="Toplam Maç", value=TotalRound, inline=True)
                embed.add_field(name="Oyun Süresi", value=f"{PlayTime} Saat", inline=True)
                embed.add_field(name="Açılan Kutu", value=BoxCount, inline=True)
                embed.add_field(name="Kazanma", value=Win, inline=True)
                embed.add_field(name="Kaybetme", value=Lose, inline=True)
                embed.add_field(name="Öldürme", value=Kill, inline=True)
                embed.add_field(name="Ölme", value=Dead, inline=True)
                embed.add_field(name="Tam Kafadan", value=HeadShot, inline=True)
                embed.add_field(name="Bomba", value=GrenadeKill, inline=True)
                embed.add_field(name="Kurtla Öldürme", value=WolfKill, inline=True)
                embed.add_field(name="Favori Silahı", value=FavWeapon, inline=True)
                embed.add_field(name="Son Giriş", value=LastLoginDate, inline=True)
                embed.add_field(name="Kayıt Tarihi", value=UserCreateDate, inline=True)
                embed.add_field(name="İlk Nakit Kullan Tarihi", value=FirstCashUse, inline=True)
                embed.set_footer(text="Powered by 4NaT")
                await message.channel.send(embed=embed)
            elif data == False:
                embed=discord.Embed(title="Aradığın Hesabı Bulamadık!", description=nickname+" Kullanıcısı Bulunamadı!", color=0x7a00b3)
                embed.set_footer(text="Powered by 4NaT")
                await message.channel.send(embed=embed)
        elif "!klanara" in message.content:
            clan = message.content.replace("!klanara","").strip()
            data = getClan(clan) 
            data1 = getClanRank(clan) 
            if data and data1 != False:
                ClanName = data["Data"]["ClanName"]
                ClanRank = data1["Data"]["Rank"]
                ClanOwner = data1["Data"]["ClanMaster"]
                MemberCount = data["Data"]["MemberCount"]
                WinCount = data["Data"]["ClanBattleWinCount"]
                LoseCount = data["Data"]["ClanBattleLoseCount"]   
                CreateDate = data["Data"]["CreateDate"]
                ClanExp = data["Data"]["Exp"]  
                ID = data["Data"]["Id"]  
                BattleCount = WinCount + LoseCount
                embed=discord.Embed(title=ClanName+" Klanının Bilgieri", color=0x6d01a7)
                embed.set_author(name=ClanName)
                embed.add_field(name="Klan Kimliği", value=ID, inline=True)
                embed.add_field(name="Kazanma", value=WinCount, inline=True)
                embed.add_field(name="Kaybetme", value=LoseCount, inline=True)
                embed.add_field(name="Sıra", value=ClanRank, inline=True)
                embed.add_field(name="Sahibi", value=ClanOwner, inline=True)
                embed.add_field(name="EXP", value=ClanExp, inline=True)
                embed.add_field(name="Üye Sayısı", value=MemberCount, inline=True)
                embed.add_field(name="Maç Sayısı", value=BattleCount, inline=True)
                await message.channel.send(embed=embed)
            elif data == False:
                embed=discord.Embed(title="Aradığın Klanı Bulamadık!", description=clan+" Klanı Bulunamadı!", color=0x7a00b3)
                embed.set_footer(text="Powered by 4NaT")
                await message.channel.send(embed=embed)
        elif "!klanoyuncu" in message.content:
            clan = message.content.replace("!klanoyuncu","").strip()
            data = getMemberList(clan) 
            x = []
            if data != False:
                for n in range (0,50):
                    try:
                        MemberName = data["Data"][n]["MemberNickname"]
                        MemberJoin = data["Data"][n]["JoinDate"]
                        x.append(f"Ad: {MemberName} | Katılım Tarihi: {MemberJoin}\n")
                    except:
                        break
                m = listToString(x)
                await message.channel.send(f"```{m}```")
client.run(TOKEN)
