def validate_input(business_type, target_audience, problem_statement, budget,
                   business_stage=None, known_competitors=None, biggest_challenge=None,
                   company_name=None, usp=None, location=None):
    errors = []
    
    if not business_type or len(business_type) < 3:
        errors.append('Business type must be at least 3 characters')
    
    if not target_audience or len(target_audience) < 5:
        errors.append('Target audience must be at least 5 characters')
    
    if not problem_statement or len(problem_statement) < 10:
        errors.append('Problem statement must be at least 10 characters')
    
    if not budget or len(budget) < 2:
        errors.append('Budget is required')
    
    if len(business_type) > 255:
        errors.append('Business type is too long')
    
    if len(target_audience) > 500:
        errors.append('Target audience is too long')
    
    if len(problem_statement) > 5000:
        errors.append('Problem statement is too long')
    
    if len(budget) > 100:
        errors.append('Budget is too long')
    
    if business_stage and len(business_stage) > 100:
        errors.append('Business stage is too long')
    
    if known_competitors and len(known_competitors) > 1000:
        errors.append('Known competitors is too long')
    
    if biggest_challenge and len(biggest_challenge) > 1000:
        errors.append('Biggest challenge is too long')
        
    if company_name and len(company_name) > 255:
        errors.append('Company name is too long')
        
    if usp and len(usp) > 1000:
        errors.append('USP is too long')
        
    if location and len(location) > 255:
        errors.append('Location is too long')
    
    return errors
