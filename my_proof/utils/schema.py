import json
import os
import logging
from typing import Dict, Any, Tuple

import jsonschema

def validate_schema(input_data: Dict[str, Any]) -> Tuple[str, bool]:
    """
    Validate input data against the Google profile schema using jsonschema.
    
    Args:
        input_data: The JSON data to validate
        
    Returns:
        tuple[str, bool]: A tuple containing (schema_type, is_valid)
        where schema_type is 'google-profile.json'
        and is_valid indicates if the schema validation passed
    """
    try:
        # schema_type = 'google-profile.json'
        schema_type = 'fhir-patient.json'
        
        # Load the schema
        schema_path = os.path.join(os.path.dirname(__file__), '..', 'schemas', schema_type)
        with open(schema_path, 'r') as f:
            schema = json.load(f)
            
        # Validate against schema
        jsonschema.validate(instance=input_data, schema=schema)
        return schema_type, True
        
    except jsonschema.exceptions.ValidationError as e:
        logging.error(f"Schema validation error: {str(e)}")
        return schema_type, False
    except Exception as e:
        logging.error(f"Schema validation failed: {str(e)}")
        return schema_type, False
