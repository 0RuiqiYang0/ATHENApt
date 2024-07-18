import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../ATHENApp_plot_tool')))
from plot_slice import main

def test_plot_slice():
    args = {
        'data_file': 'disk.out2.00800.athdf',
        'quantity': 'rho',
        'output_file': 'test_out.png',
        'direction': 3,
        'slice_location': None,
        'average': False,
        'sum': False,
        'level': None,
        'x_min': 1.0,
        'x_max': 70.0,
        'y_min': None,
        'y_max': None,
        'fill': False,
        'colormap': 'viridis',
        'vmin': 0.,
        'vmax': 0.2,
        'logc': False,
        'stream': None,
        'stream_average': False,
        'stream_density': 1.0,
        'num_ghost': 0,
        'fig_width': 6.0,
        'fig_height': 6.0,
        'dpi': 100,
        'format': 'png'
    }

    # Run main function
    main(**args)

    assert os.path.exists(args['output_file'])

if __name__ == '__main__':
    pytest.main()