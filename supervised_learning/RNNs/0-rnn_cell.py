#!/usr/bin/env python3
import numpy as np


class RNNCell:
    """Represents a cell of a simple RNN."""

    def __init__(self, i, h, o):
        """
        Class constructor.

        Args:
            i (int): dimensionality of the data
            h (int): dimensionality of the hidden state
            o (int): dimensionality of the outputs

        Attributes:
            Wh (numpy.ndarray): weights for concatenated hidden state and input data
            Wy (numpy.ndarray): weights for output
            bh (numpy.ndarray): biases for concatenated hidden state and input data
            by (numpy.ndarray): biases for output
        """
        # Initialize weights with random normal distribution
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))

        # Initialize biases as zeros
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Performs forward propagation for one time step.

        Args:
            x_t (numpy.ndarray): shape (m, i) containing data input for the cell
            h_prev (numpy.ndarray): shape (m, h) containing the previous hidden state

        Returns:
            tuple: (h_next, y)
                h_next (numpy.ndarray): next hidden state
                y (numpy.ndarray): output of the cell (softmax activation)
        """
        # Concatenate previous hidden state and current input
        concat = np.concatenate((h_prev, x_t), axis=1)

        # Compute the next hidden state using tanh activation
        h_next = np.tanh(np.matmul(concat, self.Wh) + self.bh)

        # Compute the output using softmax activation
        z = np.matmul(h_next, self.Wy) + self.by
        y = self.softmax(z)

        return h_next, y

    @staticmethod
    def softmax(x):
        """
        Computes the softmax activation function.

        Args:
            x (numpy.ndarray): input values

        Returns:
            numpy.ndarray: softmax output
        """
        # Subtract max for numerical stability
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e_x / e_x.sum(axis=1, keepdims=True)
