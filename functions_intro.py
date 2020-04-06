# Multiple return values on functions:

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

print("target has a low limit of " + str(low) + 
" and margin has a high limit of " + str(high))