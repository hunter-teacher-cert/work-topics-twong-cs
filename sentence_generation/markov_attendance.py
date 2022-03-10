import random
attendance_chain = {
  'absent': ['absent', 'absent', 'absent', 'absent', 'absent', 'absent', 'absent','late','present','present'],
  'late': ['late', 'late', 'late', 'present', 'present', 'present', 'present', 'absent', 'absent', 'absent'],
  'present': ['present', 'present', 'present', 'present', 'present', 'present', 'present', 'present', 'absent', 'late']
}

attendance = [random.choice(list(attendance_chain.keys()))]

for i in range(10):
    attendance.append(random.choice(attendance_chain[attendance[i]]))

print(attendance)