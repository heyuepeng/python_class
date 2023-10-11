# 初始化总学分和绩点
total_credit = 0
total_gpa = 0

# 循环读取每门课程的信息
for i in range(5):
    course_name, score, credit = input().split()
    score = int(score)
    credit = int(credit)

    # 计算课程绩点
    course_gpa = 4.0 * (90 if score > 90 else score) / 90

    # 累加总学分和总绩点
    total_credit += credit
    total_gpa += course_gpa * credit

# 计算综合GPA
gpa = total_gpa / total_credit

# 输出结果，保留两位小数
print("GPA:{:.2f}".format(gpa))
