from app import db
from datetime import datetime
import json

class StrategyReport(db.Model):
    __tablename__ = 'strategy_reports'
    
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=True)
    business_type = db.Column(db.String(255), nullable=False)
    target_audience = db.Column(db.String(500), nullable=False)
    problem_statement = db.Column(db.Text, nullable=False)
    budget = db.Column(db.String(100), nullable=False)
    usp = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=True)
    
    strategy = db.Column(db.Text, nullable=True)
    marketing_plan = db.Column(db.Text, nullable=True)
    revenue_model = db.Column(db.Text, nullable=True)
    risk_analysis = db.Column(db.Text, nullable=True)
    competitor_insights = db.Column(db.Text, nullable=True)
    
    full_report = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'business_type': self.business_type,
            'target_audience': self.target_audience,
            'problem_statement': self.problem_statement,
            'budget': self.budget,
            'usp': self.usp,
            'location': self.location,
            'strategy': self.strategy,
            'marketing_plan': self.marketing_plan,
            'revenue_model': self.revenue_model,
            'risk_analysis': self.risk_analysis,
            'competitor_insights': self.competitor_insights,
            'full_report': self.full_report,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
