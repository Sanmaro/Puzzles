def queue_time(customers, n):
    count = 0
    if customers:
        while set(customers) != {"x"}:
            for i in range(n):
                try:
                    customers[i] -= 1
                except (IndexError, TypeError):
                    continue
            while 0 in customers:
                for customer in customers:
                    if customer == 0: 
                        customers.remove(customer)
                        customers.append("x")
            count += 1
    return count

print(queue_time([], 2))
print(queue_time([5], 1))
print(queue_time([2], 5))
print(queue_time([1,2,3,4,5], 1))
print(queue_time([1,2,3,4,5], 100))
print(queue_time([2,2,3,3,4,4], 2))