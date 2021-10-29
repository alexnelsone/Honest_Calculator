units = int(input())

if units < 1:
    print('no army')
elif units >= 1 and units <= 9:
    print('few')
elif units >= 10 and units <= 49:
    print('pack')
elif units >= 50 and units <= 499:
    print('horde')
elif units >= 500 and units <= 999:
    print('swarm')
elif units >= 1000:
    print('legion')