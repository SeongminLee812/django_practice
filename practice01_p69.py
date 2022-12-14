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
	result_list = []
	for string in compare_list:
		if string not in input_str:
			result_list.append(string)
	return result_list

input_str1 = '012345678'
input_str2 = '48750219'
print(solution(input_str1), ", ", solution(input_str2))

# %%

# 실전예제 1-3 숫자 제외하기
# 숫자와 문자가 섞인 문자열 입력에서 숫자를 제외하고 문자만 남게해서 반환하자.

def solution(input_str):
	answer = ""
	for string in input_str:
		if not string.isdigit():
			answer = answer + string
	return answer

input_str1 = 'H123e4l5l6o7, p8y9t0h23o1n'

print(solution((input_str1)))

# %%

# 실전예제 1-4 문자열 횟수 세기

'''알파벳으로 구성된 입력 문자열에서 각각의 알파벳이 등장한 횟수를 세어 해당 알파벳 + 해당 알파벳이 나온 횟수'
형태로 반환해 보자. 이때 알파벳은 정렬해서 반환한다.
예를 들어, 입력 "aaabbccd"는 "a3b2c2d1"로 반환하면 된다.'''
from string import ascii_lowercase

def solution(input_str):
	answer = ""
	alphabet_list = list(ascii_lowercase)
	num_list = [0 for _ in alphabet_list]
	print(alphabet_list)
	print(num_list)
	input_dict = dict(zip(alphabet_list, [0 for _ in alphabet_list]))
	
	for i in input_str:
		input_dict[i] += 1
	input_str = list(set(input_str))
	input_str.sort()
	
	for i in input_str:
		answer = answer + i + str(input_dict[i])
	return answer

print(solution('aabbccdd')+ '\n' + solution('aabcdabbfweeaddfadf'))