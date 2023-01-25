from typing import Dict, Tuple

# Led brightness map for train states where [1] is the destination station
# Tune for fade effect into stations and train stacking
# Invert for inbound vs outbound directions
brightness_overlay: Dict[str, Tuple] = dict(in_transit_to=(0.01, 0.01, 0.0),
                                      incoming_at=(0.01, 0.2, 0.0),
                                      stopped_at=(0.0, 0.5, 0.0))
