# PR: Add Multi-Model LLM Provider Support

## Description
This PR enhances the Hexperiment Startup Navigator by adding support for multiple Large Language Model providers beyond the default Toolhouse integration. This allows users to choose between different AI models for different use cases.

## New Model Support
- **GitHub Copilot**: Integration for code-related tasks and pattern recognition
- **DeepSeek**: Added for specialized market analysis capabilities
- **Claude (Anthropic)**: Integration for detailed market recommendations

## Changes
- Created a model provider abstraction layer in `src/hexperiment/providers/`
- Added provider-specific adapters for each LLM API
- Updated the `NavigatorAgent` to support model switching
- Enhanced configuration to allow specifying preferred models for different tasks

## Technical Implementation
- Each model provider is implemented as a pluggable adapter
- API keys are loaded from environment variables
- Response formatting is standardized across all providers
- Fallback mechanisms ensure operation continues if a specific provider is unavailable

## Usage Example
```python
from hexperiment import NavigatorAgent
from hexperiment.providers import ModelProvider

# Using Claude for recommendations
agent = NavigatorAgent(provider=ModelProvider.CLAUDE)
recommendations = agent.analyze_opportunity(market_data)

# Using DeepSeek for technical analysis
agent = NavigatorAgent(provider=ModelProvider.DEEPSEEK)
technical_analysis = agent.get_market_details(segment)
```

## Testing
- Unit tests for each provider adapter
- Integration tests verifying correct provider selection
- Benchmarks comparing response quality between providers

## Documentation
- Added documentation for configuring each provider
- Included provider-specific capabilities and limitations
- Updated README with model selection guidance