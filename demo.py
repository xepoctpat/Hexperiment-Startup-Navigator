"""
Hexperiment Startup Navigator - Interactive Demo

This script demonstrates the key features of the Hexperiment Startup Navigator,
an AI-powered tool for market analysis and startup opportunity identification.
"""
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
from datetime import datetime

# Import our modules
from src.hexperiment.agent import NavigatorAgent
from src.hexperiment.analysis.market_analysis import (
    prepare_market_data, calculate_market_attractiveness, 
    identify_market_gaps, predict_market_evolution
)
from src.hexperiment.visualizations.market_charts import (
    create_market_size_chart, create_growth_vs_size_chart,
    create_competitor_analysis_chart
)
from src.hexperiment.feedback.feedback_manager import FeedbackManager
from src.hexperiment.tools.data_utils import clean_market_data

# Configure plotly to display in the browser for better interactivity
pio.renderers.default = "browser"

def print_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80 + "\n")
def print_step(step_num, description):
    """Print a formatted step description"""
    print(f"\n--- Step {step_num}: {description} ---\n")

def print_message(*lines):
    """Print multiple lines of text"""
    for line in lines:
        print(line)

def wait_for_user():
    """Wait for the user to press Enter to continue"""
    input("\nPress Enter to continue...")

def main():
    """Main demo function"""
    print_header("HEXPERIMENT STARTUP NAVIGATOR DEMO")
    print_message(
        "Welcome to the Hexperiment Startup Navigator demo!",
        "This interactive demonstration will showcase the key features of our",
        "AI-powered startup analysis and visualization tool."
    )
    
    # Step 1: Define market segments to analyze
    print_step(1, "Defining Market Segments")
    market_segments = [
    market_segments = [
        'AI Tools','SaaS','FinTech','EdTech','Health Tech','Clean Energy'
    ]
    print(f"We'll analyze these market segments: {', '.join(market_segments)}")
    wait_for_user()
    # Step 2: Generate market data (simulated for the demo)
    print_step(2, "Gathering Market Data")
    print("In a real scenario, we would use the NavigatorAgent to retrieve")
    print("market data from the Toolhouse SDK. For this demo, we'll use simulated data.")
    
    # Generate simulated market data
    np.random.seed(42)  # For reproducible results
    market_data = {
        'Segment': market_segments,
        'Market_Size': [
            98.7,  # AI Tools
            195.2, # SaaS
            112.5, # FinTech
            89.3,  # EdTech
            187.6, # Health Tech
            215.8  # Clean Energy
        ],
        'Growth_Rate': [
            38.2,  # AI Tools
            16.4,  # SaaS
            20.3,  # FinTech
            18.7,  # EdTech
            15.9,  # Health Tech
            22.1   # Clean Energy
        ],
        'Competitors': [
            124,  # AI Tools
            482,  # SaaS
            340,  # FinTech
            215,  # EdTech
            390,  # Health Tech
            178   # Clean Energy
        ]
    }
    # Step 3: Analyze market opportunities
    print_step(3, "Analyzing Market Opportunities")
    print_message("Now we'll analyze the market data to identify the most attractive opportunities.")
    # Step 3: Analyze market opportunities
    print_step(3, "Analyzing Market Opportunities")
    print_message("Now we'll analyze the market data to identify the most attractive opportunities.")
    
    # Clean the market data and convert to DataFrame for display
    cleaned_data = clean_market_data(market_data)
    market_df = pd.DataFrame(cleaned_data)
    print("\nCleaned market data:")
    print(market_df)
    
    # Calculate market attractiveness scores with custom weights
    attractiveness_df = calculate_market_attractiveness(
        market_df, size_weight=0.35, growth_weight=0.45, competition_weight=0.2
    )
    
    # Sort by attractiveness score
    sorted_df = attractiveness_df.sort_values("Attractiveness_Score", ascending=False)
    
    print("\nMarket segments ranked by attractiveness:")
    for i, (index, row) in enumerate(sorted_df.iterrows(), 1):
        print(f"{i}. {row['Segment']} - Score: {row['Attractiveness_Score']:.3f}")
    
    # Identify market gaps (high growth, low competition)
    gaps_df = identify_market_gaps(market_df, growth_threshold=18.0, competition_threshold=250)
    
    print("\nIdentified market gaps (high growth, low competition):")
    if not gaps_df.empty:
        for i, (index, row) in enumerate(gaps_df.iterrows(), 1):
            print(f"{i}. {row['Segment']} - Growth: {row['Growth_Rate']}%, Competitors: {row['Competitors']}")
    else:
        print("No market gaps identified with the current thresholds")
    
    print("We'll generate several charts and open them in your browser.")
    
    wait_for_user()
    print("We'll generate several charts and open them in your browser.")
    input("\nPress Enter to continue...")
    
    print("We'll generate several charts and open them in your browser.")
    
    wait_for_user()
    print("\nGenerating Market Size Chart...")
    market_size_fig = create_market_size_chart(market_df)
    market_size_fig.show()
    
    # Create growth vs size chart
    print("Generating Growth vs Size Chart...")
    growth_size_fig = create_growth_vs_size_chart(market_df)
    growth_size_fig.show()
    
    # Create competitor analysis chart
    # Create competitor analysis chart
    print("Generating Competitive Landscape Analysis...")
    competitor_fig = create_competitor_analysis_chart(market_df)
    competitor_fig.show()
    
    input("\nPress Enter to continue after viewing the charts...")
    
    # Create competitor analysis chart
    print("The Navigator can predict how markets will evolve over time.")
    
    # Predict market evolution for the next 5 years
    prediction_df = predict_market_evolution(market_df, years_ahead=5)
    
    # Display market size predictions
    print("\nPredicted Market Size (Billions USD):")
    columns_to_show = ["Segment", "Market_Size"] + [f"Market_Size_Y{i}" for i in range(1, 6)]
    pred_display = prediction_df[columns_to_show].round(1)
    print(pred_display)
    # Create a visualization of the predictions for the top segment
    top_segment = sorted_df.iloc[0]["Segment"]
    top_segment_data = prediction_df[prediction_df["Segment"] == top_segment]
    
    years = list(range(2025, 2031))  # Current year to current+5
    sizes = [top_segment_data["Market_Size"].values[0]] + [
        top_segment_data[f"Market_Size_Y{i}"].values[0] for i in range(1, 6)
    ]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, sizes, marker='o', linewidth=2)
    plt.title(f"{top_segment} Market Size Projection (2025-2030)")
    plt.xlabel("Year")
    plt.ylabel("Market Size (Billions USD)")
    plt.grid(True)
    plt.savefig("market_projection.png")
    plt.show()
    # Step 6: Collect feedback
    print_step(6, "Collecting Feedback")
    print_message("The Navigator includes a feedback system to improve over time.")
    plt.savefig("market_projection.png")
    plt.show()
    
    wait_for_user()
    
    # Initialize feedback manager and create a dummy analysis ID
    feedback_mgr = FeedbackManager()
    analysis_id = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Record feedback on the analysis
    feedback_mgr.record_analysis_feedback(
        analysis_id=analysis_id,
        market_segments=market_segments,
        usefulness_rating=5,
        accuracy_rating=4,
        comments="Great insights on emerging market opportunities!",
        user_id="demo_user"
    )
    
    print("\nDemo completed! You've seen the key features of the Hexperiment Startup Navigator.")
    print("In a real deployment, the Navigator would connect to the Toolhouse SDK")
    print("to gather real-time market data and provide AI-powered recommendations.")
    
    print_header("THANK YOU FOR TRYING THE HEXPERIMENT STARTUP NAVIGATOR!")

if __name__ == "__main__":
    main()