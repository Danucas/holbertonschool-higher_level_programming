#!/usr/bin/python3
"""
Finds a peak in a list
"""

def find_peak(signal):
    """
    Finds a peak in a list
    """
    peak = None
    for i, num in enumerate(signal):
        try:
            if i > 0 and i < len(signal) - 1:
                if num >= signal[i-1] and num >= signal[i+1]:
                    peak = num
        except:
            pass
    return peak
