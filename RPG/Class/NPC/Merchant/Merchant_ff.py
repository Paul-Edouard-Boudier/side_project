def buy_potion(seller: 'Merchant', buyer: 'Hero'):
    seller.life_potion_count -= 1
    buyer.life_potion_count += 1
    buyer.hero_gold_value -= seller.life_potion_value
