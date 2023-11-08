import numpy as np
from scipy.optimize import minimize

#  data from the traffic counts, week 1
traffic_data = {
    'time_intervals': ['8 AM - 9 AM', '9 AM - 10 AM', '10 AM - 11 AM', '11 AM - 12 PM', '12 PM - 1 PM', '1 PM - 2 PM', '2 PM - 3 PM'],
    'total_vehicles': [450, 300, 250, 280, 350, 400, 500],
    'petrol_vehicles': [324, 216, 180, 202, 252, 288, 360],
    'diesel_vehicles': [121, 81, 67, 75, 94, 108, 135],
    'lpg_vehicles': [5, 3, 3, 3, 4, 4, 5],
    'average_speed': [15, 20, 25, 20, 18, 15, 12],
    'congestion_level': ['Heavy', 'Moderate', 'Light', 'Moderate', 'Moderate to heavy', 'Heavy', 'Very heavy'],
    'illegal_parking': [20, 10, 5, 15, 25, 30, 40],
    'public_transport_utilization': [0.7, 0.5, 0.4, 0.45, 0.6, 0.65, 0.75]
}

# Validate that no average speed is zero to avoid division by zero
for speed in traffic_data['average_speed']:
    if speed == 0:
        raise ValueError('Average speed cannot be zero.')

# Define the congestion index function
def congestion_index(total_vehicles, average_speed):
    # A simple function that inversely relates congestion to average speed
    return total_vehicles / average_speed

# Define the emission estimation function
def emission_estimate(vehicle_counts, emission_factors):
    # Calculate emissions based on vehicle count and emission factors
    return np.dot(vehicle_counts, emission_factors)


# Define the optimization function for traffic signal adjustment
# This function would have to be replaced with a genetic algorithm for real use
def optimize_signals(congestion_indices):
    # Placeholder function for optimizing traffic signals
    # The optimization variable x is assumed to represent the green light duration for each signal
    # The objective is to minimize the sum of congestion indices weighted by green light duration
    # The bounds represent the range of possible green light durations
    result = minimize(lambda x: np.sum(congestion_indices * x), x0=np.ones(len(congestion_indices)), bounds=[(30, 180) for _ in congestion_indices])
    if result.success:
        return result.x
    else:
        raise ValueError('Optimization did not converge.')

# Example usage of the functions
# Calculate congestion indices for each time interval
congestion_indices = [congestion_index(tv, asp) for tv, asp in zip(traffic_data['total_vehicles'], traffic_data['average_speed'])]

# Assume emission factors for petrol, diesel, and LPG vehicles
emission_factors = [1.2, 1.5, 1.1]  # Placeholder values

# Calculate emission estimates for each time interval
emission_estimates = [emission_estimate(vc, emission_factors) for vc in zip(traffic_data['petrol_vehicles'], traffic_data['diesel_vehicles'], traffic_data['lpg_vehicles'])]

# Optimize traffic signals based on congestion indices
try:
    optimized_signals = optimize_signals(congestion_indices)
    print('Optimized Signals:', optimized_signals)
except ValueError as e:
    print(e)

# Output the results
print('Congestion Indices:', congestion_indices)
print('Emission Estimates:', emission_estimates)