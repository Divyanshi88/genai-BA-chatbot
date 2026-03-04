from flask import Blueprint, render_template, request, jsonify, send_file
import io
from app import db
from app.models import StrategyReport
from app.gemini_service import generate_business_strategy
from app.validators import validate_input
from app.export_service import export_report_as_docx, export_report_as_pdf

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/generate-strategy', methods=['POST'])
def generate_strategy():
    try:
        data = request.get_json()
        
        business_type = data.get('business_type', '').strip()
        company_name = data.get('company_name', '').strip()
        target_audience = data.get('target_audience', '').strip()
        problem_statement = data.get('problem_statement', '').strip()
        budget = data.get('budget', '').strip()
        business_stage = data.get('business_stage', '').strip()
        known_competitors = data.get('known_competitors', '').strip()
        biggest_challenge = data.get('biggest_challenge', '').strip()
        usp = data.get('usp', '').strip()
        location = data.get('location', '').strip()
        
        errors = validate_input(business_type, target_audience, problem_statement, budget,
                                business_stage, known_competitors, biggest_challenge,
                                company_name, usp, location)
        if errors:
            return jsonify({'success': False, 'errors': errors}), 400
        
        strategy_result = generate_business_strategy(
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
        
        # Format growth plan for DB storage
        growth_plan = strategy_result.get('growth_plan', {})
        growth_plan_text = f"Short Term: {growth_plan.get('short_term', '')}\nMid Term: {growth_plan.get('mid_term', '')}\nLong Term: {growth_plan.get('long_term', '')}"
        
        # Format key strategies for DB storage
        key_strategies = strategy_result.get('key_strategies', [])
        key_strategies_text = "\n".join([f"- {s}" for s in key_strategies])
        
        report = StrategyReport(
            company_name=company_name,
            business_type=business_type,
            target_audience=target_audience,
            problem_statement=problem_statement,
            budget=budget,
            usp=usp,
            location=location,
            strategy=strategy_result.get('positioning'),
            marketing_plan=key_strategies_text,
            revenue_model=strategy_result.get('budget_focus'),
            risk_analysis=growth_plan_text,
            competitor_insights=strategy_result.get('executive_summary'),
            full_report=strategy_result.get('full_report')
        )
        
        db.session.add(report)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': report.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@bp.route('/api/reports', methods=['GET'])
def get_reports():
    try:
        reports = StrategyReport.query.order_by(StrategyReport.created_at.desc()).all()
        return jsonify({
            'success': True,
            'data': [report.to_dict() for report in reports]
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@bp.route('/api/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    try:
        report = StrategyReport.query.get_or_404(report_id)
        return jsonify({
            'success': True,
            'data': report.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Report not found or error occurred: {str(e)}'
        }), 404

@bp.route('/api/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    try:
        report = StrategyReport.query.get_or_404(report_id)
        db.session.delete(report)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Report deleted successfully'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@bp.route('/api/reports/<int:report_id>/export/docx', methods=['GET'])
def export_report_docx(report_id):
    """Export a report as DOCX file."""
    try:
        report = StrategyReport.query.get_or_404(report_id)
        report_data = report.to_dict()
        
        docx_bytes = export_report_as_docx(report_data)
        
        filename = f"strategy-report-{report_id}.docx"
        
        return send_file(
            io.BytesIO(docx_bytes),
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Export failed: {str(e)}'
        }), 500

@bp.route('/api/reports/<int:report_id>/export/pdf', methods=['GET'])
def export_report_pdf(report_id):
    """Export a report as PDF file."""
    try:
        report = StrategyReport.query.get_or_404(report_id)
        report_data = report.to_dict()
        
        pdf_bytes = export_report_as_pdf(report_data)
        
        filename = f"strategy-report-{report_id}.pdf"
        
        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Export failed: {str(e)}'
        }), 500
