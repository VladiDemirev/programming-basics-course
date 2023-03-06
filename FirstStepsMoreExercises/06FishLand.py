mackerel_cost_kg = float(input())
sprat_cost_kg = float(input())
bonito_quantity_kg = float(input())
scad_quantity_kg = float(input())
mussels_quantity_kg = int(input())

bonito_cost_kg = mackerel_cost_kg * 1.6
scad_cost_kg = sprat_cost_kg * 1.8

MUSSELS_COST_KG = 7.50

bill = (bonito_cost_kg * bonito_quantity_kg) \
       + (scad_cost_kg * scad_quantity_kg) \
       + (mussels_quantity_kg * MUSSELS_COST_KG)

print(f"{bill:.2f}")