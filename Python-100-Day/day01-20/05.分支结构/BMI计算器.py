height = float(input('请输入您的身高（单位：米）：'))
weight = float(input('请输入您的体重（单位：千克）：'))
bmi = weight / height**2
print(f'您的BMI值为：{bmi:.2f}')
if bmi < 18.5:
    print('您的体重过轻')
elif bmi < 24:
    print('您的体重正常')
elif bmi < 27:
    print('您的体重过重')
elif bmi < 30:
    print('您的体重肥胖')
else:
    print('您的体重严重肥胖')
