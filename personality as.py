import pyautogui as pg
import webbrowser as wb

points = 0

show = pg.prompt(" What is your favorite show? ")

if show == "my little pony":
    wb.open ("https://mylittlepony.hasbro.com/en-us/videos/categories?categorytype=tvshows&subbrand=mylittlepony&category=soundtrack&playlistid=&videoid=4586810663001")
    pg.alert ("That is a really AMAZIINNNNGGGGGG show!I love bubblegum")
    points += 2
elif show == "barbie":
    wb.open ("//www.youtube.com/watch?v=nsoAajFkBYY")
    pg.alert (" ken is james charles SHHHHHHH!")
    points += 5
elif show == "toddlers in tiaras":
    wb.open ("https://www.youtube.com/watch?v=kml7XztIRAY")
    pg.alert (" OMGIZZLESS I LOVES TODDLERS WAAAOOOW")
    points += 10
elif show == " dora the explorer":
    wb.open ("https://www.youtube.com/watch?v=Fm6YSvdnvww")
    pg.alert (" BOOTS")
elif show == "nemo":
    wb.open ("https://www.youtube.com/watch?v=5Ouc1oDFoos")
    pg.alert ("NEMO ISNT A SHOWWWW")
    points -= 10
elif show == "music":
    wb.open ("https://www.youtube.com/watch?v=PZtDUzE0CAM")
    pg.alert (" like the song? ")
    points -= 20
elif show == "horror movies":
    wb.open ("https://www.youtube.com/watch?v=XTgFtxHhCQ0")
    pg.alert (" horrow movies ARE SO FUN TO WATCHHHHHHHHH")
    points += 20
elif show == "aMERICan horror story":
    wb.open ("https://www.youtube.com/watch?v=I2jFHMgZ71U")
    pg.alert (" yikes thats creepy")
else:
    pg.alert ("your fav show is " + show)

    
food = pg.prompt(" What is your favorite food? ")

if food == "grapes":
    wb.open ("https://www.youtube.com/watch?v=tlQy1dYNzY0")
    pg.alert ("i only like GREEN grapes!")
    points += 50
elif food == "belly button":
    wb.open ("https://www.youtube.com/watch?v=TO8gAvl59Kw")
    pg.alert (" BELLY BUTTTTOOOONN")
    points -= 100
elif food == "cake":
    wb.open ("https://www.youtube.com/watch?v=3kyn9Es4HoY")
    pg.alert ("Cake is your favorite food?!")
elif foood == "every food":
    wb.open ("https://www.youtube.com/watch?v=8lQCbaIK2PI")
    pg.alert (" STOP ITTT")
    points += 1000
elif food == "no food":
    wb.open ("https://www.youtube.com/watch?v=8lQCbaIK2PI")
    pg.alert (" yikes awkward")
    points -= -1000
elif food == "chicken nuggs":
    wb.open ("https://www.youtube.com/watch?v=8lQCbaIK2PI")
    pg.alert (" NUGGETSSSS")
else:
    pg.alert ("your fav food is " + food)
    
animal = pg.prompt(" What is your favorite animal? ")

if animal == " polar bear":
    wb.open ("https://www.youtube.com/watch?v=fsQwmRgEEr4")
    pg.alert (" i only like koalas!")
    points += 200
elif animal == "red panda":
    pg.alert (" WOW they are not like pandas at all!")
    points +=10000
elif animal == "frog":
    wb.open ("https://www.youtube.com/watch?v=bvKD_aplsvw")
    pg.alert (" RIBIT")
    points += 1
elif animal == "turtle":
    wb.open ("https://www.youtube.com/watch?v=PBVtZbpiRZA")
    pg.alert (" i loooooooooooooooooooooooooveeeeeeeeeeeeeeee turttttllllllllleeessssssssssssssssssssssssssssssssssssssssssssssss")
    points +=100
elif animal == "every animal":
    pg.alert (" CHOOOOSE ONE")
elif animal == "fish":
    pg.alert (" What FISH")
    points += 1
else:
    pg.alert ("your fav animal is " + animal)

holiday = pg.prompt(" What is your favorite holiday? ")

if holiday == "christmas":
    wb.open ("https://www.youtube.com/watch?v=wscrNSqAHSs")
    pg.alert (" HAVE A HOlLY JOLLY CHRISTMAS ITS THE BEST TIME OF THE YEAR!")
    points += 10000000
elif holiday == " halloween":
    wb.open ("https://www.youtube.com/watch?v=Bt5rCgHN1Gc")
    pg.alert (" BOOOOOOOOOOO")
    points += 666
elif holiday == "THANKSGIVING":
    wb.open ("https://www.youtube.com/watch?v=Ywmfexl-2sc")
    pg.alert (" OMG SO MUCH FOOD")
    points += 3
elif holiday == "new years":
    wb.open ("https://www.youtube.com/watch?v=lvJRmdN9iyU")
    pg.alert (" bye bye new years resolutions")
elif holiday == "Easter":
    wb.open ("https://www.youtube.com/watch?v=q7UXYvRRZFc")
    pg.alert (" have you ever wondered why it is a bunny laying eggs?")
    points +=3456789
elif holiday == "birthday":
    wb.open ("https://www.youtube.com/watch?v=BTs5FS66IUI")
    pg.alert (" When is your birthday?")
    points += 80000000000000000
else:
    pg.alert ("your fav holiday is " + holiday)


seasons = pg.prompt(" What is your favorite season? ")

if seasons == "fall":
    wb.open ("https://www.youtube.com/watch?v=CyJIfdA71Lc")
    pg.alert (" OMG FALL IS MY FAVORITE! the weather is so nice")
    points += 400
elif seasons == "spring":
    wb.open ("https://www.youtube.com/watch?v=DobrRgD5aOU")
    pg.alert (" I LOVE all the flowers that pop up!")
    points += 34
elif seasons == "winter":
    wb.open ("https://www.youtube.com/watch?v=-b-U1eQqBmk")
    pg.alert (" Yikes winter is way to cold for me")
    points -= 999999999999999999999999999999999999
elif seasons == "summer":
    wb.open ("https://www.youtube.com/watch?v=mVhh0oATqBI")
    pg.alert (" HOT HOT HOT")
    points += 333
elif seasons == "all seasons":
    wb.open ("https://www.youtube.com/watch?v=Iisj2kTZIFs")
    pg.alert (" You have to have one favorite!")
    points -=987654321
elif seasons == "none":
    wb.open ("https://www.youtube.com/watch?v=a6GGZ68mOZA")
    pg.alert (" yikes are you ok?")

else:
    pg.alert ("your season is show is " + seasons)
