#!/bin/bash

echo "🚀 Business Strategy Generator Setup"
echo "======================================"
echo ""

if command -v python3 &> /dev/null; then
    echo "✓ Python 3 found"
    python3 --version
else
    echo "✗ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "⚙️ Setting up environment variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file from .env.example"
    echo ""
    echo "⚠️  Please edit .env file and add your Google Cloud Project ID:"
    echo "   - Open .env and set GOOGLE_CLOUD_PROJECT_ID"
    echo "   - Make sure you have Google Cloud Vertex AI API enabled"
    echo "   - Ensure you have valid credentials configured"
else
    echo "✓ .env file already exists"
fi

echo ""
echo "✓ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Edit .env and add your Google Cloud Project ID"
echo "   2. Ensure you have GCP credentials configured:"
echo "      export GOOGLE_APPLICATION_CREDENTIALS=business-strategy-generator/sales-insights-gcp-c21ac32e454d.json"
echo "   3. Run the app: python3 run.py"
echo "   4. Open http://localhost:5000 in your browser"
echo ""
