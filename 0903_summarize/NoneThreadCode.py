# thread를 사용하지 않고 연산을 하는 1~1억까지 더하는 코드
# 연산 결과값과 연산을 마친 시간을 확인해본다.

# 시간을 체크하기 위해 time 패키지 불러오기
import time


# 코드 시작 시간 check
start_time = time.time()

# 1부터 1억까지 더하기
sum_of_numbers = sum(range(1, 100000001))

# 완료한 시간 check
end_time = time.time()

# 연산한 결과값과, 코드 실행 시간을 출력
# print 연산을 하는 시간이 있기 때문에 print 연산 이전에 시간을 check
print("1부터 1억까지 합 : {}".format(sum_of_numbers))
print("코드 실행 시간 : {}초".format(end_time - start_time))

# 2.14598초 정도 소요