import string_math

fn_1 = '1'
fn_2 = '1'
fn = '2'
idx = 3
while len(fn) < 1000:
    fn_2 = fn_1
    fn_1 = fn
    fn = string_math.add(fn_1, fn_2)
    idx += 1
print idx
