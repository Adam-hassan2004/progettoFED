import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="civ"
)

mycursor = mydb.cursor()


query = """
LOAD DATA INFILE 'Leaderbias.csv'
INTO TABLE civ.leaders
IGNORE 1 LINES 
( nome ,Boldness ,Chattiness ,Denounce_WillIngness ,Diplomatic_Balance ,Friendship_Willingness,Forgiveness ,Loyalty ,Meaness ,CityState_Competitiveness ,Neediness ,Victory_Competitiveness ,Warmonger_Hatred ,Air ,Airlift ,AntiAir ,Archaeology, Diplomacy,Gold, Growth,Happiness,Land_Trade,Sea_Trade,Naval, Build_Nuke, Recon, Religion,Spaceship,Use_Nuke,Friendly,Hostile,Neutrality, War, CS_Conquest,CS_Protect,)
"""

mycursor.execute(query)


