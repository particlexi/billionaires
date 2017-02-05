#calculate the exceeds 6 groups in the coin sequence
import random

group_num=0
total_group=0
group_cnt=0
exceed_five = 0
head_five = 0
hfive_cnt = 0

toss_num=10
trial_num=10000000

p = 0.6
pc = 0.4

for i in range(trial_num):
	prev_H = False
	prev_T = False
	for j in range(toss_num):
		if random.random()<=0.6:
			head_five += 1
			prev_T = False
			if prev_H==False:
				group_num += 1
				prev_H = True
		else:
			head_five = 0
			prev_H = False
			if prev_T==False:
				group_num += 1
				prev_T = True
				
	if head_five > 5:
		hfive_cnt += 1
	if group_num > 6:
		group_cnt += 1
	if group_num > 5:
		exceed_five += 1
		
	total_group += group_num
	group_num = 0
	head_five = 0
				
expect =  float(total_group)/float(trial_num)
print '{:.9f}'.format(expect)
				
prob = float(group_cnt)/float(total_group)
print '{:.9f}'.format(prob)

prob5 = float(group_cnt)/float(exceed_five)
print '{:.9f}'.format(prob5)

prob5e = float(hfive_cnt)/float(total_group)
print '{:.9f}'.format(prob5e)