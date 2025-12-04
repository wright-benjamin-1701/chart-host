# Chart Host

A lightweight Flask application for hosting interactive data visualizations using Plotly.js. Perfect for embedding charts into blog posts and documentation.

## Features

- **Homepage Gallery**: Browse all your visualizations in one place
- **Iframe-Ready**: Each chart has its own URL, perfect for embedding
- **Interactive Charts**: Powered by Plotly.js with hover, zoom, and pan capabilities
- **Easy Deployment**: Deploy to Heroku with automatic updates on git push
- **Simple JSON Configuration**: Add charts by creating JSON files

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Visit `http://localhost:5000` to see your gallery

### Deploy to Heroku

1. Create a new Heroku app:
```bash
heroku create your-chart-host-name
```

2. Deploy:
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

3. Open your app:
```bash
heroku open
```

## Adding Visualizations

Create JSON files in the `visualizations/` directory. Each file should follow this structure:

```json
{
  "title": "My Chart Title",
  "description": "A brief description of what this chart shows",
  "data": [
    {
      "x": [1, 2, 3, 4, 5],
      "y": [10, 20, 15, 25, 30],
      "type": "scatter",
      "mode": "lines+markers"
    }
  ],
  "layout": {
    "title": "Chart Title",
    "xaxis": {"title": "X Axis Label"},
    "yaxis": {"title": "Y Axis Label"}
  },
  "config": {
    "responsive": true,
    "displayModeBar": true,
    "displaylogo": false
  }
}
```

### Plotly.js Format

The JSON files follow the [Plotly.js JSON schema](https://plotly.com/javascript/). The main components are:

- **title**: Chart title shown in the gallery
- **description**: Brief description for the gallery card
- **data**: Array of trace objects (your actual data and chart type)
- **layout**: Chart layout configuration (titles, axes, styling)
- **config**: Plotly configuration options

### Chart Types

Plotly.js supports many chart types:
- Line charts (`type: "scatter"`, `mode: "lines"`)
- Scatter plots (`type: "scatter"`, `mode: "markers"`)
- Bar charts (`type: "bar"`)
- Pie charts (`type: "pie"`)
- And many more...

See the [Plotly.js documentation](https://plotly.com/javascript/) for all available options.

## Migrating from Chart Studio

If you're migrating from Chart Studio:

1. Export your data as CSV from Chart Studio
2. Recreate the chart configuration in Plotly.js JSON format
3. Save as a `.json` file in the `visualizations/` directory
4. The filename (without `.json`) becomes the chart's URL slug

## Embedding in Blog Posts

From the homepage, click "Copy Embed Code" for any visualization to get an iframe snippet:

```html
<iframe src="https://your-app.herokuapp.com/viz/chart-name"
        width="100%"
        height="600"
        frameborder="0">
</iframe>
```

## Project Structure

```
chart-host/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Procfile               # Heroku process configuration
├── runtime.txt            # Python version for Heroku
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html         # Homepage gallery
│   └── visualization.html # Individual chart view
├── static/
│   └── css/
│       └── style.css      # Styling
└── visualizations/        # Your chart JSON files
    ├── example-line-chart.json
    └── example-bar-chart.json
```

## API Endpoints

- `GET /` - Homepage with gallery of all visualizations
- `GET /viz/<viz_id>` - View a specific visualization (for embedding)
- `GET /api/viz/<viz_id>` - Get raw JSON data for a visualization

## License

MIT License - See LICENSE file for details
