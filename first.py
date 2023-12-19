def make_juice(fruit):
    return f"{fruit}+🍹"
    
def add_ice(juice):
    return f"{juice}+🧊"

def add_suger(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_suger(cold_juice)

print(perfect_juice)