# Quick EDSA Leaderboard get from Kaggle
# Pre  Script   Procedures - Getting   your   API   key 
#If you haven't installed the Kaggle Package, please do so via PIP:
'''!pip install Kaggle'''

#Once installed - get your Kaggle API key here https://www.kaggle.com/**YOUR USERNAME HERE*/account
#The JSON file needs to be saved in, assuming windows, C:/Users/**YOUR USER**/.kaggle
#Kaggle api checks the environment variable here.


# NB to ensure API Key instructions have been followed first.

# Packages needed
import kaggle as kg
import zipfile
import pandas as pd
import os


# Funtion Defining

def comp_edsa_leaderboard(competition_name):
    '''
    Function Creates Dataframe containing specified competitions leaderboard as at the time of execution.
    
    NB - set Function to object: Object_001 = comp_edsa_leaderboard(competition_name)
    
    Competition Name = Kaggle Denominated name 
    
    Best place to obtain is in URL
    E.g - https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
    **house-prices-advanced-regression-techniques**
    
    '''

    #Authentication with Kaggle API
    kg.api.authenticate()
    
    #Api request leaderboard file - Saves Zip File in local directory
    kg.api.competition_leaderboard_download(competition=competition_name,path=r'./')
    
    #Opens Zip File 
    zf = zipfile.ZipFile(r'./'+str(competition_name)+'.zip')
    
    #Grabs CSV from zip file and loads into Dataframe
    df_comp_leaderboard = pd.read_csv(zf.open(str(competition_name)+'-publicleaderboard.csv'))
    
    #Deletes zf object so as to allow delete of zip file in local direcotry, deletes zip file.
    del zf
    os.remove(str(competition_name)+'.zip')
    
    return df_comp_leaderboard


# Play Ground

#Calling the function
df_comp_leaderboard = comp_edsa_leaderboard('house-prices-advanced-regression-techniques')

#Filters the Dataframe to show only EDSA teams &&& only the team's lowest score.
df_comp_leaderboard[df_comp_leaderboard['TeamName'].str.contains('EDSA')].groupby('TeamId').min().sort_values('Score')

