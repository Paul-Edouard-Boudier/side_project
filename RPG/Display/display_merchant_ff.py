
def display_merchant(merchant: 'Merchant', hero: 'Hero'):
    print(f' ================================= ')
    for i in range(1, merchant.life_potion_count):
        print(f'|| Life potion : 25 golds ')
    print(f' =================================')
    print(f'You have {hero.hero_gold_value} golds')
