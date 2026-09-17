#!/usr/bin/env python3
import numpy as np


def rnn(rnn_cell, X, h_0):
    """
    Performs forward propagation for a simple RNN.

    Args:
        rnn_cell: instance of RNNCell to use for forward propagation
        X (numpy.ndarray): data of shape (t, m, i)
            t = max number of time steps
            m = batch size
            i = dimensionality of the data
        h_0 (numpy.ndarray): initial hidden state of shape (m, h)

    Returns:
        tuple: (H, Y)
            H (numpy.ndarray): all hidden states, shape (t + 1, m, h)
            Y (numpy.ndarray): all outputs, shape (t, m, o)
    """
    # Unpack dimensions from the inputs
    t, m, i = X.shape
    _, h = h_0.shape
    o = rnn_cell.Wy.shape[1]

    # Pre-allocate arrays for hidden states and outputs
    H = np.zeros((t + 1, m, h))
    Y = np.zeros((t, m, o))

    # Store the initial hidden state
    H[0] = h_0

    # Iterate over each time step
    h_prev = h_0
    for timestep in range(t):
        h_next, y = rnn_cell.forward(h_prev, X[timestep])
        H[timestep + 1] = h_next
        Y[timestep] = y
        h_prev = h_next

    return H, Y
