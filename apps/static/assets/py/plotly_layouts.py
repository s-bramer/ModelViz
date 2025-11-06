import plotly.graph_objects as go

standard_layout = go.Layout(
        title=dict(
            # text=f'{DEFAULT_CATCHMENT} Plot',
            font=dict(
                family='Arial, sans-serif',
                size=14,
                color='red'
            ),
            x=0.1,
            xanchor='left'
        ),
        xaxis=dict(
            title='X Axis Label',
            titlefont=dict(
                family='Arial, sans-serif',
                size=12,
                color='black'
            ),
            showgrid=False,
            gridcolor='lightgrey',
            zeroline=False,
            zerolinecolor='lightgrey',
            showline=False,
            linecolor='lightgrey',
            ticklen=20, 
            tickfont=dict(
                family='Arial, sans-serif',
                size=12,
                color='black'
            )
        ),
        yaxis=dict(
            title='Y Axis Label',
            titlefont=dict(
                family='Arial, sans-serif',
                size=12,
                color='black'
            ),
            showgrid=True,
            gridcolor='lightgrey',
            zeroline=False,
            zerolinecolor='lightgrey',
            showline=False,
            linecolor='lightgrey',
            ticklen=20, 
            tickfont=dict(
                family='Arial, sans-serif',
                size=12,
                color='black'
            )
        ),
        legend=dict(
            orientation='h',
            y=1.05,  # Move the legend below the plot
            yanchor='top',
            x=1,
            xanchor='right',
            font=dict(
                family='Arial, sans-serif',
                size=12,
                color='#333'
            ),
            # bgcolor='rgba(255, 255, 255, 0.5)',  # Background color of the legend
            # bordercolor='#333',  # Border color of the legend
            # borderwidth=2  # Border width of the legend
        ),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(
            l=60,
            r=20,
            t=60,
            b=10  # Adjust to make space for the legend
        )
    )