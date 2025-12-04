from flask import Flask, render_template, jsonify
import os
import json
from pathlib import Path

app = Flask(__name__)

# Directory to store visualization configurations
VISUALIZATIONS_DIR = Path('visualizations')
VISUALIZATIONS_DIR.mkdir(exist_ok=True)

def get_all_visualizations():
    """Get metadata for all available visualizations"""
    visualizations = []
    for file in VISUALIZATIONS_DIR.glob('*.json'):
        try:
            with open(file, 'r') as f:
                viz_data = json.load(f)
                visualizations.append({
                    'id': file.stem,
                    'title': viz_data.get('title', file.stem),
                    'description': viz_data.get('description', ''),
                })
        except Exception as e:
            print(f"Error loading {file}: {e}")
    return sorted(visualizations, key=lambda x: x['title'])

@app.route('/')
def index():
    """Homepage showing all available visualizations"""
    visualizations = get_all_visualizations()
    return render_template('index.html', visualizations=visualizations)

@app.route('/viz/<viz_id>')
def visualization(viz_id):
    """Display a specific visualization"""
    viz_file = VISUALIZATIONS_DIR / f'{viz_id}.json'

    if not viz_file.exists():
        return "Visualization not found", 404

    with open(viz_file, 'r') as f:
        viz_data = json.load(f)

    return render_template('visualization.html',
                         viz_id=viz_id,
                         title=viz_data.get('title', viz_id),
                         description=viz_data.get('description', ''))

@app.route('/embed/<viz_id>')
def embedded_visualization(viz_id):
    """Display visualization without header/footer for embedding"""
    viz_file = VISUALIZATIONS_DIR / f'{viz_id}.json'

    if not viz_file.exists():
        return "Visualization not found", 404

    with open(viz_file, 'r') as f:
        viz_data = json.load(f)

    return render_template('embedded.html',
                         viz_id=viz_id,
                         title=viz_data.get('title', viz_id))

@app.route('/api/viz/<viz_id>')
def get_visualization_data(viz_id):
    """API endpoint to get visualization data as JSON"""
    viz_file = VISUALIZATIONS_DIR / f'{viz_id}.json'

    if not viz_file.exists():
        return jsonify({'error': 'Visualization not found'}), 404

    with open(viz_file, 'r') as f:
        viz_data = json.load(f)

    return jsonify(viz_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
