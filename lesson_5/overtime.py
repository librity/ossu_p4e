OVERTIME_LIMIT = 40.0

hours = input("Enter Hours:")
hours_f = float(hours)

rate = input("Enter Rate:")
rate_f = float(rate)


def computepay(hours, rate):
  if (hours <= OVERTIME_LIMIT):
    return hours * rate

  overtime_hrs = hours - OVERTIME_LIMIT
  normal_hrs = hours - overtime_hrs

  pay = normal_hrs * rate
  pay += overtime_hrs * 1.5 * rate

  return pay


pay = computepay(hours_f, rate_f)
print("Pay", pay)
