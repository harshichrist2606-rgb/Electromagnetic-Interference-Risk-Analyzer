print("==============================================")
print(" ELECTROMAGNETIC INTERFERENCE RISK ANALYZER")
print("==============================================")

frequency = float(input("Enter operating frequency (MHz): "))
field_strength = float(input("Enter field strength (V/m): "))
distance = float(input("Enter distance from source (meters): "))
shielding = float(input("Enter shielding effectiveness (dB): "))

if distance <= 0:
    print("Distance must be greater than zero.")
    exit()

# Simplified field reduction with distance
received_field = field_strength / distance

# Shielding reduction
shielding_factor = 10 ** (-shielding / 20)

effective_field = received_field * shielding_factor

# Educational risk score
risk_score = effective_field

if risk_score < 1:
    risk_level = "LOW"
elif risk_score < 10:
    risk_level = "MODERATE"
else:
    risk_level = "HIGH"

print("\n==============================================")
print(" EMI ANALYSIS RESULTS")
print("==============================================")

print(f"Operating Frequency: {frequency:.2f} MHz")
print(f"Original Field Strength: {field_strength:.2f} V/m")
print(f"Distance: {distance:.2f} m")
print(f"Shielding Effectiveness: {shielding:.2f} dB")
print(f"Effective Field Strength: {effective_field:.4f} V/m")
print(f"Risk Score: {risk_score:.4f}")
print(f"EMI Risk Level: {risk_level}")

if risk_level == "LOW":
    print("Recommendation: Continue basic EMI monitoring.")
elif risk_level == "MODERATE":
    print("Recommendation: Improve grounding and shielding.")
else:
    print("Recommendation: Perform detailed EMC testing.")

print("\nNote: This is a simplified educational analyzer.")
