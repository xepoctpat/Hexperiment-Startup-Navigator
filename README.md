# Hexperiment Startup Navigator

AI-powered startup analysis and visualization tool built on Toolhouse SDK

## Overview

Hexperiment Startup Navigator is a comprehensive toolkit designed to help entrepreneurs, investors, and market analysts identify promising startup opportunities through data-driven market analysis. The application leverages AI through the Toolhouse SDK to gather and analyze market data, generate visualizations, and provide strategic recommendations.

## Key Features

- **Market Data Analysis**: Retrieve and analyze market size, growth rates, and competitive landscape.
- **Opportunity Identification**: Identify attractive market segments based on customizable criteria.
- **Market Gap Detection**: Discover underserved areas with high growth potential and low competition.
- **Trend Analysis**: Track and visualize market trends over time to spot emerging opportunities.
- **AI-Powered Recommendations**: Get strategic recommendations for entering specific market segments.
- **Advanced Visualizations**: Generate interactive charts and graphs to understand market dynamics.
- **Feedback Collection**: Gather and analyze user feedback to improve analysis results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hexperiment-Labs/Hexperiment-Startup-Navigator.git
   cd Hexperiment-Startup-Navigator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the project root directory
   - Add your Toolhouse API key:

     ```env
     TOOLHOUSE_API_KEY=your_api_key_here
     # Optional: Specify a custom bundle ID
     BUNDLE_ID=3710
     ```

## Required API Keys

The Hexperiment Startup Navigator requires the following API keys:

1. **Toolhouse API Key**: Required for accessing market data and generating AI-powered recommendations.
   - Register at [toolhouse.io](https://toolhouse.io) to get your API key
   - Set it as an environment variable `TOOLHOUSE_API_KEY` or in the `.env` file

2. **News API Key** (Optional): For retrieving market news in the `fetch_news_data` utility.
   - If you want to use the news functionality, sign up for a free key at [newsapi.org](https://newsapi.org)
   - Set it as an environment variable `NEWS_API_KEY` or pass it directly to the function

## Usage

### Running the Demo

To see the Startup Navigator in action, run the demo script:

```bash
python demo.py
```

### Using the Jupyter Notebook

For an interactive experience with more detailed explanations:

```bash
jupyter notebook notebooks/demo/startup_navigator_demo.ipynb
```

### Using as a Library

You can import and use components individually in your own projects:

```python
from hexperiment.agent import NavigatorAgent
from hexperiment.analysis.market_analysis import identify_market_gaps
from hexperiment.visualizations.market_charts import create_growth_vs_size_chart

# Initialize agent with your API key
agent = NavigatorAgent(api_key="your_api_key")

# Get market data
market_data = agent.get_market_data(["AI Tools", "EdTech", "FinTech"])

# Analyze market gaps
from hexperiment.tools.data_utils import clean_market_data
from hexperiment.analysis.market_analysis import prepare_market_data, identify_market_gaps

cleaned_data = clean_market_data(market_data)
market_df = prepare_market_data(cleaned_data)
gaps = identify_market_gaps(market_df, growth_threshold=20.0)

# Create visualizations
chart = create_growth_vs_size_chart(market_df)
chart.show()
```

## Documentation

For detailed documentation on each module:

- `hexperiment.agent`: Interface with Toolhouse SDK for AI-powered analysis
- `hexperiment.analysis`: Market analysis algorithms and opportunity scoring
- `hexperiment.visualizations`: Chart generation and visualization tools
- `hexperiment.tools`: Utilities for data processing and cleaning
- `hexperiment.feedback`: User feedback collection and management

## Development

### Running Tests

```bash
pytest tests/
```

### Project Structure

- `src/hexperiment/`: Core package code
  - `agent.py`: Toolhouse SDK integration
  - `analysis/`: Market analysis algorithms
  - `visualizations/`: Chart generation
  - `tools/`: Utility functions
  - `feedback/`: Feedback collection
- `notebooks/`: Jupyter notebooks for demos and tutorials
- `tests/`: Unit tests
- `demo.py`: Standalone demo script

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, contact [support@hexperiment-labs.com](mailto:support@hexperiment-labs.com)
