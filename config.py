REF_SUM = 350
REF_AVG = 27
REF_MAX = 60
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
