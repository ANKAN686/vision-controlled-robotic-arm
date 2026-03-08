import math

def ik_2dof(x, y, L1, L2, z):
    # 1. Distance from base to target
    r2 = x*2 + y2 + z*2
    r = math.sqrt(r2)

    # 2. Safety Check: Out of reach?
    if r > (L1 + L2):
        print(f"Target unreachable: Distance {r:.2f} > Max Reach {L1+L2}")
        return None, None, None

    # 3. Prevent division by zero in atan(x/z)
    if z == 0:
        z = 0.000001

    # Base rotation angle (phi)
    phi = math.degrees(math.atan(x / z))

    # 4. Compute cos(theta2)
    cos_val = (r2 - L1*2 - L2*2) / (2 * L1 * L2)

    # 5. Clamp for floating point safety
    cos_val = max(-1.0, min(1.0, cos_val))

    theta2 = math.acos(cos_val)  # elbow-down

    # 6. Compute theta1
    def compute_theta1(t2):
        k1 = L1 + L2 * math.cos(t2)
        k2 = L2 * math.sin(t2)
        return math.atan(y / z) - math.atan(k2 / k1)

    theta1 = compute_theta1(theta2)

    # Return shoulder, elbow, base
    return math.degrees(theta1) + 90, math.degrees(theta2), phi