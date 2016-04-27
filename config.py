REF_SUM = 250
REF_AVG = 17
REF_MAX = 50
REF_RAT = 0.6

def template(args):
    return '''\
%s
Complexity results for %s
   Total Complexity:   %d, target was %d, %d%%
   Average Complexity: %d, target was %d, %d%%
   Maximum Complexity: %d, target was %d, %d%%
   Top Quartile Ratio: %.2f, target was %.2f, %d%%

Score: %d%%
''' % args
