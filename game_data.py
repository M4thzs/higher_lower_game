# import pandas as pd


# url = 'https://pt.wikipedia.org/wiki/Lista_das_contas_mais_seguidas_no_Instagram'
# html = pd.read_html(url)
# table = html[0]
# print(table.columns)
# dictionary = dict(zip(table["Proprietário/a"], table["Seguidores (milhões)[1]"]))
# print(dictionary)

# Dicionário com algumas das páginas mais seguidas no Instagram
instagram_followers_millions = {
    'Lionel Messi': 504.0, 'Selena Gomez': 422.0, 'Dwayne Johnson': 395.0, 'Kylie Jenner': 394.0,
    'Ariana Grande': 376.0, 'Kim Kardashian': 358.0, 'Beyoncé': 313.0, 'Khloé Kardashian': 304.0,
    'Nike': 302.0, 'Justin Bieber': 294.0, 'Kendall Jenner': 289.0, 'Taylor Swift': 282.0,
    'National Geographic': 279.0, 'Virat Kohli': 270.0, 'Jennifer Lopez': 249.0, 'Neymar': 228.0,
    'Nicki Minaj': 226.0, 'Kourtney Kardashian': 220.0, 'Miley Cyrus': 213.0, 'Katy Perry': 204.0,
    'Zendaya': 180.0, 'Kevin Hart': 177.0, 'Real Madrid CF': 171.0, 'Cardi B': 164.0,
    'LeBron James': 159.0, 'Demi Lovato': 154.0, 'Rihanna': 150.0, 'Chris Brown': 144.0,
    'Drake': 143.0, 'Ellen DeGeneres': 137.0, 'FC Barcelona': 135.0, 'Kylian Mbappé': 123.0,
    'Billie Eilish': 121.0, 'UEFA Champions League': 118.0, 'Gal Gadot': 108.0, 'Lisa': 105.0,
    'Vin Diesel': 103.0, 'NASA': 96.7, 'Shraddha Kapoor': 94.2, 'Priyanka Chopra': 92.5,
    'Narendra Modi': 92.4, 'Shakira': 90.8, 'NBA': 89.5, 'David Beckham': 88.2, 'Snoop Dogg': 88.0,
    'Dua Lipa': 87.4, 'Alia Bhatt': 86.2, 'Jennie': 86.1
}