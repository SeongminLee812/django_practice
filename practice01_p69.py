# 실전예제 1-1 자기소개

name = '이성민'
age = 28
school = '서울디지털대학교'
job = 'MLOps 엔지니어'
dream = '많은 사람들에게 선한 영향력을 미치는 사람'

text = """
안녕하세요! {}살 {}입니다.
저는 {}를 졸업하고, 현재는 {}로 일하고 있습니다.
제 꿈은 '{}'입니다.""".format(age, name, school, job, dream)

print(text)

# %%
# 실전예제 2-2 없는 숫자 찾기

# 숫자로 구성된 입력 문자열을 받아서 해당 문자열에 없는 숫자를 찾아서 반환해보자,
# 예를 들어, 입력 "012345678"에서는 "9"를 반환하면 된다.

def solution(input_str):
	# 각 숫자 있나 확인부터
	compare_list = ['0', '1', '2' , '3', '4', '5', '6', '7', '8', '9']
	for string in compare_list:
		result_list = []
		if string not in input_str:
			result_list.append(string)
	return result_list

input_str1 = '012345678'
input_str2 = '48750219'
print(solution(input_str1), ", ", solution(input_str2))

# %%