import spotipy
import spotipy.oauth2 as oauth2
import random
import account_info
import logging
import threading

class LinkGenerator:

    def __init__(self, log):
        self.__log = log
        self.__lock = threading.Lock()
        self.__spotify = self.__login()

    '''
    def __test_main(self):
        print(chooseTrack())
    '''

    def __login(self):
        credentials = oauth2.SpotifyClientCredentials(
        client_id=account_info.client_id,
        client_secret=account_info.client_secret)

        token = credentials.get_access_token()
        spotify = spotipy.Spotify(auth=token)

        return spotify

    def __chooseBand(self):

        band_list = ["spotify:artist:0ybFZ2Ab08V8hueghSXm6E",   #Opeth
                    "spotify:artist:2aaLAng2L2aWD2FClzwiep",   #Dream Theater
                    "spotify:artist:2Hkut4rAAyrQxRdof7FVJq",   #Rush
                    "spotify:artist:1uRpg2s2jNaxbmoNiJDGfd",   #Pain of Salvation
                    "spotify:artist:6w6z8m4WXX7Tub4Rb6Lu7R",   #Jethro Tull
                    "spotify:artist:2OgUPVlWYgGBGMefZgGvCO",   #Queensryche
                    "spotify:artist:5yjbUO1Jocui7RKE30zfLT",   #Riverside
                    "spotify:artist:3Uz6jx81OY2J5K8Z4wmy2P",   #Camel
                    "spotify:artist:0k17h0D3J5VfsdmQ1iZtE9",   #Pink Floyd
                    "spotify:artist:4lrBMUSk8PiNnCEZfsmPAk",   #Pineapple Thief
                    "spotify:artist:4X42BfuhWCAZ2swiVze9O0",   #Steven Wilson
                    "spotify:artist:5NXHXK6hOCotCF8lvGM1I0",   #Porcupine Tree
                    "spotify:artist:4DFhHyjvGYa9wxdHUjtDkc",   #A Perfect Circle
                    "spotify:artist:7M1FPw29m5FbicYzS2xdpi",   #King Crimson
                    "spotify:artist:7AC976RDJzL2asmZuz7qil",   #Yes
                    "spotify:artist:7jefIIksOi1EazgRTfW2Pk",   #ELO
                    "spotify:artist:1hrQ50kU6hMQBVLatqUqnO",   #Gentle Giant
                    "spotify:artist:7dtYyLTWjuZGOcweC3eD2f",   #Strawbs
                    "spotify:artist:2oVy65ms3RMMhwnAPUEisV",   #Crack the Sky
                    "spotify:artist:5JeJHWfm2ZxNd09hrIf7Zb",   #Magma
                    "spotify:artist:7ai5TWiOG8g9Hds5AATS28",   #Marillion
                    "spotify:artist:2m62cc253Xvd9qYQ8d2X3d",   #The Alan Parsons Project
                    "spotify:artist:0r1s1XoxdoXECGfyChzb2v",   #Liquid Tension Experiment
                    "spotify:artist:3xrzXKnScjOEoy172vsJMW",   #Blackfield
                    "spotify:artist:3CkvROUTQ6nRi9yQOcsB50",   #Genesis
                    "spotify:artist:02frazNrWgZCxUEf4UTfHt",   #Van der Graaf Generator
                    "spotify:artist:0nCiidE5GgDrc5kWN3NZgZ",   #Emerson, Lake & Palmer
                    "spotify:artist:2jK54ZlZhTF1TxygsVeR05",   #Hawkwind
                    "spotify:artist:1MD5pgVzlusqGyuSTcTxvu",   #Premiata Forneria Marconi
                    "spotify:artist:5A0MH7JfEBEMySevsmauds",   #Soft Machine
                    "spotify:artist:00ZLLJ51l9Ir5gyaGSUYxL",   #Eloy
                    "spotify:artist:00Uv0804nrBM2RxUBTkyHj",   #Wobbler
                    "spotify:artist:75U40yZLLPglFgXbDVnmVs",   #The Mars Volta
                    "spotify:artist:1HN6EhIK1fRYk5gtXHclZv",   #Spock's Beard
                    "spotify:artist:45O9BwPMyywM755SYUK0sP",   #Uriah Heep
                    "spotify:artist:0GbqW5TJr7n4is453VOY4C",   #Procol Harum
                    "spotify:artist:3JsMj0DEzyWc0VDlHuy9Bx",   #Supertramp
                    "spotify:artist:36QJpDe2go2KgaRleHCDTp",   #Led Zeppelin
                    "spotify:artist:6aJOdlEvn7AFJTHCLZTwJH",   #Happy the Man
                    "spotify:artist:0BI5vXwUl4lZMtARfXQ0No",   #The Flower Kings
                    "spotify:artist:47yvARr7dCOKqvjDVwfbf3",   #Gong
                    "spotify:artist:0ZXKT0FCsLWkSLCjoBJgBX",   #Anathema
                    "spotify:artist:0Opj9xi9HHrH0L9uHAKnKm",   #Oceansize
                    "spotify:artist:40DqL6Tv84cKT2pH2NMs9r",   #Roger Waters
                    "spotify:artist:2FcC4sDMXme2ziI7tGKMK8",   #David Gilmour
                    "spotify:artist:4vs7NIU7kZc2Efh6yOGKEZ",   #Steve Hackett
                    "spotify:artist:38uWD5h115pdz278q4rwZW",   #Soen
                    "spotify:artist:6HN1s0JzLowapZ7nhOAJ71",   #Naxatras
                    "spotify:artist:0oSGxfWSnnOXhD2fKuz2Gy",   #David Bowie
                    "spotify:artist:2pVMD4bFwl4AyoYyyo51Qg",   #Barclay James Harvest
                    "spotify:artist:5oHYrXNyCSEdacKCCrteMX",   #The Nice
                    "spotify:artist:0ifzzRKdmtgaHy9cfnnyCR",   #Focus
                    "spotify:artist:7uBH52YnXUbJ0ssoyNqQTB",   #Peter Hammill
                    "spotify:artist:4RuYtHjAKBufQRqBUMiOfK",   #Banco Del Mutuo Soccorso
                    "spotify:artist:3lnV6khgTreN8QiqtSAAgW",   #Triumvirat
                    "spotify:artist:6mFPT1M2JWpuoSGSCQCpHX",   #Alphataurus
                    "spotify:artist:7HBJP1DqJrxWZCNODl5lii",   #Gracious
                    "spotify:artist:2AVt92RJvypZ6WIvhNyTej",   #Utopia
                    "spotify:artist:4MERAVAHX04B50JOnasmWf",   #Renaissence
                    "spotify:artist:1tOf99w6rxZmDobcsiuXMH",   #Solaris
                    "spotify:artist:6p9KeMVhd7SS0CYh9l44bq",   #Maxophone
                    "spotify:artist:4di9TLoyXVRLmXm79GOvxQ",   #Latte E Miele
                    "spotify:artist:42rAM3PDey3Z3QIDrAQ3ux",   #Different Light
                    "spotify:artist:4POFwgsibhA3uhQo08kUEw",   #Greenslade
                    "spotify:artist:5YeoQ1L71cXDMpSpqxOjfH",   #Sonata Arctica
                    "spotify:artist:1Dvfqq39HxvCJ3GvfeIFuT",   #Mastodon
                    "spotify:artist:19sJfp2FK2evlsw46WVhPG",   #Paul Gilbert
                    "spotify:artist:1SDL0IuBpmrqx7Jag5HWdQ",   #OSI
                    "spotify:artist:73p7913nnreqv6jbWpeNb1",   #Storm Corrison
                    "spotify:artist:6uejjWIOshliv2Ho0OJAQN",   #Devin Townsend
                    "spotify:artist:6Zd7AjXsoLaweP9FHyudVC",   #Caligula's House
                    "spotify:artist:3nhimyYmNisxdoWj6T7HEY",   #Memory Garden
                    "spotify:artist:0AZ3VR0YbFcS0Kgei7L2QF",   #Russian Circles
                    "spotify:artist:4ZNG0WQPQ10ehIVkCnM5ku",   #Gandalf
                    "spotify:artist:0n2Uel3CvQrmMsYLEfpO3s",   #Nektar
                    "spotify:artist:2hl0xAkS2AIRAu23TVMBG1",   #Kansas
                    "spotify:artist:568ZhdwyaiCyOGJRtNYhWf",   #Deep Purple
                    "spotify:artist:6UUrUCIZtQeOf8tC0WuzRy",   #Sigur Ros
                    "spotify:artist:5g8zU3hIMirIT8gwhV6Hlz",   #Beardfish
                    "spotify:artist:1Joel9mDWSEZfHPE2KooW3",   #Gazpacho
                    "spotify:artist:3Ao7NH7lRyQAeKQg2mlTcO"    #Mahavishnu Orchestra
                    ]
        
        selected = random.choice(band_list)
        
        self.__log.printLog("debug","Band: " + str(selected))

        return selected

    def __chooseAlbum(self):

        album_list = []
        albums = self.__spotify.artist_albums(self.__chooseBand(), album_type='album')

        for i in albums['items']:
            if('TR' in i['available_markets']):
                album_list.append(i['external_urls']['spotify'])
            
        selected = random.choice(album_list)
        
        self.__log.printLog("debug","Album: " + str(selected))

        return selected

    def chooseTrack(self):
        with self.__lock:
            track_list = []
            track = self.__spotify.album_tracks(self.__chooseAlbum(), limit=50, offset=0)

            for i in track['items']:
                track_list.append(i['external_urls']['spotify'])

            selected = random.choice(track_list)
            
            self.__log.printLog("debug", "Track: " + str(selected))
        
            return selected
