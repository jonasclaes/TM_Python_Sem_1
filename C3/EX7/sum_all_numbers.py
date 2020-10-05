start_limit = int(input("Start limit: "))
end_limit = int(input("End limit: "))

sum = start_limit

if start_limit == end_limit:
    print("Sum of numbers from", start_limit, "till", end_limit)
    print(start_limit)
elif start_limit > end_limit:
    print("The start limit must be smaller than the end limit!")
else:
    print("Sum of numbers from", start_limit, "till", end_limit)
    for i in range(start_limit + 1, end_limit + 1):
        sum += i
        print("+", i, "-->", sum)
