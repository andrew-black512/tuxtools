import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_author_timeline(authors_data):
    """
    Generates and saves a horizontal bar chart visualizing the lifespans (timeline) of authors.

    Args:
        authors_data (list of tuples): A list where each tuple contains
                                       (Author Name, Birth Year, Death Year).
                                       Example: [('John of Ruusbroec', 1294, 1381), ...]
    """

    # 1. Load data into a pandas DataFrame
    df = pd.DataFrame(authors_data, columns=['Author', 'Birth_Year', 'Death_Year'])

    # 2. Calculate the lifespan (duration for the bar length)
    df['Lifespan'] = df['Death_Year'] - df['Birth_Year']

    # 3. Sort by Birth Year chronologically for visualization clarity
    df_sorted = df.sort_values(by='Birth_Year', ascending=True).reset_index(drop=True)

    # 4. Create the visualization (Gantt-style timeline)
    plt.figure(figsize=(12, 6))

    # Plot the horizontal bars
    # 'left' sets the start position of the bar (Birth Year)
    # The bar width is the 'Lifespan'
    bars = plt.barh(
        df_sorted['Author'],
        df_sorted['Lifespan'],
        left=df_sorted['Birth_Year'],
        color=['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974', '#64B5CD'] # A color cycle
    )

    # 5. Add text labels for start and end years
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


    # 6. Final chart formatting
    plt.title('Historical Author Timeline (Lifespan)', fontsize=16, pad=20)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Author', fontsize=12)

    # Add a slight margin to the x-axis limits for better label visibility
    min_year = df_sorted['Birth_Year'].min()
    max_year = df_sorted['Death_Year'].max()
    plt.xlim(min_year - 50, max_year + 50)

    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Invert y-axis to list the earliest author at the top
    plt.gca().invert_yaxis()

    plt.tight_layout()

    # 7. Save the plot to a file
    output_filename = 'authors_timeline_chart.png'
    plt.savefig(output_filename)
    print(f"Timeline chart successfully saved as '{output_filename}'")
    print("\nDataFrame:")
    print(df_sorted[['Author', 'Birth_Year', 'Death_Year', 'Lifespan']].to_markdown(index=False))


# --- Sample Data (You can modify this list) ---
# Format: (Name, Birth Year, Death Year)
sample_authors = [
    ('John of Ruusbroec', 1294, 1381),
    ('Hildegard of Bingen', 1098, 1179),
    ('Geoffrey Chaucer', 1343, 1400),
    ('William Shakespeare', 1564, 1616),
    ('Jane Austen', 1775, 1817),
    ('Virginia Woolf', 1882, 1941)
]

if __name__ == '__main__':
    # Ensure dependencies are installed: pip install pandas matplotlib
    generate_author_timeline(sample_authors)
