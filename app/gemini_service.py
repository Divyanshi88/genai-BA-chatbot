"""
Business Strategy Generator - Gemini Service
Production-ready AI service with robust JSON extraction and retry logic.
"""

import json
import re
import os
import random
from typing import Dict, Any, Optional

from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# Load environment variables
load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
LOCATION = "us-central1"
MODEL_ID = "gemini-2.0-flash-001"

# Max retries for JSON parsing failures
MAX_RETRIES = 2

# Required fields that must always be present
REQUIRED_FIELDS = [
    "executive_summary",
    "target_customers",
    "positioning",
    "swot_analysis",
    "key_strategies",
    "growth_plan",
    "budget_focus",
    "kpis",
    "next_steps"
]


def initialize_vertex_ai() -> None:
    """Initialize Vertex AI with project credentials."""
    if not PROJECT_ID:
        raise ValueError("GOOGLE_CLOUD_PROJECT_ID is not set in .env file")
    
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION
    )


def build_input_context(business_type: str, target_audience: str,
                         problem_statement: str, budget: str,
                         business_stage: str, known_competitors: str,
                         biggest_challenge: str, company_name: str = "",
                         usp: str = "", location: str = "") -> str:
    """
    Build a structured input context block for better grounding.
    This ensures all outputs reference the provided inputs directly.
    """
    competitor_info = known_competitors if known_competitors else "Not specified"
    challenge_info = biggest_challenge if biggest_challenge else "Not specified"
    stage_info = business_stage if business_stage else "Not specified"
    name_info = company_name if company_name else "Not specified"
    usp_info = usp if usp else "Not specified"
    location_info = location if location else "Not specified"
    
    return f"""Company Name: {name_info}
Business Type: {business_type}
Location/Geography: {location_info}
Unique Selling Proposition (USP): {usp_info}
Target Audience: {target_audience}
Problem Solved: {problem_statement}
Budget: {budget}
Business Stage: {stage_info}
Competitors: {competitor_info}
Main Challenge: {challenge_info}"""


def build_strategy_prompt(business_type: str, target_audience: str, 
                          problem_statement: str, budget: str,
                          business_stage: str = "", 
                          known_competitors: str = "",
                          biggest_challenge: str = "",
                          company_name: str = "",
                          usp: str = "",
                          location: str = "") -> str:
    """
    Build a comprehensive prompt for a senior business consultant AI.
    Generates specific, actionable, and structured business strategies.
    """
    
    # Build input context for grounding
    input_context = build_input_context(
        business_type, target_audience, problem_statement, budget,
        business_stage, known_competitors, biggest_challenge,
        company_name, usp, location
    )
    
    return f"""You are a world-class senior business strategist generating a HYPER-PERSONALIZED, unconventional, and extremely detailed business strategy for '{company_name or 'the business'}'.

Everything you suggest must be 100% specific to the provided inputs. Avoid generic advice like "use social media" or "create a website". Instead, name specific platforms, niche communities, specific pricing models, and direct competitive moves.

## BUSINESS INPUTS (GROUND TRUTH)

{input_context}

---

## YOUR MISSION
Develop a strategy that feels like it was written by a $500/hr consultant who has studied this specific niche for years.
1. If a location is provided, tailor all marketing and operational advice to that specific region/culture.
2. If a USP is provided, build the entire positioning around reinforcing that specific advantage.
3. Address the 'Main Challenge' with a multi-step tactical solution.
4. Directly compare the business against the 'Competitors' and suggest how to "steal" their customers.

## OUTPUT FORMAT (STRICT JSON ONLY)

Return ONLY a valid JSON object with this exact structure:

{{
  "executive_summary": "3-4 sentence summary of the core strategy, mentioning the company by name and its unique position in the market.",
  "target_customers": "Deep psychological and behavioral profile of the ideal customers.",
  "positioning": "A 'Blue Ocean' positioning strategy - how to make the competition irrelevant.",
  "swot_analysis": {{
    "strengths": ["...", "..."],
    "weaknesses": ["...", "..."],
    "opportunities": ["...", "..."],
    "threats": ["...", "..."]
  }},
  "key_strategies": [
    "Strategy 1: High-impact move focusing on the USP",
    "Strategy 2: Tactical move to solve the Biggest Challenge",
    "Strategy 3: Growth move to scale within the Budget"
  ],
  "growth_plan": {{
    "short_term": "Weeks 1-4: Exact tactical steps to get immediate results.",
    "mid_term": "Months 2-6: Steps to build a repeatable growth engine.",
    "long_term": "6+ months: Vision for dominance or expansion."
  }},
  "budget_focus": "A detailed breakdown of how to spend the {budget} budget for maximum ROI.",
  "kpis": ["Specific metric 1 (with target number)", "Specific metric 2", "Specific metric 3"],
  "next_steps": ["Action item 1 (Start today)", "Action item 2", "Action item 3"]
}}"""


def extract_json_from_response(response_text: str) -> Optional[Dict[str, Any]]:
    """
    Extract JSON from response, handling various formats:
    - Plain JSON
    - JSON wrapped in ```json ... ```
    - JSON embedded in text
    """
    if not response_text:
        return None
    
    # Clean the response
    cleaned = response_text.strip()
    
    # Try direct parse first
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    
    # Remove markdown code blocks
    cleaned = re.sub(r'^```json\s*', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'^```\s*', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'```$', '', cleaned, flags=re.MULTILINE)
    
    # Try parse after removing code blocks
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    
    # Find first JSON object using regex
    json_match = re.search(r'\{[\s\S]*\}', cleaned)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except json.JSONDecodeError:
            pass
    
    return None


def validate_and_fill_fields(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate that all required fields are present and filled.
    Fill any missing/empty fields with fallback content.
    """
    fallback_content = {
        "executive_summary": "Develop a specialized solution for your target audience by focusing on the core problem identified.",
        "target_customers": "Your primary customers are those currently experiencing the pain point described in your problem statement.",
        "positioning": "Your unique advantage lies in your specific focus and agility compared to established competitors.",
        "swot_analysis": {
            "strengths": ["Clear problem focus", "Agile decision making"],
            "weaknesses": ["Limited brand awareness", "Small initial team"],
            "opportunities": ["Unmet market needs", "Direct customer engagement"],
            "threats": ["Established competitors", "Market entry barriers"]
        },
        "key_strategies": [
            "Conduct 10 deep-dive customer interviews to validate core assumptions.",
            "Launch a minimum viable version focusing ONLY on the primary problem.",
            "Establish a direct feedback loop with early adopters."
        ],
        "growth_plan": {
            "short_term": "Focus on validation and securing your first 5-10 paying customers.",
            "mid_term": "Refine the product based on feedback and start small-scale acquisition.",
            "long_term": "Scale the proven acquisition channels and expand feature set."
        },
        "budget_focus": "Allocate 70% of budget to product validation and 30% to high-intent customer acquisition.",
        "kpis": ["Customer Validation Score > 8/10", "First 5 paying customers acquired"],
        "next_steps": ["Talk to 5 potential users today", "Draft MVP feature list", "Set up a landing page"]
    }
    
    # Ensure all required fields exist
    for field in REQUIRED_FIELDS:
        if field not in result or not result[field]:
            result[field] = fallback_content.get(field)
    
    # Nested check for growth_plan
    if "growth_plan" not in result or not isinstance(result["growth_plan"], dict):
        result["growth_plan"] = fallback_content["growth_plan"]
    else:
        for subfield in ["short_term", "mid_term", "long_term"]:
            if subfield not in result["growth_plan"] or not result["growth_plan"][subfield]:
                result["growth_plan"][subfield] = fallback_content["growth_plan"][subfield]
    
    # Ensure full_report exists
    result["full_report"] = json.dumps(result, indent=2)
    
    return result


def generate_with_retry(prompt: str, attempt: int = 0) -> Dict[str, Any]:
    """
    Generate strategy with retry logic for JSON parsing failures.
    Uses JSON mode for consistent output.
    """
    initialize_vertex_ai()
    
    model = GenerativeModel(MODEL_ID)
    
    generation_config = {
        "temperature": 0.4,  # Reduced for more consistency/accuracy
        "top_p": 0.9,
        "max_output_tokens": 3072,
        "response_mime_type": "application/json"
    }
    
    try:
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        response_text = response.text.strip() if response.text else ""
        
        # Extract JSON from response
        result = extract_json_from_response(response_text)
        
        if result is None:
            raise ValueError("Failed to extract valid JSON from response")
        
        # Validate and fill required fields
        result = validate_and_fill_fields(result)
        
        return result
        
    except Exception as e:
        print(f"[DEBUG] Attempt {attempt + 1} failed: {str(e)}")
        
        if attempt < MAX_RETRIES - 1:
            return generate_with_retry(prompt, attempt + 1)
        else:
            return get_fallback_response()


def get_fallback_response() -> Dict[str, Any]:
    """
    Return a structured fallback response when AI generation fails.
    """
    fallback = {
        "executive_summary": "Focus on validating your core value proposition with a lean approach to minimize risk and maximize learning.",
        "target_customers": "Early adopters who feel the problem most acutely and are seeking immediate solutions.",
        "positioning": "Agile, customer-centric positioning that addresses specific gaps in the current market offerings.",
        "swot_analysis": {
            "strengths": ["Agility", "Customer proximity"],
            "weaknesses": ["Low visibility", "Limited resources"],
            "opportunities": ["Niche penetration", "Viral growth potential"],
            "threats": ["Competitive reaction", "Market shifts"]
        },
        "key_strategies": [
            "Customer-led development through continuous feedback",
            "Lean MVP launch to test market resonance",
            "High-touch early customer support and onboarding"
        ],
        "growth_plan": {
            "short_term": "Validation and initial traction with 10 core users.",
            "mid_term": "Product refinement and steady user growth.",
            "long_term": "Expansion into adjacent segments and scaling operations."
        },
        "budget_focus": "Priority on customer discovery and low-cost validation techniques.",
        "kpis": ["User engagement rate", "Conversion from trial to paid"],
        "next_steps": ["Schedule discovery calls", "Define success metrics", "Build basic prototype"],
        "full_report": "{}"
    }
    fallback["full_report"] = json.dumps(fallback, indent=2)
    return fallback


def generate_business_strategy(business_type: str, target_audience: str, 
                               problem_statement: str, budget: str,
                               business_stage: str = "",
                               known_competitors: str = "",
                               biggest_challenge: str = "",
                               company_name: str = "",
                               usp: str = "",
                               location: str = "") -> Dict[str, Any]:
    """
    Main function to generate business strategy.
    Returns always-valid JSON with all required fields.
    """
    prompt = build_strategy_prompt(
        business_type=business_type,
        target_audience=target_audience,
        problem_statement=problem_statement,
        budget=budget,
        business_stage=business_stage,
        known_competitors=known_competitors,
        biggest_challenge=biggest_challenge,
        company_name=company_name,
        usp=usp,
        location=location
    )
    
    result = generate_with_retry(prompt)
    
    # Final validation to ensure no empty fields
    result = validate_and_fill_fields(result)
    
    # Set full_report to the final JSON (using correct keys)
    result["full_report"] = json.dumps({
        "executive_summary": result.get("executive_summary", ""),
        "target_customers": result.get("target_customers", ""),
        "positioning": result.get("positioning", ""),
        "swot_analysis": result.get("swot_analysis", {}),
        "key_strategies": result.get("key_strategies", []),
        "growth_plan": result.get("growth_plan", {}),
        "budget_focus": result.get("budget_focus", ""),
        "kpis": result.get("kpis", []),
        "next_steps": result.get("next_steps", [])
    }, indent=2)
    
    return result

