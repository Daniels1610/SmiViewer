from collections import defaultdict
import re, datetime
import json

from dashboard_data import (all_models_raw, monomers_raw, pp_raw, units_raw)
from cleaners import (_clean_model_steps, _clean_stringified_dict)

def get_dashboard_data() -> defaultdict: 
    '''
        Gets model's results to display on Dashboard

        Dataset Structure:
        - status
        - property
        - dataset
        - run_id
        - monomer_counts 
        - features
        - rows 
        - steps

        Model Metrics:
        - y_max
        - y_min 
        - y_mean
        - mae
        - mae_std
        - mape, 
        - mape_std,
        - rmse
        - rmse_std
        - s3_location
        - start_time
        - units 
    '''

    unique_properties = set()
    unique_units = set()
    
    def init_model_metrics():
        return {
            'y_max':None,
            'y_min':None,
            'y_mean':None,
            'mae':None,
            'mae_std':None,
            'mape':None,
            'mape_std':None,
            'rmse':None,
            'rmse_std':None
        }
    all_models = defaultdict(lambda: {
        'name':None,
        'dev': None,
        'prod': None,
        's3_location':None,
        'properties':[],
        'model_type':None,
        'rows':None,
        'steps':None,
        'dataset':None,
        'features':None,
        'start_time':None
    })
    
    for (
        status, property, dataset, run_id, monomer_counts,features, rows, steps, 
        y_max, y_min, y_mean, mae, mae_std, mape, mape_std,rmse, rmse_std, 
        s3_location, start_time, units 
        ) in all_models_raw:
        

        # Clean data 
        # Previous RegEx: (?<=model', )\w+(?=\()
        stringify_steps = ''.join(str(e) for e in steps)
        stringify_monomer = json.dumps(monomer_counts)
        
        model_match = re.search(r"(?<=\('model', ')[^(\r\n]+", stringify_steps)
        steps = _clean_model_steps(stringify_steps)
        monomer_counts = _clean_stringified_dict(stringify_monomer)

        # Storage for query
        unique_properties.add(property)
        unique_units.add(units)
        
        # Process data
        run_data = all_models[run_id]

        if property not in run_data['properties']:
            run_data['properties'].append(property)
                                
        run_data['s3_location'] = s3_location
        run_data['dataset_size'] = rows
        run_data['steps'] = steps
        run_data['model_type'] = model_match.group()
        run_data['dataset'] = dataset.upper()
        run_data['features'] = features
        run_data['monomer_counts'] = monomer_counts
        run_data['units'] = units
        run_data['creation_date'] = datetime.datetime.fromtimestamp(start_time / 1000).strftime('%d/%m/%y %H:%M') # Convert the Unix timestamp from milliseconds to seconds then to to a datetime object
        
        if run_data[status] is None:
            run_data[status] = init_model_metrics()
        
        status_data = run_data[status]
        
        status_data['y_max'] = round(y_max, 4)
        status_data['y_min'] = round(y_min, 4)
        status_data['y_mean'] = round(y_mean, 4)
        status_data['mae'] = round(mae, 4)
        status_data['mae_std'] = round(mae_std, 4)
        status_data['mape'] = round(mape, 4)
        status_data['mape_std'] = round(mape_std, 4)
        status_data['rmse'] = round(rmse, 4)
        status_data['rmse_std'] = round(rmse_std, 4)
        
        
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
    
    for model_details in all_models.values():
        # Units
        model_details['units'] = units_dict[ str(model_details['units']) ] # replace the uuid with the symbol

        # Properties
        model_properties = []
        for property in model_details['properties']:
            model_properties.append(properties_dict[str(property)])
        
        model_details['properties'] = model_properties
        model_details['name'] = '+'.join([property['short_name'] for property in model_properties ])# Assign readable names to each run
        model_details['complete_name'] = '+'.join([property['name'] for property in model_properties ])# Assign readable names to each run
        
        # Monomer
        if not model_details['monomer_counts']:
            continue
        
        model_monomer_counts = {}
        for monomer_uuid, count in model_details['monomer_counts'].items():
            model_monomer_counts[ monomers_dict[monomer_uuid] ] = {'count':count, 'uuid':monomer_uuid}
        model_details['monomer_counts'] = model_monomer_counts
        
    return all_models
    


if (__name__ == '__main__'):
    amodels = get_dashboard_data()
    print(f'ALL MODELS: {amodels}')