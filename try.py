import random
# 1: correct method
# 0: wrong method
sample=[0,0,0,1,0,0,0,0,0]+[0]*91
# len(sample)=100
single_prop=sum(sample)/len(sample)
print(f"single_prop is {single_prop}")
exp_cnt=10000

def rand_choose():
    return sample[random.randint(0,len(sample)-1)]

def rand_choose_n_times(cnt):
    ret=0
    for i in range(cnt):
        ret|=rand_choose()
    return ret

def rand_choose_n_times_correct_at_least_once_prop(cnt):
    result=[]
    for i in range(exp_cnt):
        result.append(rand_choose_n_times(cnt))
    print(f"try {cnt} times, experiment prop {sum(result)/len(result)}, theory prop {1-(1-single_prop)**cnt}")

rand_choose_n_times_correct_at_least_once_prop(10)
rand_choose_n_times_correct_at_least_once_prop(50)
rand_choose_n_times_correct_at_least_once_prop(100)
rand_choose_n_times_correct_at_least_once_prop(200)
print("try n times and success at least once, if you try enough..\nincrease the single_prop, or reduce the time of each try")