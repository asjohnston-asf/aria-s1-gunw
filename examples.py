from itertools import product

from source import get_stack_for_frame


frame_id = 23474
stack = get_stack_for_frame(frame_id)

# nearest neighbor
pairs = list(zip(stack, stack[1:]))

# nearest neighbor and next nearest neighbor
pairs = list(zip(stack, stack[1:])) + list(zip(stack, stack[2:]))

# all pairs
pairs = [pair for pair in product(stack, stack) if (pair[1]['date'] - pair[0]['date']).total_seconds() > 0]

# all pairs with temporal baseline from 1-28 days
pairs = [pair for pair in product(stack, stack) if 1 <= (pair[1]['date'] - pair[0]['date']).total_seconds()/60/60/24 <= 28]

jobs = [
    {
        'job_type': 'INSAR_ISCE',
        'job_parameters': {
            'granules': pair[1]['granules'],
            'secondary_granules': pair[0]['granules'],
            'frame_id': frame_id,
        },
    }
    for pair in pairs
]
