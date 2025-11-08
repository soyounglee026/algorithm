credit = []
score = []
grade = 0
lecture = 0
# 학점, 성적 입력 리스트 생성
for _ in range(20):
  s = input().split()
  credit.append(float(s[1]))
  score.append(s[2])
# 평균 계산
for i in range(20):
  lecture = lecture + credit[i]
  if score[i] == 'A+':
    grade = grade + (credit[i] * 4.5)
  elif score[i] == 'A0':
    grade = grade + (credit[i] * 4.0)
  elif score[i] == 'B+':
    grade = grade + (credit[i] * 3.5)
  elif score[i] == 'B0':
    grade = grade + (credit[i] * 3.0)
  elif score[i] == 'C+':
    grade = grade + (credit[i] * 2.5)
  elif score[i] == 'C0':
    grade = grade + (credit[i] * 2.0)
  elif score[i] == 'D+':
    grade = grade + (credit[i] * 1.5)
  elif score[i] == 'D0':
    grade = grade + (credit[i] * 1.0)
  elif score[i] == 'P':
    lecture = lecture - credit[i]

print(grade/lecture)