# ===============================================================
# cq-python-0065: Timezone Awareness
# This file contains both violating and compliant examples.
# ===============================================================

from datetime import datetime, timezone, timedelta
import pytz  # pip install pytz if not available

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Naive datetime without timezone
# --------------------------------------------------------------
naive_dt = datetime(2025, 11, 18, 12, 0, 0)
print("Violation 1 - naive datetime:", naive_dt)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Operations with naive datetime
# --------------------------------------------------------------
future_dt = datetime(2025, 11, 19, 12, 0, 0)
time_diff = future_dt - naive_dt  # VIOLATION: naive datetime arithmetic
print("Violation 2 - time difference (naive):", time_diff)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using timezone-aware datetime objects
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# UTC aware datetime
# --------------------------------------------------------------
utc_dt = datetime(2025, 11, 18, 12, 0, 0, tzinfo=timezone.utc)
print("\nCompliant 1 - UTC datetime:", utc_dt)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Convert naive datetime to aware datetime using pytz
# --------------------------------------------------------------
local_tz = pytz.timezone("Asia/Kolkata")
aware_dt = local_tz.localize(datetime(2025, 11, 18, 12, 0, 0))
print("Compliant 2 - local timezone aware datetime:", aware_dt)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Operations with timezone-aware datetime
# --------------------------------------------------------------
future_aware_dt = local_tz.localize(datetime(2025, 11, 19, 12, 0, 0))
time_diff_aware = future_aware_dt - aware_dt
print("Compliant 3 - time difference (aware):", time_diff_aware)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 4
# Converting between timezones
# --------------------------------------------------------------
new_york_tz = pytz.timezone("America/New_York")
ny_dt = aware_dt.astimezone(new_york_tz)
print("Compliant 4 - converted to New York timezone:", ny_dt)
