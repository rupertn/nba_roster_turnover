import pandas as pd

rosters = pd.read_csv('rosters.csv')
df = rosters.copy()

# Fixing incorrect name formats
df.loc[df['name'] == 'Devontae Cacok\xa0\xa0(TW)', 'name'] = 'Devontae Cacok'
df.loc[df['name'] == 'Kostas Antetokounmpo\xa0\xa0(TW)', 'name'] = 'Kostas Antetokounmpo'

df[['first_name', 'last_name']] = df['name'].str.split(expand=True)


def get_initials(name):
    words = name.replace('-', ' ').split()
    return ''.join([word[0] for word in words])


df['initials'] = df['name'].apply(lambda x: get_initials(x))

df['season_player'] = [list(a) for a in (zip(df.season, df.name))]
player_list = df['season_player'].to_list()


def player_returned(p_list, season_player):
    if season_player[0] == 2021:
        return None
    elif [season_player[0] + 1, season_player[1]] in p_list:
        return 1
    else:
        return 0


df['returned'] = df.apply(lambda row: player_returned(player_list, row['season_player']), axis=1)

nickname_dict = dict(zip(df.initials.str.lower(), df.name.str.lower()))

nickname_dict['kuz'] = 'kyle kuzma'
nickname_dict['bron'] = 'lebron james'
nickname_dict['lbj'] = 'lebron james'
nickname_dict['zu'] = 'ivica zubac'
nickname_dict['zo'] = 'lonzo ball'
nickname_dict['jr'] = 'j.r. smith'
nickname_dict['wes'] = 'wesley matthews'
nickname_dict['kief'] = 'markieff morris'

del nickname_dict['am']
del nickname_dict['it']
del nickname_dict['js']

df['season'] = df['season'].astype(str)

roster_train = df[df['season'] != '2021']
roster_test = df[df['season'] == '2021']

len(df['name'].unique())

# roster_train.to_csv('roster_train.csv', index=False)
# roster_test.to_csv('roster_test.csv', index=False)
