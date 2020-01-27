import matplotlib.colors

la_diverging = [
    "#CA5800",
    "#FDBF11",
    "#FDD870",
    "#FFF2CF",
    "#CFE8F3",
    "#73BFE2",
    "#1696D2",
    "#0A4C6A",
]

la_blues = [
    "#CDEAF8",
    "#B3D0E2",
    "#97BFD6",
    "#78B0CA",
    "#5F84A9",
    "#4B6A8A",
    "#315174",
    "#17375E",
]

la_greens = [
    "#D1F5DF",
    "#B8F1C6",
    "#8CC69F",
    "#76B18B",
    "#609B77",
    "#4A8663",
    "#347050",
    "#1E5B3C",
]

la_grayred = [
    "#E1E1E1",
    "#D1C5C8",
    "#E15F51",
    "#A30F23",
]

cmaps = [
    matplotlib.colors.LinearSegmentedColormap.from_list("la_diverging", la_diverging),
    matplotlib.colors.LinearSegmentedColormap.from_list(
        "la_diverging_r", la_diverging[::-1]
    ),
    matplotlib.colors.ListedColormap(la_diverging, "la_diverging_d"),
    matplotlib.colors.ListedColormap(la_diverging[::-1], "la_diverging_r_d"),
    matplotlib.colors.LinearSegmentedColormap.from_list("la_blues", la_blues),
    matplotlib.colors.LinearSegmentedColormap.from_list("la_blues_r", la_blues[::-1]),
    matplotlib.colors.ListedColormap(la_blues, "la_blues_d"),
    matplotlib.colors.ListedColormap(la_blues[::-1], "la_blues_r_d"),
    matplotlib.colors.LinearSegmentedColormap.from_list("la_greens", la_greens),
    matplotlib.colors.LinearSegmentedColormap.from_list("la_greens_r", la_greens[::-1]),
    matplotlib.colors.ListedColormap(la_greens, "la_greens_d"),
    matplotlib.colors.ListedColormap(la_greens[::-1], "la_greens_r_d"),
    matplotlib.colors.LinearSegmentedColormap.from_list("la_grayred", la_grayred),
    matplotlib.colors.LinearSegmentedColormap.from_list(
        "la_grayred_r", la_grayred[::-1]
    ),
    matplotlib.colors.ListedColormap(la_grayred, "la_grayred_d"),
    matplotlib.colors.ListedColormap(la_grayred[::-1], "la_grayred_r_d"),
]

if __name__ == "__main__":
    """
    Generate a plot showing the available colormaps.
    Adapted from https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
    """
    import numpy as np
    import matplotlib.pyplot as plt

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmaps)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axes = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    axes[0].set_title("Colormaps", fontsize=14)

    for ax, cmap in zip(axes, cmaps):
        ax.imshow(gradient, aspect="auto", cmap=cmap)
        ax.text(
            -0.01,
            0.5,
            cmap.name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    plt.savefig("cmaps.png")
