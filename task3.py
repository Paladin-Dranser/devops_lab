number = int(input())

friends = set(i for i in input().split())
for i in range(number):
    friends.add(input())

number = int(input())

followers = set()
for i in range(number):
    followers.add(input())

print("Friends: %s" % ', '.join(sorted(friends)))
print("Mutual Friends: %s" % ', '.join(sorted(friends & followers)))
print("Also Friend of: %s" % ', '.join(sorted(followers - friends)))
