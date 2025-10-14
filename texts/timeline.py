import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def generate_author_timeline(csv_filepath):
    """
    Generates and saves a horizontal bar chart visualizing the lifespans (timeline) of authors,
    reading data from a specified CSV file.
    
    The CSV must have 'Author', 'Birth_Year', and 'Death_Year' columns.
    An optional fourth column, 'Colour', can be provided to specify bar colors,
    defaulting to 'blue' if the column is missing or the cell is blank.

    Args:
        csv_filepath (str): The path to the CSV file containing the data.
    """
    # Set the default color for bars if the 'Colour' column is missing or a cell is blank.
    DEFAULT_COLOR = 'blue'

    try:
        # 1. Load data from the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_filepath)

        # Basic check for required columns
        required_cols = ['Author', 'Birth_Year', 'Death_Year']
        if not all(col in df.columns for col in required_cols):
            print(f"Error: CSV file must contain the following columns: {required_cols}")
            return

        # 2. Handle the optional 'Colour' column
        if 'Colour' in df.columns:
            # If the column exists, fill any missing values (NaN) or empty strings with the default color
            # We create a new 'Color' column for consistency after sorting
            df['Color'] = df['Colour'].fillna(DEFAULT_COLOR).replace('', DEFAULT_COLOR)
        else:
            # If the column does not exist, set all colors to the default
            df['Color'] = DEFAULT_COLOR

        # Ensure year columns are numeric (important for plotting)
        df['Birth_Year'] = pd.to_numeric(df['Birth_Year'], errors='coerce')
        df['Death_Year'] = pd.to_numeric(df['Death_Year'], errors='coerce')
        # Drop any rows where years couldn't be converted
        df.dropna(subset=['Birth_Year', 'Death_Year'], inplace=True)

        # 3. Calculate the lifespan (duration for the bar length)
        df['Lifespan'] = df['Death_Year'] - df['Birth_Year']

        # 4. Sort by Birth Year chronologically for visualization clarity
        # Important: The color data must be sorted along with the author data
        df_sorted = df.sort_values(by='Birth_Year', ascending=True).reset_index(drop=True)

        # 5. Create the visualization (Gantt-style timeline)
        plt.figure(figsize=(12, 6))

        # Plot the horizontal bars
        # 'left' sets the start position of the bar (Birth Year)
        # The bar width is the 'Lifespan'
        # Now using the determined colors from the DataFrame
        bars = plt.barh(
            df_sorted['Author'],
            df_sorted['Lifespan'],
            left=df_sorted['Birth_Year'],
            color=df_sorted['Color'] # <-- Use the calculated Color column
        )
        
        # 6. Add text labels for start and end years
        for bar in bars:
            # Get bar properties
            y_pos = bar.get_y() + bar.get_height() / 2
            birth_year = int(bar.get_x())
            lifespan = bar.get_width()
            death_year = int(birth_year + lifespan)

            # Place the Birth Year label (aligned right)
            plt.text(birth_year, y_pos, str(birth_year), ha='right', va='center',
                     fontsize=10, color='black', fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))

            # Place the Death Year label (aligned left)
            plt.text(death_year, y_pos, str(death_year), ha='left', va='center',
                     fontsize=10, color='black', fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))


        # 7. Final chart formatting
        plt.title(f'Historical Timeline from Data File: {os.path.basename(csv_filepath)}', fontsize=16, pad=20)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Person/Subject', fontsize=12)

        # Add a slight margin to the x-axis limits for better label visibility
        min_year = df_sorted['Birth_Year'].min()
        max_year = df_sorted['Death_Year'].max()
        plt.xlim(min_year - 50, max_year + 50)

        plt.grid(axis='x', linestyle='--', alpha=0.5)

        # Invert y-axis to list the earliest author at the top
        plt.gca().invert_yaxis()

        plt.tight_layout()

        # 8. Save the plot to a file
        output_filename = 'timeline_chart_from_csv.png'
        plt.savefig(output_filename)
        print(f"Timeline chart successfully saved as '{output_filename}'")
        # Display relevant columns, including the applied color
        print("\nProcessed Data:")
        print(df_sorted[['Author', 'Birth_Year', 'Death_Year', 'Lifespan', 'Color']].to_markdown(index=False))

    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
        print("Please ensure the CSV file path is correct.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_filepath}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Execution Block ---
if __name__ == '__main__':
    # Check if a file name was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python timeline.py <path_to_csv_file>")
        print("Example: python timeline.py authors_data.csv")
        sys.exit(1)
    
    # Get the CSV filename from the first command-line argument (sys.argv[1])
    CSV_FILENAME = sys.argv[1]
    
    # Generate the timeline using the provided CSV file path
    print(f"Attempting to read data from '{CSV_FILENAME}'...")
    generate_author_timeline(CSV_FILENAME)
