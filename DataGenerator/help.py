fashion_wordset = ['Blazer', 'Dupatta', 'Jeans', 'T-Shirt', 'Socks', 'Watch', 'Tops', 'Clogs', 'Trainers', 'Salwar',
                   'Activewer', 'Swimwear', 'Kurta', 'Sandals', 'Blouse', 'Jumpsuit', 'Suits', 'Churidar', 'Jackets',
                   'Sweater', 'Bags', 'Coat', 'Hat', 'Bra', 'Loafers', 'T-shirts', 'Dresses', 'Leggings', 'Watches',
                   'Sherwani', 'Wedges', 'Shapewear', 'Flip Flops', 'Dress', 'Scarf', 'Gloves', 'Bodysuit', 'Pants',
                   'Nightwear', 'Sweatshirt', 'Wallet', 'Panties', 'Sneakers', 'Denim', 'Belt', 'Shirt', 'Sliders',
                   'Underwear', 'Tie', 'Tuxedo', 'Shorts', 'Hats', 'Heels', 'Jacket', 'Boots', 'Bag', 'Slippers',
                   'Espadrilles', 'Skirt', 'Sunglasses', 'Saree', 'Mules', 'Flats', 'Wallets', 'Jodhpuri', 'Shoes',
                   'Belts', 'Trousers', 'Kurti', 'Mask', 'Gloves', 'Socks', 'Sweatshirt', 'Sweater', 'T-Shirt', 'Shirt',
                   'Perfume', 'Tie', 'Jacket', 'Coat', 'Jeans', 'Shorts', 'Pants', 'Skirt', 'Dress', 'Blazer', 'Suit',
                   'Cream', 'Flip-Flops', 'Thongs', 'Top', 'Jean'
                   ]

# keep only unique words
fashion_wordset = list(set(fashion_wordset))

print(fashion_wordset)

# If word end in 's' then remove that and add to new list
fashion_wordset_s = []
for word in fashion_wordset:
    if word.endswith('s'):
        fashion_wordset_s.append(word[:-1])

print(fashion_wordset_s)

# from words in fashion wordset if a word include in another word add to new list
fashion_wordset_ss = []
fashion_wordset_sss = []
for word in fashion_wordset:
    for word2 in fashion_wordset:
        if word in word2 and word != word2:
            fashion_wordset_ss.append(word)
            fashion_wordset_sss.append(word2)

print(fashion_wordset_ss)
print(fashion_wordset_sss)


ss = ['Boot', 'Short', 'Trouser', 'Sneaker', 'Espadrille', 'Trainer', 'Pant', 'Flip-Flop', 'Wallet', 'T-shirt',
      'Belt', 'Pantie', 'Mule', 'Flat',  'Wedge', 'Bag', 'Shoe', 'Top', 'Sandal', 'Glove', 'Legging', 'Slider',
      'Sock', 'Thong', 'Clog', 'Slipper', 'Loafer', 'Jacket', 'Heel', 'Suit', 'Jean', 'Watche', 'Flip Flop',
      'Sunglasse', 'Hat']

a =   1588 + 1258 + 1065 + 778 + 514 + 451 + 407 + 396 + 322 + 310 + 302 + 292 + 260 + 245 + 215 + 158 + 150 + 143 + 122 + 107 + 94 + 89 + 82 + 69 + 64 + 53 + 45 + 45 + 41 + 41 + 40 + 34 + 31 + 27 + 27 + 24 + 20 + 17 + 15 + 14 + 14 + 10 + 9 + 9 + 9 + 8 + 7 + 4 + 4 + 4 + 4 + 3 + 3 + 2 + 2 + 1 + 1 + 1 + 1

print(a)
