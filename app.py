import streamlit as st

import pydeck as pdk

# Data for globe visualization

DATA_URL = "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"

# Streamlit app

def main():

    st.title("3D Globe Visualization with Streamlit")

    # Load data

    data = pd.read_csv(DATA_URL)

    # Set up initial view state

    view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1, max_zoom=10, pitch=0, bearing=0)

    # Create the globe layer

    globe_layer = pdk.Layer(

        "GlobeLayer",

        data=data,

        pickable=True,

        opacity=0.8,

        auto_highlight=True,

        radius_scale=100,

        get_position="[longitude, latitude]",

        get_radius="intensity",

        get_color="[200, 30, 0]",

        get_elevation="intensity * 10",

    )

    # Create the deck.gl visualization

    r = pdk.Deck(layers=[globe_layer], initial_view_state=view_state, tooltip={"text": "{country}"})

    # Render the globe

    st.pydeck_chart(r)

if __name__ == "__main__":

    main()

