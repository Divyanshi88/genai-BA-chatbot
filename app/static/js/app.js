// StrategyAI - Modern Frontend Logic

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    const form = document.getElementById('strategyForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
    
    // Initialize theme toggle
    initThemeToggle();
    
    // Initialize tabs
    initTabs();
    
    // Load previous reports
    loadPreviousReports();
}

// ===== Theme Toggle =====
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;
    
    // Check saved preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    }
    
    toggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'light' ? 'dark' : 'light';
        
        if (next === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'dark');
        }
    });
}

// ===== Tab Navigation =====
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabName = btn.dataset.tab;
            
            // Remove active class from all buttons and panels
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            
            // Add active class to clicked button and corresponding panel
            btn.classList.add('active');
            document.getElementById(`panel-${tabName}`).classList.add('active');
        });
    });
}

// ===== Form Handling =====
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const companyName = document.getElementById('companyName').value.trim();
    const location = document.getElementById('location').value.trim();
    const usp = document.getElementById('usp').value.trim();
    const businessType = document.getElementById('businessType').value.trim();
    const targetAudience = document.getElementById('targetAudience').value.trim();
    const problemStatement = document.getElementById('problemStatement').value.trim();
    const budget = document.getElementById('budget').value.trim();
    const businessStage = document.getElementById('businessStage').value.trim();
    const knownCompetitors = document.getElementById('knownCompetitors') ? document.getElementById('knownCompetitors').value.trim() : '';
    const biggestChallenge = document.getElementById('biggestChallenge') ? document.getElementById('biggestChallenge').value.trim() : '';
    
    clearErrors();
    
    try {
        const submitBtn = document.getElementById('submitBtn');
        setLoadingState(submitBtn, true);
        
        const response = await fetch('/api/generate-strategy', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                company_name: companyName,
                location: location,
                usp: usp,
                business_type: businessType,
                target_audience: targetAudience,
                problem_statement: problemStatement,
                budget: budget,
                business_stage: businessStage,
                known_competitors: knownCompetitors,
                biggest_challenge: biggestChallenge
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            if (data.errors) {
                displayErrors(data.errors);
            } else {
                displayErrors([data.error || 'An error occurred']);
            }
            setLoadingState(submitBtn, false);
            return;
        }
        
        // Show results
        displayResults(data.data);
        loadPreviousReports();
        
        setLoadingState(submitBtn, false);
        
    } catch (error) {
        displayErrors(['Network error: ' + error.message]);
        const submitBtn = document.getElementById('submitBtn');
        setLoadingState(submitBtn, false);
    }
}

function setLoadingState(btn, loading) {
    const btnText = btn.querySelector('.btn-text');
    const btnLoading = btn.querySelector('.btn-loading');
    
    if (loading) {
        btn.disabled = true;
        if (btnText) btnText.style.display = 'none';
        if (btnLoading) btnLoading.style.display = 'flex';
    } else {
        btn.disabled = false;
        if (btnText) btnText.style.display = 'inline';
        if (btnLoading) btnLoading.style.display = 'none';
    }
}

function displayErrors(errors) {
    const container = document.getElementById('errorMessages');
    container.innerHTML = '<ul>' + errors.map(err => `<li>${escapeHtml(err)}</li>`).join('') + '</ul>';
    container.style.display = 'block';
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        container.style.display = 'none';
    }, 5000);
}

function clearErrors() {
    const container = document.getElementById('errorMessages');
    container.style.display = 'none';
    container.innerHTML = '';
}

// ===== Results Display =====
function displayResults(report) {
    // Parse JSON if needed
    let parsedReport = JSON.parse(JSON.stringify(report));
    
    if (typeof report.full_report === 'string' && report.full_report.trim().startsWith('{')) {
        try {
            parsedReport = JSON.parse(report.full_report);
            parsedReport.business_type = report.business_type;
            parsedReport.target_audience = report.target_audience;
            parsedReport.budget = report.budget;
            parsedReport.id = report.id; // Preserve ID for PDF download
        } catch (e) {
            console.log('JSON parse failed');
        }
    }
    
    // Display sections with new structure mapping
    displaySummarySection(parsedReport);
    
    // Strategy Panel: Positioning + Key Strategies
    const strategyHtml = `
        <div class="personalization-badge">
            ${parsedReport.company_name ? `<span>🏢 ${escapeHtml(parsedReport.company_name)}</span>` : ''}
            ${parsedReport.location ? `<span>📍 ${escapeHtml(parsedReport.location)}</span>` : ''}
        </div>
        <h3>Strategic Positioning</h3>
        <p>${formatMarkdown(parsedReport.positioning || '')}</p>
        ${parsedReport.usp ? `<h3>Unique Selling Proposition</h3><p>${formatMarkdown(parsedReport.usp)}</p>` : ''}
        <h3>Core Target Audience</h3>
        <p>${formatMarkdown(parsedReport.target_customers || '')}</p>
        <h3>Key Performance Indicators</h3>
        <ul>
            ${(parsedReport.kpis || []).map(kpi => `<li>${escapeHtml(kpi)}</li>`).join('')}
        </ul>
    `;
    displayStrategySection(strategyHtml);
    
    // Marketing Panel: Key Strategies
    const marketingHtml = `
        <h3>Actionable Strategies</h3>
        <ul>
            ${(parsedReport.key_strategies || []).map(s => `<li>${formatMarkdown(s)}</li>`).join('')}
        </ul>
    `;
    displayMarketingSection(marketingHtml);
    
    // Revenue Panel: Budget Focus
    displayRevenueSection(parsedReport.budget_focus || '');

    // SWOT Panel
    displaySwotSection(parsedReport.swot_analysis || {});
    
    // Risks Panel: KPIs + Next Steps (or just Next Steps as risks/mitigation)
    const riskHtml = `
        <h3>Key Success Metrics</h3>
        <ul>
            ${(parsedReport.kpis || []).map(kpi => `<li>${escapeHtml(kpi)}</li>`).join('')}
        </ul>
        <h3>Critical Next Steps</h3>
        <ul>
            ${(parsedReport.next_steps || []).map(step => `<li>${escapeHtml(step)}</li>`).join('')}
        </ul>
    `;
    displayRiskSection(riskHtml);
    
    // Competitor Panel: Executive Summary + Positioning
    const competitorHtml = `
        <h3>Market Positioning</h3>
        <p>${formatMarkdown(parsedReport.positioning || '')}</p>
    `;
    displayCompetitorSection(competitorHtml);
    
    // Roadmap Panel: Growth Plan + Next Steps
    const growth = parsedReport.growth_plan || {};
    const roadmapHtml = `
        <div class="roadmap-container">
            <div class="roadmap-item">
                <div class="roadmap-dot short"></div>
                <h4>Short Term (1-30 Days)</h4>
                <p>${formatMarkdown(growth.short_term || '')}</p>
            </div>
            <div class="roadmap-item">
                <div class="roadmap-dot mid"></div>
                <h4>Mid Term (2-6 Months)</h4>
                <p>${formatMarkdown(growth.mid_term || '')}</p>
            </div>
            <div class="roadmap-item">
                <div class="roadmap-dot long"></div>
                <h4>Long Term (6+ Months)</h4>
                <p>${formatMarkdown(growth.long_term || '')}</p>
            </div>
        </div>
        <h3>Immediate Action Items</h3>
        <ul>
            ${(parsedReport.next_steps || []).map(step => `<li>${escapeHtml(step)}</li>`).join('')}
        </ul>
    `;
    displayRoadmapSection(roadmapHtml);
    
    // Show results section
    const inputSection = document.getElementById('inputSection');
    const resultsSection = document.getElementById('resultsSection');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const resultsContent = document.getElementById('resultsContent');
    
    // Show loading first
    inputSection.style.display = 'none';
    resultsSection.style.display = 'block';
    loadingSpinner.style.display = 'block';
    resultsContent.style.display = 'none';
    
    // Simulate AI thinking time for better UX
    setTimeout(() => {
        loadingSpinner.style.display = 'none';
        resultsContent.style.display = 'block';
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 1500);
    
    // Store current report for download
    window.currentReport = parsedReport;
}

// ===== Summary Section =====
function displaySummarySection(report) {
    const summaryContent = document.getElementById('summaryContent');
    const highlightsList = document.getElementById('highlightsList');
    
    // Display executive summary
    if (report.executive_summary) {
        summaryContent.innerHTML = `<p>${formatMarkdown(report.executive_summary)}</p>`;
    } else if (report.summary) {
        summaryContent.innerHTML = `<p>${formatMarkdown(report.summary)}</p>`;
    } else {
        summaryContent.innerHTML = '<p class="empty-state">No summary available</p>';
    }
    
    // Display key highlights using key strategies or other fields
    const highlights = [];
    if (report.target_customers) highlights.push(`Target: ${report.target_customers.substring(0, 60)}...`);
    if (report.budget_focus) highlights.push(`Budget: ${report.budget_focus.substring(0, 60)}...`);
    if (report.next_steps && report.next_steps.length > 0) highlights.push(`Next: ${report.next_steps[0]}`);
    
    if (highlights.length > 0) {
        const icons = ['🎯', '💰', '🚀'];
        highlightsList.innerHTML = highlights.map((highlight, index) => `
            <div class="highlight-card">
                <span class="highlight-icon">${icons[index % icons.length]}</span>
                <span class="highlight-text">${escapeHtml(highlight)}</span>
            </div>
        `).join('');
    } else {
        highlightsList.innerHTML = '';
    }
}

// ===== Strategy Section =====
function displayStrategySection(content) {
    const container = document.getElementById('strategyContent');
    if (!content) {
        container.innerHTML = '<div class="empty-state">No strategy data available</div>';
        return;
    }
    container.innerHTML = content.includes('</h3>') ? content : formatMarkdown(content);
}

// ===== Marketing Section =====
function displayMarketingSection(content) {
    const container = document.getElementById('marketingContent');
    if (!content) {
        container.innerHTML = '<div class="empty-state">No marketing data available</div>';
        return;
    }
    container.innerHTML = content.includes('</h3>') ? content : formatMarkdown(content);
}

// ===== Revenue Section =====
function displayRevenueSection(content) {
    const container = document.getElementById('revenueContent');
    if (!content) {
        container.innerHTML = '<div class="empty-state">No revenue data available</div>';
        return;
    }
    container.innerHTML = content.includes('</h3>') ? content : formatMarkdown(content);
}

// ===== Risk Section =====
function displayRiskSection(content) {
    const container = document.getElementById('riskContent');
    if (!content) {
        container.innerHTML = '<div class="empty-state">No risk data available</div>';
        return;
    }
    container.innerHTML = content.includes('</h3>') ? content : formatMarkdown(content);
}

// ===== Competitor Section =====
function displayCompetitorSection(content) {
    const container = document.getElementById('competitorContent');
    if (!content) {
        container.innerHTML = '<div class="empty-state">No competitor data available</div>';
        return;
    }
    container.innerHTML = content.includes('</h3>') ? content : formatMarkdown(content);
}

// ===== SWOT Section =====
function displaySwotSection(swot) {
    const strengthsList = document.getElementById('swotStrengths');
    const weaknessesList = document.getElementById('swotWeaknesses');
    const opportunitiesList = document.getElementById('swotOpportunities');
    const threatsList = document.getElementById('swotThreats');
    
    if (!strengthsList) return;
    
    strengthsList.innerHTML = (swot.strengths || []).map(s => `<li>${escapeHtml(s)}</li>`).join('');
    weaknessesList.innerHTML = (swot.weaknesses || []).map(w => `<li>${escapeHtml(w)}</li>`).join('');
    opportunitiesList.innerHTML = (swot.opportunities || []).map(o => `<li>${escapeHtml(o)}</li>`).join('');
    threatsList.innerHTML = (swot.threats || []).map(t => `<li>${escapeHtml(t)}</li>`).join('');
}

// ===== Roadmap Section =====
function displayRoadmapSection(content) {
    const container = document.getElementById('roadmapContent');
    if (!content) {
        container.innerHTML = '<div class="empty-state">No roadmap data available</div>';
        return;
    }
    container.innerHTML = content.includes('</h3>') ? content : formatMarkdown(content);
}

// ===== Markdown Formatter =====
function formatMarkdown(text) {
    if (!text) return '';
    
    // Escape HTML first
    let html = escapeHtml(text);
    
    // Headers
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h3>$1</h3>');
    
    // Bold
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    
    // Process line by line
    const lines = html.split('\n');
    let result = [];
    let inList = false;
    
    lines.forEach(line => {
        const trimmed = line.trim();
        
        // Skip if it's just an empty line after a header
        if (trimmed === '' && !inList) {
            return;
        }
        
        // Nested list item
        if (/^\s+[-\*]/.test(trimmed)) {
            if (!inList) {
                result.push('<ul>');
                inList = true;
            }
            result.push(`<li>${trimmed.replace(/^\s+[-\*]\s*/, '')}</li>`);
            return;
        }
        
        // Close list if open
        if (inList) {
            result.push('</ul>');
            inList = false;
        }
        
        // Regular bullet
        if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
            result.push(`<ul><li>${trimmed.substring(2)}</li></ul>`);
        } else if (trimmed) {
            result.push(`<p>${trimmed}</p>`);
        }
    });
    
    if (inList) {
        result.push('</ul>');
    }
    
    return result.join('');
}

// ===== Risk Extraction =====
function extractRisks(text) {
    const risks = [];
    if (!text) return risks;
    
    const lines = text.split('\n');
    const keywords = {
        high: ['high', 'critical', 'major', 'severe', 'significant'],
        medium: ['medium', 'moderate', 'concern'],
        low: ['low', 'minor', 'small', 'minimal']
    };
    
    lines.forEach(line => {
        const trimmed = line.trim();
        if (trimmed.length > 20 && (trimmed.startsWith('-') || trimmed.startsWith('*') || trimmed.toLowerCase().includes('risk'))) {
            let level = 'medium';
            const lower = trimmed.toLowerCase();
            
            if (keywords.high.some(k => lower.includes(k))) level = 'high';
            else if (keywords.low.some(k => lower.includes(k))) level = 'low';
            
            const percentage = level === 'high' ? 85 : level === 'medium' ? 55 : 25;
            let name = trimmed.replace(/^[-\*]\s*/, '').split('(')[0].trim();
            
            risks.push({
                name: name.substring(0, 50),
                level: level,
                percentage: percentage
            });
        }
    });
    
    return risks.slice(0, 4);
}

// ===== Copy to Clipboard =====
function copySection(elementId) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const text = element.innerText;
    
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!');
    }).catch(() => {
        showToast('Failed to copy');
    });
}

function showToast(message) {
    // Remove existing toast
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();
    
    // Create new toast
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    // Show toast
    setTimeout(() => toast.classList.add('show'), 10);
    
    // Hide after 2 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 2000);
}

// ===== Previous Reports =====
async function loadPreviousReports() {
    try {
        const response = await fetch('/api/reports');
        const data = await response.json();
        
        if (data.success && data.data.length > 0) {
            displayPreviousReports(data.data);
        } else {
            document.getElementById('previousReports').style.display = 'none';
        }
    } catch (error) {
        console.error('Error loading reports:', error);
    }
}

function displayPreviousReports(reports) {
    const section = document.getElementById('previousReports');
    const list = document.getElementById('reportsList');
    
    list.innerHTML = reports.map(report => `
        <div class="report-item" onclick="viewReport(${report.id})">
            <div class="report-info">
                <div class="report-title">${escapeHtml(report.company_name || report.business_type)}</div>
                <div class="report-meta">
                    <span>🏢 ${escapeHtml(report.business_type)}</span>
                    <span>👥 ${escapeHtml(report.target_audience.substring(0, 20))}...</span>
                    <span>💰 ${escapeHtml(report.budget)}</span>
                    <span>📅 ${formatDate(report.created_at)}</span>
                </div>
            </div>
            <div class="report-actions">
                <button class="btn-delete" onclick="event.stopPropagation(); deleteReport(${report.id})">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');
    
    section.style.display = 'block';
}

async function viewReport(reportId) {
    try {
        const response = await fetch(`/api/reports/${reportId}`);
        const data = await response.json();
        
        if (data.success) {
            displayResults(data.data);
        }
    } catch (error) {
        console.error('Error loading report:', error);
    }
}

async function deleteReport(reportId) {
    if (!confirm('Delete this strategy?')) return;
    
    try {
        const response = await fetch(`/api/reports/${reportId}`, {
            method: 'DELETE'
        });
        
        const data = await response.json();
        
        if (data.success) {
            loadPreviousReports();
            showToast('Strategy deleted');
        }
    } catch (error) {
        console.error('Error deleting report:', error);
    }
}

// ===== Reset Form =====
function resetForm() {
    const inputSection = document.getElementById('inputSection');
    const resultsSection = document.getElementById('resultsSection');
    const form = document.getElementById('strategyForm');
    
    form.reset();
    resultsSection.style.display = 'none';
    inputSection.style.display = 'block';
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ===== Download Report =====
async function downloadReport() {
    if (!window.currentReport || !window.currentReport.id) {
        showToast('Please generate a report first');
        return;
    }
    
    const reportId = window.currentReport.id;
    const downloadBtn = document.querySelector('.btn-download');
    
    try {
        if (downloadBtn) {
            downloadBtn.disabled = true;
            downloadBtn.innerHTML = '<span>⌛ Generating PDF...</span>';
        }
        
        const response = await fetch(`/api/reports/${reportId}/export/pdf`);
        
        if (!response.ok) {
            throw new Error('Export failed');
        }
        
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Business-Strategy-Report-${reportId}.pdf`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
        showToast('PDF downloaded successfully!');
    } catch (error) {
        console.error('Download error:', error);
        showToast('Failed to download PDF. Please try again.');
    } finally {
        if (downloadBtn) {
            downloadBtn.disabled = false;
            downloadBtn.innerHTML = '<span>📄 Download PDF Report</span>';
        }
    }
}

// ===== Utilities =====
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

