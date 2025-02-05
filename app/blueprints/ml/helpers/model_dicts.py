from app.blueprints.ml.services.dashboard_data import monomers_raw, units_raw, pp_raw

# Unit UUID to name    
units_dict = {str(unit['uuid']) : unit['symbol'] for unit in units_raw}


# Property UUID to name
properties_dict = {}
for item in pp_raw:
    properties_dict[str(item['uuid'])] = {
        'name': item['name'],
        'short_name': item['short_name']
    }
    

# Monomer UUID to name
monomers_dict = {str(monomer_uuid) : name for name,monomer_uuid in monomers_raw}
