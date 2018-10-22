import pandas as pd
import numpy as np

df = pd.read_csv("Results/StrainScrape_full_2018-10-21.csv")

props = []
for i in range(15):
    props.append('prop' + str(i+1))
unique_props = [pd.unique(df[prop]).flatten() for prop in props]
prop_set = set(np.concatenate(unique_props, axis=0))
prop_set.remove(np.nan)
print(prop_set)

cols = ['strain_name', 'species', 'flavour1', 'flavour2', 'flavour3', 'Pain', 'Euphoric', 'Fatigue', 'Paranoid',
        'Focused', 'Spasticity', 'Nausea', 'Tingly', 'Headache', 'Dry Mouth', 'Aroused', 'Happy', 'Muscle Spasms',
        'Uplifted', 'Anxious', 'Energetic', 'Headaches', 'Depression', 'Giggly', 'Talkative', 'Dizzy', 'Insomnia',
        'Inflammation', 'Stress', 'Relaxed', 'Seizures', 'Cramps', 'Sleepy', 'Hungry', 'Lack of Appetite', 'Dry Eyes',
        'Creative', 'Eye Pressure', 'Orange', 'Violet', 'Mint', 'Peach', 'Chestnut', 'Rose', 'Coffee', 'Citrus',
        'Lime', 'Plum', 'Sage', 'Pine', 'Pungent', 'Pear', 'Tar', 'Tree Fruit', 'Berry', 'Vanilla', 'Pepper',
        'Chemical', 'Tea', 'Ammonia', 'Apple', 'Skunk', 'Pineapple', 'Grapefruit', 'Honey', 'Earthy', 'Cheese',
        'Blue Cheese', 'Tropical', 'Grape', 'Lemon', 'Flowery', 'Strawberry', 'Butter', 'Tobacco', 'Spicy/Herbal',
        'Woody', 'Blueberry', 'Sweet', 'Lavender', 'Nutty', 'Apricot', 'Diesel', 'Menthol', 'Mango']

flavours = []
for i in range(3):
    flavours.append('flavour' + str(i+1))
unique_flavours = [pd.unique(df[flavour]).flatten() for flavour in flavours]
flavour_set = set(np.concatenate(unique_flavours, axis=0))
flavour_set.remove(np.nan)
print(flavour_set)